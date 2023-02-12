# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 22:46:36 2023

@author: jagar
"""

import streamlit as st
import pickle
import pandas as pd


xgb = pickle.load(open("food.pkl","rb"))

lat = st.number_input("enter the lat of restaurant")
lan=st.number_input("enter the lan of restaurant")
lat1=st.number_input("enter the lat of delivery location ")
lan1=st.number_input("enter the lan of the delivery location")

df=pd.DataFrame(data=[[lat,lan],[lat1,lan1]],columns=["latitude","longitude"])
st.map(df)

Type_of_vehicle_motorcycle = st.number_input("enter ur vehicle (if scooter enter 1 if others enter 0)")
distance = st.number_input("enter the distance")
Delivery_person_Ratings= st.number_input("what is the previous rating of the delivery man")
Delivery_person_Age= st.number_input("what is the age of the delivery man")


prediction = xgb.predict([[Delivery_person_Age,Delivery_person_Ratings,Type_of_vehicle_motorcycle ,distance]])

st.header(prediction)
