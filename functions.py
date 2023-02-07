import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
from unidecode import unidecode
import math

#Global attributes
wiki_url = "https://en.wikipedia.org/wiki/"
api_url = "http://www.7timer.info/doc.php?lang=en#web_interface"
    


def documentation_cloud_cover(dataframe):

    #api_url = "http://www.7timer.info/doc.php?lang=en#web_interface"

    weather = requests.get(api_url)

    weather_out = BeautifulSoup(weather.text, features="lxml")

    tables = weather_out.find_all("table")
    
    row= []
    cloud = []

    for i,entry in enumerate(tables[5].find_all("td")):
        try:
            if i >= 4 and i <= 21:
                row.append(entry.text)
                if (i+1)%2 == 0:
                    cloud.append(row)
                    row = []
        except:
            print("Server Error")

    df = pd.DataFrame(cloud, columns = ['cloudcover', 'Cloudcover_Meaning'])
    df.replace(to_replace = '\r\n\t', regex=True, value='', inplace=True)
    df["cloudcover"]=df["cloudcover"].astype(int)
    temp = pd.merge(dataframe,df,on="cloudcover",how="left")
    
    return temp
    


def documentation_wind_spd_10m(dataframe):

    #url = "http://www.7timer.info/doc.php?lang=en#web_interface"

    weather = requests.get(api_url)

    weather_out = BeautifulSoup(weather.text, features="lxml")

    tables = weather_out.find_all("table")
    
    wind_spd_10m = []
    row = []

    for i,entry in enumerate(tables[5].find_all("td")):
        try:
            if i >= 48 and i <= 63:
                row.append(entry.text)
                if (i+1)%2 == 0:
                    wind_spd_10m.append(row)
                    row = []
        except:
            print("Server Error")

    df2 = pd.DataFrame(wind_spd_10m, columns = ['speed', 'Speed_Meaning'])
    df2.replace(to_replace = '\r\n\t', regex=True, value='', inplace=True)
    
    df2["speed"]=df2["speed"].astype(int)
    temp = pd.merge(dataframe,df2,on="speed",how="left")

    
    return temp
    
    
    df3 = df3.join(s)


def wiki_timezone(city):  
    
    #url ="https://en.wikipedia.org/wiki/{city}".format(city=city)
    city = requests.get(wiki_url+city)

    city = BeautifulSoup(city.text, features="lxml")

    rt =""
    for item in city.find_all("tr"):
        try:
            if "Time zone" in item.text:
                for entry in item.find_all("td"):
                    rt+=(entry.text)
        except:
            print("Server Error")

    try:
        rt = rt[3:9]
        rt = rt.replace(":",".")
        ascii_string = unidecode(rt)
        time_zone = float(ascii_string)
        time_zone = math.ceil(time_zone)
        return(time_zone)
    except:
        pass