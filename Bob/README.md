# BOB

## ce README contient des informations sur l'utilisation du serveur bob

## Description
- ce serveur permet de stocker des requetes des stations velibs
- le serveur stock en memoire les donnees pendant 5 minutes 
- et fait une nouvelle requetes apres 5 minutes

## prerequis:
  - PYTHON >= 3.12

## utilisation
- preparer l'api
```python
  # prepare api
  import requests
  import socket
  api_host = socket.gethostname()
  api_port = 8081
  API_URL = f"http://{api_host}:{api_port}"
```
- requete

```python
  # vous faites des requetes sur api_host:port en utilisant flask
  # pour avoir toutes les stations il vous envoyer cette requete
  # pour le moment on recoit 100 stations sur 1400+
  from flask import request
  r = requests.get(API_URL, headers={"Content-Type":"application.json"})
  r = requests.get(f"{API_URL}/16107", headers={"Content-Type":"application/json"})
  res = r.json()
  # resultat attendu:
  # {"total_count": 992, "results": [

    # {"stationcode": "11104", "name": "Charonne - Robert et Sonia Delaunay", "is_installed": "OUI", "capacity": 20, "numdocksavailable": 9, "numbikesavailable": 9, "mechanical": 3, "ebike": 6, "is_renting": "OUI", "is_returning": "OUI", "duedate": "2024-04-28T06:33:55+00:00", "coordonnees_geo": {"lon": 2.3925706744194, "lat": 48.855907555969}, "nom_arrondissement_communes": "Paris", "code_insee_commune": null}

  # ]}
```

```python
  # pour recevoir une seule station il vous faut envoyer
  from flask import request
  r = requests.get(f"{API_URL}/{STATION_ID}", headers={"Content-Type":"application/json"})

  res = r.json()
  # resultat attendu
  # {"stationcode": "11104", "name": "Charonne - Robert et Sonia Delaunay", "is_installed": "OUI", "capacity": 20, "numdocksavailable": 9, "numbikesavailable": 9, "mechanical": 3, "ebike": 6, "is_renting": "OUI", "is_returning": "OUI", "duedate": "2024-04-28T06:33:55+00:00", "coordonnees_geo": {"lon": 2.3925706744194, "lat": 48.855907555969}, "nom_arrondissement_communes": "Paris", "code_insee_commune": null} -> station velib
  # OU
  # {} -> station vide
```



