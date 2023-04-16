import requests
##allows to send requests to websites
from pprint import pprint
##will allow json format from API to be used in a tree
import json

API_Key = '23ac97a391c8447a8ca58b2156'
#Documentation https://www.checkwxapi.com/documentation/


print("Get METAR & TAF weather data.")

city = input("Enter Airport Identifier ")

#base_url = "http://api.checkwx.com/metar/MYNN/?x-api-key=23ac97a391c8447a8ca58b2156"
base_url = "http://api.checkwx.com/metar/" + city + "?x-api-key=23ac97a391c8447a8ca58b2156"
base_url1 = "http://api.checkwx.com/taf/" + city + "?x-api-key=23ac97a391c8447a8ca58b2156"
base_url2 = "http://api.checkwx.com/taf/" + city + "radius/50/decoded?x-api-key=23ac97a391c8447a8ca58b2156"

weather_data = requests.get(base_url).json()
weather_data1 = requests.get(base_url1).json()
weather_data2 = requests.get(base_url2).json()

print("METAR", weather_data)
print("TAF", weather_data1)

want_nearest_wx = input("Do you want the nearest METAR & TAF weather data? ")
if want_nearest_wx == 'yes':
    print("Nearest", weather_data2)
