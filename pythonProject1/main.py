import requests  #we can import information through various networks
import json
import os
city = input("enter the name of the city:")
url = f"http://api.weatherapi.com/v1/current.json?key=adc4bae0d1b84fe5a2c90537242206&q={city}"
r = requests.get(url)
print(r.text)
weatherdic = json.loads(r.text) #using json module to convert the string data type to dictionary
temp = f"the temprature of {city} is: {(weatherdic["current"]["temp_c"])}"
print(temp)
os.system(f"say {temp} degree celsius")