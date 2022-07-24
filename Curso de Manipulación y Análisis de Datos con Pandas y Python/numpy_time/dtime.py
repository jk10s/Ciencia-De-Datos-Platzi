#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:08:08 2022

@author: jk10s
"""

import pandas as pd
import numpy as np


import datatime

fecha_ejecucion= datatime.datatime.now()
print(type(fecha_ejecucion))
print(fecha_ejecucion)

fecha_ejecucion.day
fecha_ejecucion.year
fecha_ejecucion.date()
str(fecha_ejecucion)
fecha_ejecucion.strftime("%x")
fecha_ejecucion.strftime()