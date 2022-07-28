#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 16:41:20 2022

@author: jk10s
"""

import pandas as pd

cancer_mama= pd.read_excel('bcancer.xlsx')

#titanic
titanic= pd.read_csv('https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv')
wine= pd.read_csv('red_wine.csv', sep=(';'))

covidd =  pd.read_csv('covid_20200430.csv')
covidd.info()