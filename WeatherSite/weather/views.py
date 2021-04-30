from django.shortcuts import render
import pandas as pd
# Create your views here.

#def  index(request):
#    """This function only renders the html file it's calling"""
#    return render(request, "weather/index.html")

def index(request):
    """
    This function will allow you to use pandas to capture the
    lat and lon data of the cities and have it printed out of the
    csv file and output the data so we can see it
    """
    df = pd.read_csv("worldcities.csv")
    city = "Kyoto"
    lat = df[df["city_ascii"] == city]["lat"]
    lon = df[df["city_ascii"] == city]["lng"]
    print(lat)
    print(city)
    print(lon)
    return render(request, "weather/index.html")
