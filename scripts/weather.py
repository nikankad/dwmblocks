#!/usr/bin/env python3
# #Python program to find current 
# weather details of any city
# using openweathermap api
  
# import required modules
import requests, json, time

# Enter your API key here
api_key = "YOUR API"
  
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name
city_name = "YOUR CITY"
  
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  
# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object 
# convert json format data into
# python format data
x = response.json()
# print(x)  
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
  
    # store the value of "main"
    # key in variable y
    y = x["main"]
  
    # store the value corresponding
    # to the "temp" key of y
    current_temperature = int(round(y["temp"] - 273, 0))


if(current_temperature < 30):
    current_temperature = "^c#C678DD^["+str(current_temperature)+"°]"
else: 
    current_temperature = "^c#E06C75^["+str(current_temperature)+"°]"


print(current_temperature)