#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:53:01 2019

@author: michael
"""
import pyasx.data.companies
import pandas as pd


#get list of ASX codes
ASX_Data = pyasx.data.companies.get_listed_companies()
ASX_Df=pd.DataFrame(ASX_Data)
ASX_Df.set_index('ticker',inplace=True)
Options=[]
for tic in ASX_Df.index:
    Options.append({'label':'{} {}'.format(tic,ASX_Df.loc[tic]['name']), 'value':tic})
#Append ETF codes
ETFdf = pd.read_csv('~/Plotly-Dashboards-with-Dash/Data/Oz-etfs.csv')
#csv loaded from https://www.asxetfs.com/
ETFdf.columns=['ticker','name']
ETFdf.set_index('ticker',inplace=True)
for tic in ETFdf.index:
    Options.append({'label':'{} {}'.format(tic,ETFdf.loc[tic]['name']), 'value':tic})