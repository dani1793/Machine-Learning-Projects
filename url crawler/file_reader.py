#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:27:35 2019

@author: daniyalusmani
"""



import csv

class CsvReader:
    def __init__(self, filename, batchSize, delimiter):
        self._filename = filename
        self._batchSize = batchSize
        self._delimiter = delimiter
        self._urlBatch = []

    def getBatches(self):
        with open(self._filename, newline='') as csvfile:
            datareader = csv.reader(csvfile, delimiter=self._delimiter, quotechar='|')
            count = 0
            batch = 0
            for row in datareader:
                count += 1
                self.addToUrlBatch(row)
                if count == self._batchSize:
                    batch += 1
                    print('processing url %s'%(batch * self._batchSize))
                    yield self._urlBatch
                    count = 0
                    self._urlBatch = []
                    print
        
    def convertToTuple(self, row):
        return (row[0], [row[i] for i in range(1,len(row))])
    
    def addToUrlBatch(self, row):
        urlTuple = self.convertToTuple(row)
        self._urlBatch.append(urlTuple)