# Introduction

This project uses Q Learning based Reinforcement Learning agent to predict optimal time for sending multiple category emails to different type of users.

# Usage

The reporting code could be found in this current directory. However the code which was used to train the RL agent and simulate the user behavior could be found in Q learning folder.
The code in q-learning runs on the user simulation so it does not take any input. The following steps should be followed in order to run the code

- Set Transition matrix for user data in user.py
- Set the parameters in train.py and train the models. Set the names at the end of the file to save the results
- Once the agents are trained use simulation.py to get to know the characteristics of each user.
- Final Q values obtained could be used to extract reports using rl-visualization.R

Report for the project could be found (here)[https://dani1793.github.io/machine-learning-portfolio/email-marketing/].





