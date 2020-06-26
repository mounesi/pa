import streamlit as st
from fig_generator import fig 


st.title("Pavement Assessment in Irvington Village in New York State")
st.markdown(
"""
This is a demo of a Streamlit app that shows the Roadway Condition
geographical distribution of Irvington Village in NYS.

[See source code](https://github.com/mounesi/pa)
""")

st.plotly_chart(fig)