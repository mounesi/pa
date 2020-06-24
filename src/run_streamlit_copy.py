#import
import pandas as pd
import plotly.express as px


# reading data
df = pd.read_csv('../data_pub/data.csv', index_col=0)
df.head()


# process data
df['PCI'] = ['good' if (x >= 7) else 'fine' if (x >= 5 and x <7) else 'bad' for x in df['Pavement Rate Total']]
df['maintenance level'] = ['routine maintenance' if (x >= 7) else 'rehabilitation' if (x >= 5 and x <7) else 'reconstruction' for x in df['Pavement Rate Total']]

df.head()

#
fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", color="machine_vision_prediction", size="AVERAGE WIDTH (FT)"
                        ,hover_name="ROAD NAME",hover_data=["machine_vision_prediction", "Pavement Rate Total", "PCI", "maintenance level"],color_discrete_sequence=["fuchsia"], zoom=12
                          )
#, hover_name="ROAD NAME", hover_data=["machine_vision_prediction", "Pavement Rate Total"],
#                        color_discrete_sequence=["fuchsia"], zoom=12, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
#fig.show()

import streamlit as st
st.plotly_chart(fig)
