from .requete import Requete
import lib.api as api 
from flask import session
def lister_favoris(user_uuid):

  req = Requete()
  res = req.select("SELECT * FROM favoris WHERE user_uuid = ? ORDER BY created_at DESC", user_uuid)
  return res

def new_favoris(user_uuid, station_code, uuid,image_name=''):
  
  station =  api.get_one_station(station_code)
  req = Requete()
  req.insert("INSERT INTO favoris (uuid,station_name,user_uuid,picture_name,stationcode,longitude,latitude,numbikesavailable) VALUES (?, ?, ?, ?,?,?,?,?)", (uuid,station['name'], user_uuid, image_name,station_code,station['coordonnees_geo']['lon'],station['coordonnees_geo']['lat'],station['numbikesavailable']))

def is_existed_favoris(station_code):
  req = Requete()
  resultat = req.select("SELECT * FROM favoris WHERE stationcode = ? AND user_uuid = ?", (station_code, session['user']['uuid']))
  return len(resultat)>0


def delete_favoris(uuid_fav):
  req = Requete()
  req.insert("DELETE FROM favoris WHERE uuid = ?", uuid_fav)

def get_favoris (uuid) :
    req = Requete()
    resultat = req.select("SELECT * FROM favoris WHERE uuid = ?", uuid)

    return resultat

def update_favoris (uuid, image_name) :
    req = Requete()
    return req.update("UPDATE favoris SET picture_name= ? WHERE uuid = ?", (image_name,uuid))