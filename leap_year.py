# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 17:07:25 2019

@author: pavan
"""
import random
year = random.randint(1993,2020)
print(year)
if (year%4==0 and year%100!=0 or year%400==0):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")