# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
pob=pd.read_csv('jk10s/poblacion.csv',encoding="latin1")
pob.info()
sample= pob.sample(100)
sample