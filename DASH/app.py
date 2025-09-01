import pandas as pd
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objs as go

# Removed deprecated imports for dash_html_components and dash_core_components
import dash
from dash import html, dcc

data = px.data.gapminder()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(style={'color': '#7FDBFF','border': '3px solid #7FDBFF','float': 'left','width': '100%','height': '50px'}, children=[html.H1("Hello Dash",style={'textAlign': 'center','color': 'red'})]),
    
    html.Div(style={'color': '#7FDBFF','border': '3px solid #7FDBFF','float': 'left','width': '49%','height': '350px'}, children=[dcc.Graph(id='scatter-plot',figure={'data':[go.Scatter(x = data['pop'], y=data['gdpPercap'], mode = 'markers')],'layout':go.Layout(title="Scatter Plot")})]),

    html.Div(style={'color': '#7FDBFF','border': '3px solid #7FDBFF','float': 'left','width': '49%','height': '350px'}, children=[dcc.Graph(id='box-plot',figure={'data':[go.Box(x=data['gdpPercap'])],'layout':go.Layout(title="Box Plot")})])
 
])

# print(data.head(2)) 


if __name__ == '__main__':
    app.run(debug=True)