from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Sumo heya rikishi'),
    dcc.Graph(id="graph"),
    dcc.Checklist(
        id="checklist",
        options=["Dewanoumi", "Nishonoseki", "Tatsunami","Tokitsukaze","Takasago"],
        value=["Dewanoumi"],
        inline=True
    ),
])


@app.callback(
    Output("graph", "figure"), 
    Input("checklist", "value"))
def update_line_chart(ichimon):
    df = px.read_csv('https://raw.githubusercontent.com/andre1670/Sumo-heya-rikishi/main/active.csv')
    mask = df.ichimon.isin(ichimon)
    fig = px.line(df[mask], 
        x="year", y="rikishi", color='heya')
    return fig


app.run_server(debug=True)