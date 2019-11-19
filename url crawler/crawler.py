#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:45:37 2019

@author: daniyalusmani
"""

import requests
from content import Content
from bs4 import BeautifulSoup
import re

class Crawler:
    def __init__(self, url):
        self._url = url
        self._pageSoup = self.getPage();
    
    def getPage(self):
        try:
            req = requests.get(self._url)
        except requests.exceptions.RequestException:
            return None        
        return BeautifulSoup(req.text, 'html.parser')

    def parse(self, bs, target):
        """
        Extract content from a given page URL
        """
        res = ''
        try:
            res = bs.find_all(string=re.compile(target))
        except:
            res = ['Unable to parse']
        finally:
            return str(res)
            
    def crawl(self,regexPattern):
        return Content(self._url, regexPattern, self.parse(self._pageSoup, regexPattern))
        