#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:02:36 2018

@author: daniyalusmani
"""

import numpy as np;

# order for row wise and column wise
#    NI, DC, I, VI, M 
# NI
# DC
# I
# VI
# M

transMatPref = [[ 0,        1.0,                    0,                  0,                  0   ],
                [ 0,        0.6168790945,           0.0260357029,       0.0299401198,       0   ],
                [ 0,        0.0299682766,           0.0766523380,       0.0007696206,       0   ],
                [ 0,        0.0386969009,           0.0003284966,       0.1807294502 ,      0   ],
                [ 0,        1,                      0,                  0,                  0   ]]

transMatPref = np.array(transMatPref)
transMatPref[0] = transMatPref[0]/sum(transMatPref[0])
transMatPref[1] = transMatPref[1]/sum(transMatPref[1])
transMatPref[2] = transMatPref[2]/sum(transMatPref[2])
transMatPref[3] = transMatPref[3]/sum(transMatPref[3])
transMatPref[4] = transMatPref[4]/sum(transMatPref[4])

transMatNonPref = [[ 0.0,     1.0,                  0.00,               0.00,               0   ],
                   [ 0.0,     0.6607942626,         0.0299411806,       0.0203704819,       0   ],
                   [ 0.0,     0.0342622984,         0.0865041605,       0.0005520592,       0   ],
                   [ 0.0,     0.0274679555,         0.0001726440,       0.1399239162,       0   ],
                   [ 0.0,     1.0,                  0.00,               0.00,               0   ],]

transMatNonPref = np.array(transMatNonPref)
transMatNonPref[0] = transMatNonPref[0]/sum(transMatNonPref[0])
transMatNonPref[1] = transMatNonPref[1]/sum(transMatNonPref[1])
transMatNonPref[2] = transMatNonPref[2]/sum(transMatNonPref[2])
transMatNonPref[3] = transMatNonPref[3]/sum(transMatNonPref[3])
transMatNonPref[4] = transMatNonPref[4]/sum(transMatNonPref[4])



class User():
    # uid is a string or integer as unique identify for the user
    # categories is an integer representing total number of categories the user is interested in
    # timeSpan is an integer representing total number of days the training is considering
    # actionSpace is an array of actions and their respective values
    # preferenceCategory is array with the number of categories which represents preference categories of user
    # preferenceTime is array with numbers showing the days that are preference to the user
    def __init__(self, uid, categories, timeSpan, actionSpace, preferencesCategory, preferenceTime):
        
        # unique id
        self.id = uid
        
        # probabiliy that the user could choose randomly from any of the provided actions on runtime
        self.randomActionChoiceProb = 0.001;
        
        self.actionSpace = actionSpace
        
        self.previousAction = np.zeros((categories,1),dtype=int)
        
        # preferences that which category user likes
        self.priorPreferencesCategory = preferencesCategory
        # Preference time in which the probabily of meeting is really high
        self.priorPreferenceTime = preferenceTime
        
        # Total number of categories available (k)
        self.categories = categories
        
        # Total time span required for offline training (t)
        self.timeSpan = timeSpan
        
        # TODO: What happens when the user unsubscribe to one of the categoriers (or all the categories)
        # Have to build that logic in the class as well
        
        self._initial_user_state()
        
        # t x k array for prior of response for each of the category for each time step
        self.response = self._generateYearlyResponse();
        
        # Flag indicating that the user has unsubscribed from this category
        self.unSubscribed = np.zeros(categories, dtype=bool)
    
    def _initial_user_state(self):
    
        for i in range(self.categories):
            if i in self.priorPreferencesCategory:
                 self.previousAction[i] = 1
            else :
                self.previousAction[i] = 0
                        

    
    # gets a number representing the category and returns the probabily
    # it is assumed that the user actions are in the following sequence
    # un_subscribe
    # ignore
    # click
    # open
    # meeting
    def _get_action_for_category(self, category, isPreferenceTime):
        currentAction = 1;
        if category in self.priorPreferencesCategory:
            if isPreferenceTime == True:
                currentAction = np.random.choice(self.actionSpace, 1, p= transMatPref[self.previousAction[category][0]])[0]
                # Low rate of un_subscription
                # A little higher rate of Ignore
                # Highest rate of click
                # High rate of open
                # return np.random.choice(self.actionSpace, 1, p= np.random.dirichlet((0.01,3,9,7),1)[0])[0]
            else:
                currentAction = np.random.choice(self.actionSpace, 1, p= transMatPref[self.previousAction[category][0]])[0]
                # Low rate of un_subscription
                # high rate of Ignore
                # High rate of click
                # High rate of open
                # return np.random.choice(self.actionSpace,1, p = np.random.dirichlet((0.01,5,5,4),1)[0])[0]
        else:
            if isPreferenceTime == True:
                currentAction = np.random.choice(self.actionSpace, 1, p= transMatNonPref[self.previousAction[category][0]])[0]
                #return np.random.choice(self.actionSpace,1, p = np.random.dirichlet((5,4,2,1),1)[0])[0]
            else:
                currentAction = np.random.choice(self.actionSpace, 1, p= transMatNonPref[self.previousAction[category][0]])[0]
               # return np.random.choice(self.actionSpace,1, p = np.random.dirichlet((7,6,2,1),1)[0])[0]
        self.previousAction[category] = currentAction;
        return currentAction
        
    # t x k array for prior of response for each of the category for each time step
    def _generateYearlyResponse(self):
        response = np.zeros((self.timeSpan,self.categories));
        for i in range(self.timeSpan):
            isPreferenceTime = i in self.priorPreferenceTime
            for j in range(self.categories):
                response[i][j] = int(self._get_action_for_category(j,isPreferenceTime));
        return response  
     
    def set_unsubscribed(self,category):
        self.unSubscribed[category] = True;
                       
    # category is index of category for which the response is required
    # This function should be used to get the response of user at runtime
    # TODO: When the user unsubscribe from the category, he would be uable to receive the email anymore
    def get_response(self, category, time):
        if  self.unSubscribed[category] == True:
            return 0.0
        else:
            priorResponse = self.response[time][category]
            u = np.random.uniform()
            if u < self.randomActionChoiceProb and category not in self.priorPreferencesCategory:
                return np.random.choice(self.actionSpace,1)[0]
            else:
                return priorResponse
 
    def reset(self):
        self.unSubscribed = np.zeros(self.categories, dtype=bool);