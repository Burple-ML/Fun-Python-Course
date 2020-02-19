#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 11:52:24 2019

@author: raghav
"""

import requests
import os
def read_text():
    quotes=open("/Users/raghav/Desktop/Udacity course/movie_quotes.txt")
    contents_of_file=quotes.read()
    print(contents_of_file)
    quotes.close
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = requests.get("http://www.wdylike.appspot.com/?q="+text_to_check)           
    
    print(connection.text)
    
    
read_text()    
