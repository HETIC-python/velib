import requests
import json

BOB_URL_SOURCE = "http://127.0.0.1:8081/"



def get_all_stations() :
    r = requests.get(BOB_URL_SOURCE)
    data=r.json()
    return data["results"]

def get_one_station(stationcode) :
    r = requests.get(f"{BOB_URL_SOURCE}{stationcode}")
    return r.json()