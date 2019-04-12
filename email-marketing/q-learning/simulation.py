#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:22:53 2018

@author: daniyalusmani
"""

import numpy as np
from user import User
import random
from matplotlib import pyplot as plt

TIME_SPAN = 365
USERS = 5
CATEGORIES = 10
ACTION_SPACE = 4

qValues = np.load("q_values-cat-4.npy")
sampleML0 = np.load("data-cat-ML1-4.npy")
users = np.load("users-cat-4.npy")

plt.plot(sampleML0[:,5])
plt.show()

print(qValues.shape)

for u in users:
    print('pref categories :: ', u.priorPreferencesCategory)
    print('pref time :: ', u.priorPreferenceTime)


plt.scatter(sampleML0[2,:],qValues[:,2])


plt.xlabel('User Response')
plt.ylabel('Qvalues')
plt.title('Q values for pref category user')
plt.show()

plt.plot(sampleML0[2,:])

# Normalised [0,3]
#c = (3*(qValues[:,1] - np.min(qValues[:,1]))/np.ptp(qValues[:,1]))
c = qValues[:,2]
plt.plot(c)
plt.xlabel('User Response')
plt.ylabel('Qvalues')
plt.title('Q values for pref category user')
plt.show()

plt.scatter(sampleML0[1,:],qValues[:,1])

plt.xlabel('User Response')
plt.ylabel('Qvalues')
plt.title('Q values for non pref category user')
plt.show()

plt.plot(sampleML0[1,:])
# Normalised [0,3]
#c = (3*(qValues[:,0] - np.min(qValues[:,0]))/np.ptp(qValues[:,0]))
c = qValues[:,1]
plt.plot(c)
plt.xlabel('User Response')
plt.ylabel('Qvalues')
plt.title('Q values for not pref category user')
plt.show()
 
corr = np.corrcoef(sampleML0[1,:], qValues[:,1])
print(corr)
corr = np.corrcoef(sampleML0[0,:], qValues[:,0])
print(corr)
corr = np.corrcoef(sampleML0[2,:], qValues[:,2])
print(corr)
corr = np.corrcoef(sampleML0[3,:], qValues[:,3])
print(corr)
corr = np.corrcoef(sampleML0[4,:], qValues[:,4])
print(corr)
