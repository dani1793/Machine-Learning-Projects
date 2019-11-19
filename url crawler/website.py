#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:43:27 2019

@author: daniyalusmani
"""
from crawler import Crawler

class Website:
    def __init__(self, url, targetPatterns):
        self.url = url
        self.targetPatterns = targetPatterns
        self.crawler = Crawler(self.url)
        self.results = []
    
    def crawlForPatterns(self):
        for target in self.targetPatterns:
            self.results.append(self.crawler.crawl(target))
    
    def convertResultsToMatrix(self):
        res = []
        for result in self.results:
            res.append(result.getContent())
        return res

    