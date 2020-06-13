

import pandas as pd
df = pd.read_csv('data.csv', index_col=0)
df.head()


import plotly.express as px

fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color="machine_vision_prediction", size="AVERAGE WIDTH (FT)"
                        ,hover_name="ROAD NAME",hover_data=["machine_vision_prediction", "Pavement Rate Total", "PCI"],color_discrete_sequence=["fuchsia"], zoom=12
                          )
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False) 
