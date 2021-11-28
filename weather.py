import serial
from gtts import gTTS
import subprocess
from datetime import date, datetime
import requests, json



# Enter your API key here
api_key = "a4bdd4b3b747843ede0c9f2fd5a5c3f5" 
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# Give city name

#city_name = input("Enter city name : ")
city_name = "Morrisville"

# http://api.openweathermap.org/data/2.5/weather?appid=a4bdd4b3b747843ede0c9f2fd5a5c3f5&q=morrisville



# complete_url variable to store
# complete url address
#  base_url + "appid=" + api_key + "&q=" + city_name

complete_url = "http://api.openweathermap.org/data/2.5/weather?appid=a4bdd4b3b747843ede0c9f2fd5a5c3f5&q=">
 
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
        today = date.today()
        today = today.strftime("%B %d, %Y")
        now = datetime.now()
        now = now.strftime("%H:%M")
        greet = "Good Morning Honey. Hope you had a good sleep. Today is " + today + "."
        say_time = "It is " + now + "now."
        #configure the serial connection
        ser = serial.Serial(port='/dev/serial0',baudrate=19200)
        if ser.isOpen():
                ser.write(str.encode(chr(12))) # 12 is clear and reset cursor
                ser.write(str.encode("City : " + city_name))
                ser.write(str.encode(chr(13))) # 13 Starts a new line
                temp = round((current_temperature-273.15)*1.8 + 32, 2)
                ser.write(str.encode("Temp : " + str(temp) + "F"))
                ser.write(str.encode(chr(13))) # 13 Starts a new line
                ser.write(str.encode("P/H : " + str(current_pressure) +" & "+ str(current_humidity)))
                ser.write(str.encode(chr(13))) # 13 Starts a new line
                ser.write(str.encode(str(weather_description)))

else:
        exit()


myText = greet + say_time + ". There is " + str(weather_description) + "in" + city_name + " area. The Tem>
language = 'en'
output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")
subprocess.run(['mpg321', r'output.mp3'])

      
