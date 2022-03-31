# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:44:20 2021

@author: Balaji Kannigesvaran
"""


"From corey schafer youtube channel pandas playlist"

import pandas as pd
df1=pd.read_csv('PANDAS\STACK OVERFLOW SURVEY\survey_results_public.csv')
pd.set_option('display.max_columns', 48)
pd.set_option('display.max_rows', 48)
print(df1)
print(df1.shape)
print(df1.info())
df2=pd.read_csv('PANDAS\STACK OVERFLOW SURVEY\survey_results_schema.csv')
print(df2.head)
