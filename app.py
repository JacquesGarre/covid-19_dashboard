# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import scraper as scrap
import tab1 as tab1
import tab2 as tab2
import tab3 as tab3
import tab4 as tab4
import graph_tab3 as graph_tab3
import chloro_map_tab4 as chloro_map_tab4
import colors as colors

colors = colors.get()

app = dash.Dash(__name__,)

app.config.suppress_callback_exceptions = True

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Covid-19 Statistics',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Today\'s Global Data', value='tab-1'),
        dcc.Tab(label='Historical Global Data', value='tab-2'),
        dcc.Tab(label='Data per country', value='tab-3'),

        dcc.Tab(label='French Data', value='tab-4')
    ]),
    html.Div(id='tabs-content')
])



@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
  if tab == 'tab-1':
    return tab1.get_content()
  elif tab == 'tab-2':
    return tab2.get_content()
  elif tab == 'tab-3':
    return tab3.get_content()
  elif tab == 'tab-4' :
    return tab4.get_content()

@app.callback(Output('country-data', 'children'),
              [Input('countries-dropdown', 'value')])
def return_graph(country):
    print('go tab3 callback')
    return graph_tab3.get_content(country)

@app.callback(Output('french_map', 'children'),
              [Input('check_option', 'value'),
               Input('crossfilter-year-slider', 'value')])
def return_chloroMap(case, id_date):
    print('go chloro' + 'date = '+str(id_date))
    return chloro_map_tab4.get_content(case, id_date)



if __name__ == '__main__':
    app.run_server(debug=False)