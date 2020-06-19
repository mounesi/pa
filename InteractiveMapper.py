import pandas as pd
import plotly.express as px


df = pd.read_csv('data.csv', index_col=0)
df.head()

fig = px.scatter_mapbox(df, 
            lat="Latitude", lon="Longitude", color="machine_vision_prediction", size="AVERAGE WIDTH (FT)"
            ,hover_name="ROAD NAME",hover_data=["machine_vision_prediction", "Pavement Rate Total"                        ,"PCI"],color_discrete_sequence=["fuchsia"], zoom=12 )
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
