import requests
#allows to send requests to websites

from pprint import pprint
#will allow json format from API to be used in a tree

import json

API_Key = '23ac97a391c8447a8ca58b2156'
#Documentation https://www.checkwxapi.com/documentation/

repeat_wx_code = 10 #repeats code 10 times
while repeat_wx_code > 0:
    print("Get METAR & TAF weather data.")

    city = input("Enter Airport Identifier ")

    #base_url = "http://api.checkwx.com/metar/MYNN/?x-api-key=23ac97a391c8447a8ca58b2156" base url template
    base_url = "http://api.checkwx.com/metar/" + city + "?x-api-key=23ac97a391c8447a8ca58b2156"
    base_url1 = "http://api.checkwx.com/taf/" + city + "?x-api-key=23ac97a391c8447a8ca58b2156"
    base_url2 = "http://api.checkwx.com/metar/" + city + "/radius/100/?x-api-key=23ac97a391c8447a8ca58b2156"
    base_url3 = "http://api.checkwx.com/taf/" + city + "/radius/100/?x-api-key=23ac97a391c8447a8ca58b2156"

    weather_data = requests.get(base_url).json()
    weather_data1 = requests.get(base_url1).json()
    weather_data2 = requests.request("GET", base_url2)
    weather_data3 = requests.request("GET", base_url3)
    #response = requests.request("GET", base_url2) from code example on website docs for nearest metar & taf within radius

    print("METAR", weather_data)
    print("TAF", weather_data1)

    want_nearest_wx = input("Do you want the nearest METAR & TAF weather data? ")
    if want_nearest_wx == 'yes':
        print(weather_data2.text)
        print(weather_data3.text)
        #print(response.text) from code example on website docs to retrieve decoded text for nearest in radius
    else: 
        break
    
    want_more_wx = input("Would you like more weather? ")
    if want_more_wx == 'yes':
        repeat_wx_code -= 1 #decreases while loop count by 1
    else:
        print("Fly safe!")
        break
