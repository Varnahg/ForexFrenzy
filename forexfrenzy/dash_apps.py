import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from django_plotly_dash import DjangoDash


from forexfrenzy.models import Rates

app = DjangoDash('SimpleDashboard')  # Create a Dash app in Django

def fetch_data():
    # Fetch data from SQLite
    queryset = Rates.objects.all()
    currencies = [1,2,3,4,5]
    data = {'Currency': currencies, 'Value': ['a','a','a','a','a']}
    return pd.DataFrame(data)

app.layout = [
    html.Div(children="just name"),
    dash_table.DataTable(data=fetch_data()),
    dcc.Graph(figure=px.histogram(fetch_data(), x='Currency', y='Value')),
    dcc.Interval(id='interval', interval=5000, n_intervals=0)  # Auto-update every 5 seconds
]

@app.callback(
    Output('currency-graph', 'figure'),
    [Input('interval', 'n_intervals')]
)
def update_graph(n_intervals):
    df = fetch_data()
    fig = {
        'data': [
            {'x': df['Currency'], 'y': df['Value']},]
        # ],
        # 'layout': {
        #     'title': 'Currency Values',
        #     'xaxis': {'title': 'Currency'},
        #     'yaxis': {'title': 'Value'},
        # }
    }
    print(type(fig))
    return fig