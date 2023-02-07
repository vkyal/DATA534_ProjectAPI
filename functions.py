import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
from unidecode import unidecode
import math

#Global attributes
wiki_url = "https://en.wikipedia.org/wiki/"
api_url = "http://www.7timer.info/doc.php?lang=en#web_interface"
    
def coordinates(city):

    try:

        city = requests.get(wiki_url+city)

        city = BeautifulSoup(city.text)

        for item in city.find_all("span", {"class":"geo"}):
            try:
                temp = item.text
                break
            except:
                print(f"Oops! Unable to find the mentioned {city} co-ordinates!")

        flag = temp.split(";")
        
        return flag
        
    except:
        return "City doesn't exist!"

def documentation_cloud_cover(dataframe):

    #api_url = "http://www.7timer.info/doc.php?lang=en#web_interface"

    weather = requests.get(api_url)

    weather_out = BeautifulSoup(weather.text)

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
    
def documentation_ppt_amt(dataframe):

    #url = "http://www.7timer.info/doc.php?lang=en#web_interface"

    weather = requests.get(api_url)

    weather_out = BeautifulSoup(weather.text)

    tables = weather_out.find_all("table")
    
    prcpt_amt = []
    row = []

    for i,entry in enumerate(tables[5].find_all("td")):
        try:
            if i >= 67 and i <= 86:
                row.append(entry.text)
                if i%2 == 0:
                    prcpt_amt.append(row)
                    row = []
        except:
            print("Server Error")
            

    df1 = pd.DataFrame(prcpt_amt, columns = ['prec_amount', 'Ppt_Meaning'])
    df1.replace(to_replace = '\r\n\t', regex=True, value='', inplace=True)
    df1["prec_amount"]=df1["prec_amount"].astype(int)
    temp = pd.merge(dataframe,df1,on="prec_amount",how="left")

    
    return temp

def documentation_wind_spd_10m(dataframe):

    #url = "http://www.7timer.info/doc.php?lang=en#web_interface"

    weather = requests.get(api_url)

    weather_out = BeautifulSoup(weather.text)

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
def documentation_weather_type(dataframe):

    #url = "http://www.7timer.info/doc.php?lang=en#web_interface"

    weather = requests.get(api_url)

    weather_out = BeautifulSoup(weather.text)

    tables = weather_out.find_all("table")
    
    weather_type = []
    row = []

    for i,entry in enumerate(tables[5].find_all("td")):
        try:
            if i >= 88 and i <= 111:
                row.append(entry.text)
                if (i+1)%2 == 0:
                    weather_type.append(row)
                    row = []
        except:
            print("Server Error")

    df3 = pd.DataFrame(weather_type, columns = ['weather', 'Weather_Meaning'])
    df3.replace(to_replace = '\r\n\t', regex=True, value='', inplace=True)

    s = df3['weather'].str.split(',').apply(pd.Series, 1).stack()
    s.index = s.index.droplevel(-1)
    s.name = 'weather'

    del df3['weather']
    
    df3 = df3.join(s)
    df3.reset_index(inplace=True)
    df3 = df3.drop('index', axis=1)
    df3["weather"]=df3["weather"].astype(str)
    df3["weather"] = df3["weather"].str.strip()
    
    temp = pd.merge(dataframe,df3,on="weather",how="left")
    
    return temp

def wiki_timezone(city):  
    
    #url ="https://en.wikipedia.org/wiki/{city}".format(city=city)
    city = requests.get(wiki_url+city)

    city = BeautifulSoup(city.text)

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
