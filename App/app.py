import streamlit as st
import tensorflow as tf
import pandas as pd
import numpy as np

from tensorflow.keras.models import load_model


@st.cache_resource
def load_model():
    model = tf.keras.saving.load_model(
        'Models\\asl_model_1.tf', custom_objects=None, compile=False, safe_mode=True
    )
    return model

st.set_page_config(layout='wide')



st.header('ASL Trasnlator App')

tab1, tab2, tab3, tab4 = st.tabs(['Home', 'Dataset', 'Model', 'Translator'])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('About the App')
        st.write('''This app is a Sign Language to text translator app for people who dont know how to use sign language.
             I'm using the American Sign Language standards for this purpose as it is the most widely used sign language standard out there.''')
        st.markdown('**Techstack used for the app:**')
        st.markdown(' - Tensorflow')
        st.markdown(' - Pandas')
        st.markdown(' - Numpy')
        st.markdown(' - Matplotlib')
    
    with col2:
        st.image('App\\assets\\ASL_reference.png')