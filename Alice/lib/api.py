import requests
import socket
api_host = socket.gethostname()
api_port = 8081
BOB_URL_SOURCE = f"http://{api_host}:{api_port}"



def get_all_stations() :
    r = requests.get(BOB_URL_SOURCE)
    data=r.json()
    return data["results"]

def get_one_station(stationcode) :
    r = requests.get(f"{BOB_URL_SOURCE}/{stationcode}")
    return r.json()