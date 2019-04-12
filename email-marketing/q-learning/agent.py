#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 18:01:33 2018

@author: daniyalusmani
"""

import numpy as np

class Agent():
    def __init__(self, time, users):
        self.userActions = {
                'UN_SUBSCRIBE': 0,
                'IGNORE': 1,
                'CLICK': 2,
                'OPEN':3,
                'MEETING': 4
                }
        self.actions = {
                'SEND': 0,
                'IGNORE': 1,
                }
        self.users = users;
        # Q values are the number of time steps by user by the actions available
        # self.qValues= np.zeros((time,users,4))
        
        # Agent would have different mailing list and each mailing would have different users attached to them
        # for now we are considering only one mailing list
        self.qValues= np.zeros((time,users))



    def get_action(self, time, user):
        int(np.random(0,4))
    
    def randomAction(self):
        return np.random.choice([i for i in range(self.users)], 1)[0];
        
    