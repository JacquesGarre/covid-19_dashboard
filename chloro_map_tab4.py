# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 04:33:03 2020

@author: MonOrdiPro
"""
import dash_core_components as dcc
import dash_html_components as html
import colors as colors
import json
import pandas as pd
import plotly.express as px
import pie_gender as pie_gender
import os

# gestion du style html
colors = colors.get()

# recuperation du geojson
dir_path = os.path.dirname(os.path.realpath(__file__))
geojson_file = os.path.join(dir_path, 'map/departements.geojson')
csv_file = os.path.join(dir_path, 'map/data_clean_28_03.csv')

with open(geojson_file, 'r', encoding='utf-8') as f:
    t = f.read()
    locations = json.loads(t)
    
# recuperation des données journalieres
data_folder = './map/archive'
files = [f for f in os.listdir(data_folder) if os.path.isfile(os.path.join(data_folder, f))]
datas = {}
for file in files :
    df = pd.read_csv(data_folder+"/"+file, encoding='utf-8') 
    df = df.rename(columns={'Code': 'code'})
    datas[file] = df

# recuperation du bon csv en fonction du slider date
def get_csv(id_date) :
    dir_path = os.path.dirname(os.path.realpath(__file__))
    csv_file = os.path.join(dir_path, 'map\\archive\\'+files[id_date])
    print(csv_file)
    return csv_file



jours = []
for elt in files :
    jours.append(elt[-9:-4])

# a supprimer
    
jours_formate = []
for jour in jours :
    jour_temp = jour[0 :2]
    mois_temp = jour[3:]
    jours_formate.append(mois_temp+"-"+jour_temp)

def get_content(case, id_date) :
    # Récuperation des noms de colonnes utiles en fonction des checkbox (case) et du slider (date)
    col_name = ''
    if case == 'mort' :
        col_name = 'Nombre cumulé total décédées 2020-{}'.format(jours_formate[id_date])
        col_sum_name_h = col_name.replace('total', 'homme')
        col_sum_name_f = col_name.replace('total', 'femme')
    elif case == 'hospitalisation' :
        col_name = 'Nombre total actuellement hospitalisées 2020-{}'.format(jours_formate[id_date])
        col_sum_name_h = col_name.replace('total', 'homme')
        col_sum_name_f = col_name.replace('total', 'femme')
    elif case == 'reanimation' :
        col_name = 'Nombre total actuellement en réanimation ou soins intensifs 2020-{}'.format(jours_formate[id_date])
        col_sum_name_h = col_name.replace('total', 'homme')
        col_sum_name_f = col_name.replace('total', 'femme')
    
    # Récupération du csv correspondant au slider (date)
    df = pd.read_csv(get_csv(id_date), encoding='utf-8') 
    df = df.rename(columns={'Code': 'code'})
    
    
    
    fig = px.choropleth(df, 
                        geojson=locations, 
                        color=col_name,
                        locations="Libellé", 
                        featureidkey="properties.nom", 
                        template="plotly_dark",
                        projection="mercator", 
                        labels={'Nombre cumulé total décédées 2020-{}'.format(jours_formate[id_date]):'nombre de personnes',
                                'Nombre total actuellement hospitalisées 2020-{}'.format(jours_formate[id_date]): 'nombre de personnes',
                                'Nombre total actuellement en réanimation ou soins intensifs 2020-{}'.format(jours_formate[id_date]) : 'nombre de personnes'
                                },

                        
                        
        )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_layout(paper_bgcolor='#111')  
    fig.update_xaxes(fixedrange=True)
    fig.update_yaxes(fixedrange=True)   
    
    nb_homme = df[col_sum_name_h].sum()
    nb_femme = df[col_sum_name_f].sum()
    
    
    
    return  html.Div([
                
                dcc.Graph(
                    className='eight columns',
                    style={
                            'backgroundColor':'#111'
                            },
                    id='French_chloro_map',
                    figure = fig,
                ),
                
                pie_gender.get(nb_homme, nb_femme),
                

                    
            ], className='row',
                style={
                        'vertical-align': 'middle'
                })