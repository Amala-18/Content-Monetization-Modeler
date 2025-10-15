import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge, Lasso
import pickle

#Streamlit part
with open("C://Users//Sri Advikam//Desktop//Amala//Content Monetization Modeler//final_model.pkl","rb")as f:
     best_model = pickle.load(f)

st.sidebar.title('Select')
selection = st.sidebar.radio( 'Select',['Home', 'Find'])
if selection == 'Home':
     st.title('▶️YouTube Monetization Modeler')
     st.write("""
     Welcome to the **YouTube Monetization Dashboard**!  

     This app uses a dataset of YouTube videos containing details like:
    - 🎥 **Views** -  Number of people watched this video  
    - 👍 **Likes** -  Audience interest  
    - 💬 **Comments** - Interaction level  
    - ⏱️ **Watch Time**- Time taken for viewers stayed in the video  
     

    Using this dataset, we trained a machine learning model to **predict potential monetization (revenue)** 
    based on engagement metrics.  
    """)

elif selection == 'Find':
    st.title('PREDICT AD REVENUE')

      
   # Create two columns
    column1, column2 = st.columns(2)	
    
  
    with column1:  
     views=st.number_input("views",min_value=0, value=10000)
     likes=st.number_input("likes", min_value=0, value=1000)
     comments=st.number_input("comments",min_value=0, value=200)
     watch_time_minutes=st.number_input("watch_time_minutes",min_value=0, value=50000)
     video_length_minutes=st.number_input("video_length_minutes", min_value=0, value=10)
     subscribers=st.number_input("subscribers",min_value=0, value=10000)

    
    with column2:
     category=st.selectbox("category",['Entertainment', 'Gaming', 'Education', 'Music', 'Tech', 'Lifestyle'])
     device=st.selectbox("device",['TV', 'Tablet', 'Mobile', 'Desktop'])
     country=st.selectbox("country",['IN', 'CA', 'UK', 'US', 'DE', 'AU'])
     st.button("Predict Ad Revenue")
   
    
  
# Predict
    input_df = pd.DataFrame([{
        "views": views,
        "likes": likes,
        "comments": comments,
        "watch_time_minutes": watch_time_minutes,
        "video_length_minutes":video_length_minutes,
        "subscribers":subscribers,
        "category": category,
        "device": device,
        "country":country
     }])
   

    prediction = best_model.predict(input_df)
    predicted_value = max(0, float(prediction[0]))  # clip at 0
    st.success(f"💰 Predicted Ad Revenue: ${predicted_value:.2f}")
 
         
