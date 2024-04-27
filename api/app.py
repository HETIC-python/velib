import socket
import requests
import json
from datetime import datetime

API_URL="https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?limit=50"
# https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?timezone=Europe%2FParis&refine=nom_arrondissement_communes%3A%22Paris%22' <==== Pour le prof ne retourne que 10 stations

# Init
srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_host = socket.gethostname()
srv_port = 8081
srv_socket.bind((srv_host, srv_port))
srv_socket.listen(5)
temp_data = {}
# Boucle infinie


def fetch_data():
    print("fetching data")
    temp_data["last_used"] = datetime.now()
    r = requests.get(API_URL)
    temp_data["data"] = json.dumps(r.json())
    data=temp_data.get("data")
    print(data)
    print("\n\n\n\n")

def find_station_by_id(id, data):
    for d in data:
        if d.get("stationcode") == id:
            return d
    return {}

while True:
    try:
        # Attente de connexion
        print(f"Waiting for new connection on port {srv_port}")
        client, adresse = srv_socket.accept()
        print(f"Connexion entrante de {adresse}")
        requete = client.recv(1000000)
        requete = requete.decode()
        method, url, http_v = requete.splitlines()[0].split(" ")
        ## nethod to handle fetch logic
        try:
            if temp_data.get("last_used"):
                print("trying old data")
                new_date = datetime.now()
                last_used = temp_data.get("last_used", new_date)
                diff = int((new_date - last_used).total_seconds())
                print("="*10, diff)
                if diff >= 300:
                    fetch_data()
            else:  
                fetch_data()

            if url == "/":
                if temp_data.get("last_used"):
                    data=temp_data.get("data")
                    client.send(f"""HTTP/1.1 200 OK\nContent-Type: application/json\n\n{data}""".encode())
            elif url != "/favicon.ico":
                print(method, url)
                id = url[1:]
                data = temp_data.get("data", "")
                if data == "":
                    client.send(f"""HTTP/1.1 200 OK\nContent-Type: application/json\n\n{json.dumps({})}""".encode())
                else:
                    data = json.loads(temp_data.get("data", ""))
                    data = find_station_by_id(id, data.get("results", []))
                    data = json.dumps(data)
                    client.send(f"""HTTP/1.1 200 OK\nContent-Type: application/json\n\n{data}""".encode())
        except Exception as e:
            print("inner exception: ", e)
            
        

        client.close()
    except Exception as err:
        print(err)
        break

srv_socket.close()
"""GET / HTTP/1.1
Host: 192.168.1.235:8080"""