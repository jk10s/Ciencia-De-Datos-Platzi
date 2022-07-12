#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 14:33:50 2022

@author: jk10s
"""

import pandas as pd

cancer_mama= pd.read_excel('bcancer.xlsx')

#titanic
titanic= pd.read_csv('https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv')
wine= pd.read_csv('red_wine.csv', sep=(';'))
#json_covid = requests.get('covid19api.com/summary').json()
#el antriono sirve por que el link eata roto
covidd =  pd.read_csv('covid_20200430.csv')
covidd.info()
wine.describe()
titanic.index
nosbres = list(titanic.Name)
litas= list(titanic.columns)
print(litas)
titanic1 = titanic[['Name', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard', 'Fare','Survived', 'Pclass']]
cancer_mama.index = cancer_mama["id"]
cancer_mama.drop(["id"],axis=1, inplace=True)
col_cancer= list(cancer_mama.columns)
col_cancer.remove("radius_mean")
cancer_mama = cancer_mama[col_cancer]

# acceder a valorres con ILOC LOC 
cancer_mama.loc[842302]
cancer_mama.loc[842302,"diagnosis"]
cancer_mama.loc[[842302, 842517]]
cancer_mama.loc[[842302, 842517],["diagnosis","texture_mean"]]

#utilizando scling  (index,columnas) orden esencial de sciling
covidd_= covidd.loc[0:49]
titanic.head(50)
covidd_.iloc[0,0]
covidd_.iloc[0,1]
covidd_.iloc[1,0]
covidd.iloc[:20,:4]
#ejemplo los ultimo 50 registros (inidices) de la ultima columna(-1)
covidd.iloc[-50:-1,:-1]

#filttrandocon operadores logicos
calidad= wine["quality"]==5
rgistro=wine[calidad]
calidad6= (wine["quality"]==5) | (wine["quality"]==6)
registro6 = wine[calidad6]

#medidas aritmrticas
wine.mean()
wine.std()
wine.median()
wine["quality"].value_counts()
titanic["Survived"].value_counts()
cancer_mama["diagnosis"].value_counts()

#creando nuevas clumnas devirivadas
covidd["Deataread"]=1
lista_covid= list(covidd.columns)
covidd["Deataread"]=covidd["TotalDeaths"]/covidd["TotalConfirmed"]
covidd.sort_values("Deataread", ascending=False, inplace=True)

# aolicando funciones a lamediada sobre las series
titanic["sisobrevivio"] = titanic["Survived"].map({0:"murio",1:"sobrevivio"})
titanic["sisobrevivio"].value_counts()

series_upper= lambda x: x.upper()
name_upper = titanic["Name"].map(series_upper)
name_upper1 = titanic["Name"].str.upper()

# aplicando funciones ala medida sobre dataframes (varias columnas)
upper_data= titanic[["Name","Sex"]].applymap(series_upper)
df_lower= lambda x: x.lower() if type(x)== str else x
titanic = titanic.applymap(df_lower)
import numpy as np
wine.apply(np.sum, axis=1)
titanic_= titanic.apply(df_lower)

import pandas as pd
import datetime

#FECHAS CON DATETIME
fecha_ejecucion = datetime.datetime.now()
print(type(fecha_ejecucion))
print(fecha_ejecucion)

fecha_ejecucion.year
fecha_ejecucion.day
fecha_ejecucion.date()
str(fecha_ejecucion.date())

fecha_ejecucion.strftime("%x")
fecha_ejecucion.strftime("%X")
fecha_ejecucion.strftime("%A")

fecha_ejecucion.date() + datetime.timedelta(days=10)
str(fecha_ejecucion.date() + datetime.timedelta(days=-2))

pd.to_datetime("05/15/2020")
pd.to_datetime("2020-05-15")
pd.to_datetime("20200515")
pd.to_datetime("20201205")
pd.to_datetime("20201205", format="%Y%d%m")

#ejercico de germany

energy= pd.read_csv("germani.csv")
energy.dtypes
type(energy.iloc[0,0])
energy.index = energy["Date"]
type(energy.index[0])
energy.drop("Date",axis=1, inplace=True)

energy = energy.loc["2014":]
energy = energy.loc["2014-06":]
#fltrado deindices por scling
energy = energy.loc["2014-06":"2017-06"]
#devolver el index redefine e indice
energy.reset_index(inplace=True)
#condicional con string
energy = energy[energy["Date"] > "2015"]

#conveirte la columna date en tipo datetime
energy["Date"] = pd.to_datetime(energy["Date"] )
energy.dtypes
energy.plot(x="Date")
energy["year"] = energy["Date"].dt.year
energy["dia"] = energy["Date"].dt.day
energy["dayofwwek"] = energy["Date"].dt.dayofweek
energy["dayofwwek_name"] = energy["Date"].dt.strftime("%A")
energy.columns
energy = energy.drop(["year","dia","dayofwwek","dayofwwek_name"], axis=1)

#resamplo funcion
m_energy = energy.resample("M",on="Date").sum()
m_energy.plot()
