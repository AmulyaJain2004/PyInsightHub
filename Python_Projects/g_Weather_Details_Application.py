import requests
import os
from datetime import datetime, timedelta
import streamlit as st 
import pandas as pd
from dotenv import load_dotenv

api_key = os.getenv("API_KEY")
url = os.getenv("API_URL")

def getweather(city):
    result = requests.get(url.format(city,api_key))
    if result:
        api_data = result.json()
        country = api_data['sys']['country']
        temp_city = (api_data['main'](["temp"]))
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']["humidity"]
        wind_speed = api_data["wind"]["speed"]
        icon=api_data["weather"][0]["icon"]
        lon=api_data["coord"]["lon"]
        lat=api_data["coord"]["lat"]
        date_time =datetime.now().strftime("%d %b %Y | %I %M %S %p")
        res=[country, round(temp_city),weather_desc,hmdt,wind_speed,icon,lon,lat,date_time]
        return res,api_data
    else: 
        print("The place mentioned doesn't exist")

st.title("Weather Application")
col1,col2=st.columns(2)
with col1:
    place_name=st.text_input("Please enter your city")
    if place_name:
        res, api_data = getweather(place_name)
        st.map(pd.DataFrame({'lat':[res[7]], "lon":[res[6]]}))
with col2:
    if place_name:
        res,api_data=getweather(place_name)
        st.success("Date & Time: " + str(res[8]))
        st.success("Current Weather : "+str(res[1]))
        st.info("Deascription : "+str(res[2]))
        st.info("Humidity : "+str(res[3]))
        st.info("Wind Speed :"+ str(res[4]))
        web_str = "![Alt Text]"+"(openweathermap.org/img/wn/"+str(res[5])+"@2x.png)"
        st.markdown(web_str)
