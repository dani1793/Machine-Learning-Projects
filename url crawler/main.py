#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 01:04:10 2019

@author: daniyalusmani
"""

import argparse
from datetime import datetime 
from pipeline import Pipeline


parser = argparse.ArgumentParser(description='Url Crawler')

parser.add_argument('--input-file', 
                    default='./input.csv',
                    help='input csv file according to the provided format (default: ./input.csv)')

parser.add_argument('--output-file', 
                    default='./out.csv',
                    help='path to output csv file (default: ./out.csv)')

parser.add_argument('--batch-size', 
                    default=25,
                    help='batch size for processing urls (default: 25)')


parser.add_argument('--input-delimiter', 
                    default=';',
                    help='input csv file according to the provided format (default: ./input.csv)')

parser.add_argument('--output-delimiter', 
                    default=',',
                    help='path to output csv file (default: ./out.csv)')


args = parser.parse_args()
print(args)



if __name__ == '__main__':
    start = datetime.now()
    print('Starting Crawler at {}'.format(start))
    pipeline = Pipeline(args.input_file, args.input_delimiter, int(args.batch_size), args.output_file, args.output_delimiter)
    pipeline.startCrawl()
    end = datetime.now()
    print('Crawler ended at {}'.format(end))
    print('Time taken by crawler %s'%(end - start))