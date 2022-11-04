from distutils.log import debug
from pickle import TRUE
import dash
from dash import Dash, html, dcc
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import geopandas as gpd
import pandas as pd
import pandas_datareader.data as web
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import search
import dash_cytoscape as cyto

# dash

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
srh = search.getTotal()
srhTweet = search.getTweet()
query = search.getquery()

usuarios = {u["id"]: u for u in srhTweet.includes["users"]}
######################

#######################

geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
map2 = px.scatter_mapbox(geo_df, lat=geo_df.geometry.y,
                         lon=geo_df.geometry.x, hover_name="name", zoom=1)
# mapa
us_cities = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
map = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=[
                        "State", "Population"], color_discrete_sequence=["green"], zoom=0.5, height=350)
map.update_layout(mapbox_style="open-street-map")
map.update_layout(margin={"r": 25, "t": 25, "l": 25, "b": 25})
# map = px.scatter_geo(geo_df,
# lat=geo_df.geometry.y,
# lon=geo_df.geometry.x,
# hover_name="name")

# seccion bootstrap

#fig = go.Figure(data=[go.Pie(labels= ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen'], values= [4500, 2500, 1053, 500], textinfo='label+percent', insidetextorientation='radial')]),
fig = px.pie(values=[9000, 1000, 5000], names=[
             'Positivo', "Negativo", 'Neutral'])
app.layout = html.Div([
    dbc.Col([


        # TITULO HEAD

        dbc.Row([

            dbc.Col(dbc.Card(html.H1("  Analisis de sentimientos Tweeter  ",
                    className='text-center text-primary')), width=6)

        ], align="center", justify="center", style={"padding": "10px"}),
        dbc.Row([

            dbc.Col(dbc.Card(html.H3("Total de Tweet: "+str(
                srh.meta["total_tweet_count"]), className='text-center text-primary')), width=3),
            dbc.Col(dbc.Card(html.H3("Tema consultado: " + str(query), className='text-center text-primary')), width=3)


        ], align="center", justify="center", style={"padding": "10px"}
        ),
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    dbc.Card([html.H3("b_a_k_i_s",className='text-center text-primary'),
                              html.H5("@beatandlove usa lo stesso fondotinta a base di Nutella di Berlusconi",
                                      className='text-center text-primary')]),
dbc.Card([html.H3("lona2havelka",className='text-center text-primary'),
                              html.H5("@mhdksafa Hello all new to USA…my great granddad’s came from Ireland 🇮🇪, Scotland 🏴󠁧󠁢󠁳󠁣󠁴󠁿, and Slovakia 🇸🇰…Welcome to the Chaos, or our messy Republic which we’re still trying to get right😎👍",
                                      className='text-center text-primary')]),
dbc.Card([html.H3("Natsuki_FFEv",className='text-center text-primary'),
                              html.H5("今日からサブうさ🐰ヴィエラのcwlsに参加させて頂いた！わーいわーい🐰ちゃんとSS撮れてなかったので名刺代わりに自機をﾉwTよろしくおねがいしまーす！#USA_oxo_MALE https://t.co/73TlFHYmSk",
                                      className='text-center text-primary')]),
dbc.Card([html.H3("IvvyNemo",className='text-center text-primary'),
                              html.H5("@HusaJaakko My man is learning the hard way that institutional knowledge is more important them 'high IQ' and 'gut feeling'.Can't wait for Elon to ask the USA government to subsidize twitter somehow.",
                                      className='text-center text-primary')]),
dbc.Card([html.H3("roemmermann",className='text-center text-primary'),
                              html.H5("Gibt von JFK ganz tolle Wahlkampfreden, in denen er analysiert, was in USA nach 1945 FALSCH UND IN DER UDSSR RICHTIG GEMACHT WURDE! Dazu gehörte vor allem NW und Ing. Qualifikation!",
                                      className='text-center text-primary')]),
dbc.Card([html.H3("oi_mike_",className='text-center text-primary'),
                              html.H5("não é possível que em pleno 2022 ainda tem gente que usa narguile",
                                      className='text-center text-primary')]),
dbc.Card([html.H3("Ayanami_vanilla",className='text-center text-primary'),
                              html.H5("@__usa__xx それは至福♡ファミマのしっとり海苔の焼きしゃけすき🥺",
                                      className='text-center text-primary')]),
dbc.Card([html.H3("MarciLeeMurray",className='text-center text-primary'),
                              html.H5("@JayinKyiv 💩tin is a COWARD, inferiority complex,&amp; a narcissistic klepto,mass murderer,a modern-day bloodthirsty Caligula.#RussiaisaTerroristState as for their So-Called 'Great Patriotic War' (WW2) the USSR would NEVER Had WON Against sHitler, if not for the UK 🇬🇧 &amp; USA 🇺🇸 HELPING Them! https://t.co/KTjujC1lnl",
                                      className='text-center text-primary')]),
                ]), width=6, style={"max-height": " 500px", "overflow-y": "auto"}),


        ], align="center", justify="center", style={"padding": "10px"}
        ),

        # FIN TITULO HEAD
dbc.Row([
            dbc.Col(dbc.Card(html.H2("Tweet por dia",
                    className='text-center text-primary')), width=4),
            dbc.Col(dbc.Card(html.H2("Porcentaje de emociones",
                    className='text-center text-primary')), width=4),
        ], align="center", justify="center", style={"padding": "10px"}),
        # Tabla
        dbc.Row(
            [

                dbc.Col(dcc.Graph(figure={'data': [

                    {'x': ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "vIERNES", "SABADO", "DOMINGO"],
                     'y': [4000, 7200, 2200, 5030, 6000, 7100, 2200], 'type': 'bar', 'name': 'NUMERO DE TWEET'},

                ],
                    'layout': {
                    'title': 'Tweet por dias'
                }}),
                    width="6",
                ),
                dbc.Col(dcc.Graph(figure=fig), width="6"),
                # labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
                # values = [4500, 2500, 1053, 500]

            ], align="center", justify="center", style={"padding": "10px"}
        ),
        dbc.Row([
            dbc.Col(dbc.Card(html.H2("Localizaciones de tweet",
                    className='text-center text-primary')), width=4),
dbc.Col(dbc.Card(html.H2("Red de usuarios",
                    className='text-center text-primary')), width=4),
        ], align="center", justify="center", style={"padding": "10px"}),
        dbc.Row([

            dbc.Col(dbc.Card(
                dcc.Graph(figure=map)), width="6"),
            dbc.Col(dbc.Card(
                cyto.Cytoscape(
                    id='cytoscape-two-nodes',
                    layout={'name': 'preset'},
                    style={'width': 'auto', 'height': '350px'},
                    elements=[
                        {'data': {'id': '1', 'label': 'Node 1'},
                         'position': {'x': 75, 'y': 75}},
                        {'data': {'id': '2', 'label': 'Node 2'},
                         'position': {'x': 200, 'y': 200}},
                        {'data': {'id': '3', 'label': 'Node 2'},
                         'position': {'x': 100, 'y': 200}},
                        {'data': {'id': '4', 'label': 'Node 2'},
                         'position': {'x': 100, 'y': 400}},
                        {'data': {'id': '5', 'label': 'Node 2'},
                         'position': {'x': 200, 'y': 400}},
                        {'data': {'id': '6', 'label': 'Node 2'},
                         'position': {'x': 100, 'y': 500}},
                        {'data': {'source': '1', 'target': '2'}},
                        {'data': {'source': '1', 'target': '3'}},
                        {'data': {'source': '3', 'target': '4'}},
                        {'data': {'source': '2', 'target': '5'}},
                        {'data': {'source': '4', 'target': '6'}},
                    ],
                )), width=6
            )

        ], align="center", justify="center", style={"padding": "10px"}),

        dbc.Row([

        ], align="center", justify="center", style={"padding": "10px"})
        # FIN TABLA
        # PASTEL

        # FIN PASTEL
    ],
        className="center")
], style={'background-color': '#1CC9E5', "justify-content": "center", "align-items": "center"})

if __name__ == ("__main__"):
    app.run_server(debug=True, port=3000)
