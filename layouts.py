#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:22:16 2019

@author: michael
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from datetime import datetime
from ASXcodes import Options


general_layout = dbc.Container([
        dbc.Row(dbc.Col(html.H1('Share Price History Dashboard'), width='auto')),
        dbc.Row([
           dbc.Col(
                    html.H3("Select share codes:"), 
                    width="6"
                    ),
            dbc.Col(
                    html.H3("Select start and end dates:"), 
                    width="6"
                    )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                        #Where you select the shares
                        id='My_share_codes',
                        options=Options,
                        multi=True
                        ),width=5
                    ),
                dbc.Button(
                    #Where you OK the input
                    'Submit codes',
                    id='submit_codes_button',
                    n_clicks=0
                    ),
            dbc.Col(
                dcc.DatePickerRange(
                        #Where you select the dates
                        id='My_dates',
                        min_date_allowed = datetime(2000, 1, 3),
                        max_date_allowed = datetime.today(),
                        initial_visible_month = datetime(2000, 1, 3),
                        start_date=datetime(2000, 1, 3),
                        end_date = datetime.today()
                        ),
                    width="6"
                    )
        ]),   
        dbc.Row([
            dbc.Col(
                    dcc.Graph(
                            id='My_graph'
                            ),
                    width='9'
                    )                      
            ]),
        # Hidden div inside the app that stores the intermediate value
        html.Div(id='intermediate_value', style={'display': 'none'})
    ],fluid=True)
