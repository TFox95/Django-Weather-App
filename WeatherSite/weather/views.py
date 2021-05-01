from django.shortcuts import render
import pandas as pd
import requests
# Create your views here.

#def  index(request):
#    """This function only renders the html file it's calling"""
#    return render(request, "weather/index.html")

#def index(request):
#    """
#    This function will allow you to use pandas to capture the
#    lat and lon data of the cities and have it printed out of the
#    csv file and output the data so we can see it
#    """
#    df = pd.read_csv("worldcities.csv")
#    city = "Kyoto"
#    lat = df[df["city_ascii"] == city]["lat"]
#    print(city)
#    print(lon)
#    return render(request, "weather/index.html")

def index(request):
    #1st we need to set the file to be deciphered with pandas and assigned to a variable
    df = pd.read_csv("worldcities.csv")
    #next we are going to assign a city
    city = "Chicago"
    #now we need to set the latitude variable that's decoded from the above csv file
    lat = df[df["city_ascii"] == city]["lat"]
    #now we need to set the longatude values
    lon = df[df["city_ascii"] == city]["lng"]
    #now we need to call the rapidapi realtime weather api url
    url = "https://climacell-microweather-v1.p.rapidapi.com/weather/realtime"
    #now we need to set the fields of what we will need to query the api for
    querystring = {"unit_system":"si",
    "fields": ["precipitation", "precipitation_type",
    "temp", "cloud_cover", "wind_speed", "weather_code"],
    "lat": lat, "lon": lon}
    #now we need to get the rapid api key and save it
    headers = {"x-rapidapi-key": "a1ca7cac7bmsh7481cbdd1b05541p170fb7jsnfb74af885ed7"}
    response = requests.request("GET", url, headers= headers, params= querystring).json()
    print (response)
    return render(request, "weather/index.html")
