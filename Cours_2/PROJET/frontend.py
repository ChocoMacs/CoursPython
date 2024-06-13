from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objects as go
import sqlite3
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='cpu'), width=6 
        ),
        dbc.Col(
            dcc.Graph(id='batt'), width=6
        )
    ]),

    dbc.Row([
        dbc.Col(
            dcc.Graph(id='ram_used'), width=6
        ), 
        dbc.Col(
            dcc.Graph(id='free_disk'), width=6
        )    
    ]),
   
    dcc.Interval(id='internal-component', 
                 interval=10000,
                 n_intervals=0
    )
    ],fluid=True)

@app.callback([
    Output('cpu', 'figure'),
    Output('batt', 'figure'),
    Output('ram_used', 'figure'),
    Output('free_disk', 'figure')
    ],
    Input('internal-component', 'n_intervals'))


def update_graph(n):
   
    db = sqlite3.connect('Cours_2/PROJET/metrics.db')

    df_cpu = pd.read_sql_query("SELECT * FROM stats", db)
    fig_cpu = go.Figure(data=[go.Scatter(x=df_cpu['time'], y=df_cpu['cpu'])])
    fig_cpu.update_layout(title = "Charge CPU (%)")

    df_batt = pd.read_sql_query("SELECT * FROM stats", db)
    fig_batt = go.Figure(data=[go.Scatter(x=df_batt['time'], y=df_batt['batt'])])
    fig_batt.update_layout(title = "Charge BATTERIE (%)")
        
    df_ram = pd.read_sql_query("SELECT * FROM stats", db)
    fig_ram = go.Figure(data=[go.Scatter(x=df_ram['time'], y=df_ram['ram_used'])])
    fig_ram.update_layout(title = "Used RAM  (Gio)")

    # df_ramf = pd.read_sql_query("SELECT * FROM stats", db)
    # fig_ramf = go.Figure(data=[go.Scatter(x=df_ramf['time'], y=df_ramf['ram_free'])])
    # fig_ramf.update_layout(title = "RAM FREE")

    df_fdisk = pd.read_sql_query("SELECT * FROM stats", db)
    fig_fdisk = go.Figure(data=[go.Scatter(x=df_fdisk['time'], y=df_fdisk['free_disk'])])
    fig_fdisk.update_layout(title = "Free disk space (Gio)")

    # df_udisk = pd.read_sql_query("SELECT * FROM stats", db)
    # fig_udisk = go.Figure(data=[go.Scatter(x=df_udisk['time'], y=df_udisk['used_disk'])])
    # fig_udisk.update_layout(title = "Disk used (Gio)")

    return fig_cpu,fig_batt,fig_ram,fig_fdisk


if __name__ == '__main__':
    app.run_server(debug=True)



