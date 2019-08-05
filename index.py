#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:15:29 2019

@author: michael
"""

#import dash_core_components as dcc
import dash_html_components as html



# see https://community.plot.ly/t/nolayoutexception-on-deployment-of-multi-page-dash-app-example-code/12463/2?u=dcomfort
from app import app
from layouts import general_layout


app.layout = html.Div([
                html.Div(id='page-content',
                children=general_layout
                )
])


if __name__ == '__main__':
    app.run_server(debug='on')