#!/usr/bin/env python3
# #Python program to find current 
# weather details of any city
# using openweathermap api
  
# import required modules
import requests, json, time

# Enter your API key here
# get your key from https://home.openweathermap.org/api_keys
api_key = "[YOUR API KEY]"
  
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name
city_name = "[YOUR CITY]"
  
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url)

# json method of response object 
# convert json format data into
# python format data
x = response.json()
if x["cod"] != "404":
  
    y = x["main"]
    #from kelvin to celcius
    current_temperature = int(round(y["temp"] - 273, 0))
    #uncomment line below to make it from kelvin to farenheit
    #current_temperature = int(round(1.8 * current_temperature + 32,0))
  
  
    z = x["weather"]
  
    
    weather_description = z[0]["description"]
if(weather_description == "few clouds"):
    icon = ""


print("["+str(current_temperature)+"°]")
  
   