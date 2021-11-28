# -*- coding: utf-8 -*-

# Python program to find current
# weather details of any city
# using openweathermap api
 
# import required modules
import requests, json
 
# Enter your API key here
api_key = "a4bdd4b3b747843ede0c9f2fd5a5c3f5"
 
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# Give city name
#city_name = input("Enter city name : ")
 


# http://api.openweathermap.org/data/2.5/weather?appid=a4bdd4b3b747843ede0c9f2fd5a5c3f5&q=morrisville



# complete_url variable to store
# complete url address
#  base_url + "appid=" + api_key + "&q=" + city_name

complete_url = "http://api.openweathermap.org/data/2.5/weather?appid=a4bdd4b3b747843ede0c9f2fd5a5c3f5&q=morrisville"
 
# get method of requests module
# return response object
response = requests.get(complete_url)
 
# json method of response object
# convert json format data into
# python format data
x = response.json()
 
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
    current_temperature = y["temp"]
 
    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]
 
    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]
 
    # store the value of "weather"
    # key in variable z
    z = x["weather"]
 
    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]
 
    # print following values
    print(" Temp : " +
                    str(current_temperature) +
          "\n Atm Press : " +
                    str(current_pressure) +
          "\n Humidity : " +
                    str(current_humidity) +
          "\n Description : " +
                    str(weather_description))
 
else:
    print(" City Not Found ")