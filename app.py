import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")

animal = st.radio("What animal is your favorite?", ("Lions", "Tigers", "Bears"))
 
