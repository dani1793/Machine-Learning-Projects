#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 21:00:03 2018

@author: daniyalusmani
"""

from user import User;
from agent import Agent;

import numpy as np;
import random
import time

# Training loop
episodes = 20000
test_episodes = 5;

# Parameters
gamma = 0.2
alpha = 0.2
a = 1000

epl_avg = []

eta = 0.1;


TIME_SPAN = 365
USERS = 5
CATEGORIES = 10
ACTION_SPACE = 5
ep_lengths = np.zeros((CATEGORIES, episodes+test_episodes));

users = []
agent = Agent(TIME_SPAN, USERS)

# generate users array which contains response for each user.
# The user have response for each category for all the days defined in TIME_SPAN
# The shape of user is (TIME_SPAN x CATEGORIES), and each category represent action taken by user for that category
def generateUsers(numUsers, pereferedCatCount = 3, preferedDayCount= 60):
    users = []
    for i in range(numUsers):
        # TODO: The prefered time is not grouped together, if the results are not good we can create group of perefered Days
        u = User(i, CATEGORIES, TIME_SPAN, ACTION_SPACE, random.sample(range(CATEGORIES), pereferedCatCount), random.sample(range(TIME_SPAN), preferedDayCount))
        users.append(u)
    return users

# This simulate data. It is assumed that an unintelligent agent would send email of every category to every user
# The data generated would contain the response of each user for each day of the time span for each category    
def generateData(users):
    sample = np.zeros((TIME_SPAN, USERS, CATEGORIES))
    for t in range(TIME_SPAN):
        for u in range(USERS):
            sample[t][u] = users[u].response[t]
    return sample


def nextStep(cat, state, action):
    userResponse = int(users[action].get_response(cat,state))
    done = False
    reward = 0
    if userResponse == 0:
        # TODO: Check if the algo does not work
        # Give high negative response and set flag on the user to give high negtaive response after wards till it is reset
        users[action].set_unsubscribed(cat)
        done = True
        reward = -1000
    elif userResponse == 1:
        reward = 0
    elif userResponse == 2:
        reward = 10
    elif userResponse == 3:
        reward = 50
    elif userResponse == 4:
        reward = 100
    if state == TIME_SPAN - 2:
        done = True;

    return state + 1, reward, done

def reset():
    for u in users:
        u.reset()


users = generateUsers(USERS)

sample = generateData(users)


# ---------------------------- Approch 1 ----------------------------------------------
# We train Q Learning for each mailing list (ML) individually
# The users are the actions and we learn the Q values for each user over the period of time
# The accumulated Q values would tell us which user belong to which mailing list
# We could implement DQN for this as well as we need to update the Q values for each user at each time step
        
# ---------------------------- Approch 2 ----------------------------------------------
# We train the Q Learning for all the users individually.
# For each user and each category we have the action for agent (SENT, NOT SENT). We make the agent learn so that it 
# sends the mail only to the user that have preference to it or preferred category.
# This approach is not scalable, as the number of user grows agent would have to itegrate over them and learn data set.
# Moreoever, the space required for this Tabular Q Learning would not work for large number of users due to space complexity

# When the user unsubscribe from the list, the agent should have -10,or -1000 reward and the iteration should stop
# Future work (Find the pattern in different users activity and update the category of users Q Learning)

def train(cat):
    for ep in range(episodes+test_episodes):
        # Initialize things
        state = 0;
        done = False;
        steps = 0;
          #  global totalUnSubscriptions;
          #  totalUnSubscriptions = 0;
        
        eta = a/(a + ep);
        reset()
                    
        # Loop through the episode
        while not done:                           
            if np.random.uniform(0, 1) < eta:
               action = agent.randomAction() # Explore action space
            else:            
               action = np.argmax(agent.qValues[state]) # Exploit learned values
               
            next_state, reward, done = nextStep(cat, state, action)        
        
            old_value = agent.qValues[state][action]
            next_max = np.max(agent.qValues[next_state]);
            
            new_value = old_value + alpha * (reward + gamma * next_max - old_value)
            agent.qValues[state][action] = new_value
            
            state = next_state;
        
            steps += 1
                    
        # Bookkeeping for plots
        # ep_lengths.append(steps)
        ep_lengths[cat,ep]= steps;
        epl_avg.append(np.mean(ep_lengths[min(0, ep-500):]))
        if ep % 1000 == 0:
            print('steps takein in this episode', steps)
            print("Episode {}, average timesteps: {:.2f}".format(ep, np.mean(ep_lengths[cat, min(0, ep-100):ep])))

      

# This gives us the information for single mailing list.
# The response of all the users for single mailing list for 365 days of year
sampleML0 = np.swapaxes(sample,2,0)[0]      

# Save users metadata
np.save("users-cat-4.npy", users)

# Train different categories and save results
for i in range(CATEGORIES):
    print('PROCESSING CATEGORY {}'.format(i));
    agent = Agent(TIME_SPAN, USERS)
    train(i)
    np.save("q_values-cat-4-{}.npy".format(i), agent.qValues)
    np.save("data-cat-4-ML{}.npy".format(i), np.swapaxes(sample,2,0)[i])
    time.sleep(2)

# save lengths of episodes for plotting
np.save("episode-steps-4.npy", ep_lengths)