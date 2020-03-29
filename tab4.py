# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 05:14:24 2020

@author: MonOrdiPro
"""

import dash_core_components as dcc
import dash_html_components as html
import colors as colors
import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
csv_file = os.path.join(dir_path, 'map/data_clean_28_03.csv')
df = pd.read_csv(csv_file, encoding='utf-8') 
colors = colors.get()

data_folder = './map/archive'
files = [f for f in os.listdir(data_folder) if os.path.isfile(os.path.join(data_folder, f))]
jours = {}
i=0
for elt in files :
    jours[i] = elt[-9:-4]
    i+=1
    

def get_content():
  return html.Div([

    html.Div([
        html.H6(
            children='France data per department\n( last update : 2020-03-28 )',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),
        html.Br(),
        html.Br(),
        dcc.RadioItems(
                        className='radio',
                        id='check_option',
                        style={
                                'height': '40px',
                                'align-items': 'center',
                                'background-color': '#2d2d2d',
                                'width': '57%',
                                'left': '23%',
                                'position': 'absolute',
                                'display': 'flex',
                                'justify-content' : 'space-evenly',
                                'color' : 'rgb(186, 137, 126)',
                                'border-radius': '14px',
                                'box-shadow': 'rgb(132, 107, 107) 0px 0px 10px',
                            },
                        options = [
                                {'label' : 'Mort', 'value' : 'mort'},
                                {'label' : 'hospitalisation' , 'value' : 'hospitalisation'},
                                {'label' : 'réanimation', 'value' : 'reanimation'}
                                ],
                        value = 'mort'),
        html.Br(),
        html.Br(),
        html.Br(),

        

    ]),
    html.Div(id='french_map'),
    
    html.Div(dcc.Slider(
    id='crossfilter-year-slider',
    min=0,
    max=len(files)-1,
    value=len(files)-1,
    marks=jours,
    step=None
    ))

  ])