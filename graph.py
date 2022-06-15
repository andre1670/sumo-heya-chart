import plotly.express as px

df = px.read_csv('https://raw.githubusercontent.com/andre1670/Sumo-heya-rikishi/main/active.csv')
fig = px.line(df, x='Basho', y='Rikishi', title='Dewanoumi')
fig.show()
