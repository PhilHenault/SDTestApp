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

new_string = "Hello World"

binary_value = hello_world(new_string, 2)

def hello_world2(string, value):
    """
    Returns True if a value is greater than 1, returns False otherwise.
    """
    if value > 1:
        print(string)
        return True 
    else:
        return False

new_string = "Hello World"

binary_value = hello_world(new_string, 2)