# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 22:46:36 2023

@author: jagar
"""

import streamlit as st
import pickle
import pandas as pd


final_model = pickle.load(open("food.pkl","rb"))

vehicle = st.number_input("enter ur vehicle (if scooter enter 1 if others enter 0)")
distance = st.number_input("enter the distance")
ratings= st.number_input("what is the previous rating of the delivery man")
age = st.number_input("what is the age of the delivery man")


prediction = final_model.predict([[age,ratings,vehicle,distance]])[0]

st.header(prediction)