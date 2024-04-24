import socket
import requests
import json
from datetime import datetime

API_URL='https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records?timezone=Europe%2FParis&refine=nom_arrondissement_communes%3A%22Paris%22'

# Init
srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_host = socket.gethostname()
srv_port = 8080
srv_socket.bind((srv_host, srv_port))
srv_socket.listen(5)
temp_data = {}
# Boucle infinie
while True:
    try:
        # Attente de connexion
        print(f"Waiting for new connection on port {srv_port}")
        client, adresse = srv_socket.accept()
        print(f"Connexion entrante de {adresse}")
        if temp_data.get("last_used"):
            print("using old data")
            data=temp_data.get("data")
            client.send(f"""HTTP/1.1 200 OK\nContent-Type: application/json\n\n{data}""".encode())
        else:
            print("fetching new data")
            temp_data["last_used"] = datetime.now()
            r = requests.get(API_URL)
            temp_data["data"] = json.dumps(r.json())
            data=temp_data.get("data")
            client.send(f"""HTTP/1.1 200 OK\nContent-Type: application/json\n\n{data}""".encode())
        requete = client.recv(10000)
        requete = requete.decode()

        client.close()
    except Exception as err:
        print(err)
        break

srv_socket.close()