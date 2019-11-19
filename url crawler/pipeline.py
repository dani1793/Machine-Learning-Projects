#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:48:48 2019

@author: daniyalusmani
"""
from multiprocessing import Pool
from website import Website
from file_reader import CsvReader

import csv

class Pipeline:
    def __init__(self, fileName, inputDelimiter, batchSize, outputFile, outputDelimiter):
        self.csvReader = CsvReader(fileName, batchSize, inputDelimiter);
        self._outputFile = outputFile
        self._outputDelimiter = outputDelimiter
        
    def crawlWebsite(self, url, regexPatterns):
        # print('processing for url %s'%(url))
        website = Website(url, regexPatterns)
        website.crawlForPatterns()
        # print('processing ended for url %s'%(url))
        return website.convertResultsToMatrix()
    
    def crawlUrlBatch(self, urlRegexTupleArr, poolNum=10):
        pool = Pool(processes=poolNum)
        res = pool.starmap_async(self.crawlWebsite, iter(urlRegexTupleArr))
        pool.close()
        pool.join()
        return res.get()
    
    def startCrawl(self):
        for urlRegexTupleArr in self.csvReader.getBatches():
            print('crawling batch');
            writeData = self.crawlUrlBatch(urlRegexTupleArr);
            print('writing results to csv');
            self.writeToCSV(writeData)
    
    def writeToCSV(self, data):
        with open(self._outputFile, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=self._outputDelimiter, quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in data:
                try:
                    writer.writerow(row)
                except:
                    writer.writerow(['','','','Error writing to csv'])
                        

    
    
     