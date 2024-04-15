from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objects as go
import sqlite3
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='cpu') #mettre 2 colonnes ,dcc.Graph(id='ram', width = 6)
        )
    ]),
    dcc.Interval(id='internal-component', 
                 interval=10000,
                 n_intervals=0
    )
],fluid=True)

@app.callback( #liste mettre des []
    Output('cpu', 'figure'),
    Input('internal-component', 'n_intervals'))

def update_graph(n):
    db = sqlite3.connect('Cours_2/PROJET/metrics.db')
    df_cpu = pd.read_sql_query("SELECT * FROM stats", db)
    fig_cpu = go.Figure(data=[go.Scatter(x=df_cpu['time'], y=df_cpu['cpu'])])
    return fig_cpu

if __name__ == '__main__':
    app.run_server(debug=True)



