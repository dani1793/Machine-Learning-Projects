#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 22:44:04 2019

@author: daniyalusmani
"""

from crontab import CronTab
import os
print(os.environ['HOME'])

class Cron:
     def __init__(self, username):
         self.myCron = CronTab(user=username)
         self._username = username
         self.myCron.env['PATH'] = os.environ['PATH']
         self.myCron.env['SHELL'] = os.environ['SHELL']
     def stopCron(self, comment):
         if comment:
             print('stopping cron jobs with comment %s'%(comment))
             self.myCron.remove_all(comment=comment)
         else:
             print('stopping all cron jobs')
             self.myCron.remove_all()
         self.myCron.write()
         
     def setupCron(self, command, comment, hour, day):
        try:    
            print('trying to execute command %s'%(command))
            if comment:
                job = self.myCron.new(command=command,comment=comment) 
            else:
                job = self.myCron.new(command=command) 
            if hour:
                job.hour.every(int(hour))
                
            if day:
                job.day.every(int(day))
            self.myCron.write()
            
            print('cron items for %s'%(self._username))
            for item in self.myCron:
                print(item)
        except:
            print('The arguments provided are not correct. Unable to create cron job')
