# -*- coding: utf-8 -*-

import dash_html_components as html
import colors as colors
import countries_dropdown as countries_dropdown


country = 'France'
 
colors = colors.get()

def get_content():
  return html.Div([
    html.H6(
        children='Select your country',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div([
      html.Div([
        countries_dropdown.get()
      ])
    ]),
    html.Div(id='country-data'),
  ])
