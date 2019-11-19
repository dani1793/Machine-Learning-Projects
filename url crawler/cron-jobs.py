#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:01:46 2019

@author: daniyalusmani
"""

	

import argparse
from cron import Cron

parser = argparse.ArgumentParser(description='Url Crawler')

parser.add_argument('--input-file', 
                    default='./input.csv',
                    help='input csv file according to the provided format (default: ./input.csv)')

parser.add_argument('--input-delimiter', 
                    default=';',
                    help='input csv file according to the provided format (default: ./input.csv)')

parser.add_argument('--output-file', 
                    default='./out.csv',
                    help='path to output csv file (default: ./out.csv)')

parser.add_argument('--output-delimiter', 
                    default=',',
                    help='path to output csv file (default: ./out.csv)')

parser.add_argument('--batch-size', 
                    default=25,
                    help='batch size for processing urls (default: 25)')

parser.add_argument('--repeat', 
                    help='schedule the task to repeat after the provided configuration')

parser.add_argument('--cron-user', 
                    help='username to start the cron from')

parser.add_argument('--cron-comment', 
                    help='can be used to identify the cron job')

parser.add_argument('--hour', 
                    help='hour to repeat the task, if 0 means the flag is not set')

parser.add_argument('--day', 
                    help='day to repeat the task, if 0 means the flag is not set')


parser.add_argument('--stop-cron', 
                    help='stop all currently running cron under the provided username')

parser.add_argument('--directory', 
                    help='directory where files are present')

args = parser.parse_args()
print(args)



if __name__ == '__main__':
    if not args.cron_user:
        raise Exception('cron-name not defined. please look at help')
        
    cron = Cron(args.cron_user);
    
    if args.stop_cron:
        print('stopping cron job for username provided');
        cron.stopCron(args.cron_comment)
    else:
        if args.repeat:
            cron.setupCron('python %smain.py --input-file %s --input-delimiter \'%s\' --batch-size \'%s\' --output-file \'%s\' --output-delimiter \'%s\''
                           %(args.directory, args.input_file, args.input_delimiter, args.batch_size, args.output_file, args.output_delimiter), 
                           args.cron_comment, 
                           args.hour, args.day)
        else:
            print('the repeat argument is not set as true, not starting cron job');

 
