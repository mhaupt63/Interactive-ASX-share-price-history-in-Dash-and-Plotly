#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:31:47 2019

@author: michael
"""

from dash.dependencies import Input, Output, State
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
import pandas as pd
import numpy as np
from app import app
import plotly.graph_objs as go



pd.options.mode.chained_assignment = None


    
######################## Callbacks ######################## 


@app.callback(
    # Get entire share price history and store it in hidden division
    Output('intermediate_value', 'children'),
    [Input('submit_codes_button','n_clicks')],
    [State('My_share_codes', 'value')])
def get_share_history(n_clicks,share_codes):
    API_key='XH54GUPF1RTEUC3P'
    ts= TimeSeries(key=API_key,output_format='pandas', indexing_type='date')
    traces=pd.DataFrame(columns=['date'])
    for tic in share_codes:
        print('here is ',tic)
        data, meta_data = ts.get_daily(symbol=tic+'.AX',outputsize='full')
        #Clean up missing/zero data
        data.replace(0,np.nan, inplace=True)
        data.fillna(method='pad', limit=2)
        data.columns=data.columns+tic
        print('appending ')
        traces=pd.merge(traces, data, on='date', how='outer')
    return traces.to_json(date_format='iso',orient='split')

@app.callback(
    # Filter share price on date range
    Output('My_graph', 'figure'),
    [Input('intermediate_value', 'children'),
     Input('My_dates', 'start_date'),
     Input('My_dates', 'end_date')])
def update_graph(json_data, start_date, end_date):
    # Recover dataframe, filter by date and create graph
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    df = pd.read_json(json_data,orient='split')
    df.index=pd.to_datetime(df['date'])
    df=df.sort_index()
    df = df.loc[start:end]
    #contruct traces list
    #data=data['4. close'] 
    share_codes=set(df.columns.str[-3:])
    #share_codes=set(share_codes)
    share_codes.remove('ate')
    print('here are ',share_codes)
    
    
    traces = [go.Scatter({
        'x': df['date'],
        'y': df['4. close'+code],
        'name': code
    }) for code in share_codes]
    
    fig = go.Figure(data=traces, layout={'title':','.join(share_codes)+' daily close'})
    return fig

