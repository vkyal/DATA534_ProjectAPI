from City2Coord import getLongLat
from time import sleep
from tqdm import tqdm
import datetime
from datetime import date

def greeting():
    global currentSTR
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12 :
        currentSTR = "morning"
        print('Good morning!')
    elif 12 <= currentTime.hour < 18 :
        currentSTR = "afternoon"
        print('Good afternoon!')
    else:
        currentSTR = "evening"
        print('Good evening!')
    return currentSTR

def getLongLat():
    print("data scrapting to get longitude and latitude")

def getCity():  
    greeting()
    global city
    global long
    global forcastType
    global lat
    try:
        city = input("Please enter the name of the city to get weather forcast:") # Get City Name
        forcastType = input("Enter forcast type [Enter - 1 for Civil, 2 for Meteo, 3 for Astro]") # Get forcast type
    except Exception as ex:
        print("An exception occurred : ",ex)
    
    if (forcastType == 1) :
        forcastStr = "Civil Forcast"
    elif (forcastType == 2) :
        forcastStr = "Meteo Forcast"
    else :
        forcastStr = "Astro Forcast"
    
    print('City Name :',city,' Forcast Type:', forcastType, forcastStr)
    getLongLat()
    
    

    
    

    
