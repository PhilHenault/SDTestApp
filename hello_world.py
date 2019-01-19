#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:19:44 2018

@author: pdhenault
"""

"""
Contains a function that returns True if a value 
is greater than 1, returns False otherwise.
"""

def hello_world(string, value):
    """
    Returns True if a value is greater than 1, returns False otherwise.
    """
    if value > 1:
        print(string)
        return True 
    else:
        return False


value = hello_world("HELLO WORLD!!", 4)
