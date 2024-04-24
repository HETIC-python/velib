from .requete import Requete
import json
import os
stations=[]

def sign(datas):
  req = Requete()
  req.insert("INSERT INTO user (uuid,firstname,lastname,email,password) VALUES (?, ?, ?, ?,?)", (datas['uuid'],datas['firstname'], datas['lastname'], datas['email'],datas['password']))


def login(email, password):
    req = Requete()
    resultat = req.select("SELECT * FROM user WHERE email = ? AND password = ?", (email,password))

    if len(resultat) == 1 :
       return resultat[0]
    else :
       return False

def delete_account(uuid):
  req = Requete()
  req.insert("DELETE FROM user WHERE uuid = ?", uuid)

def get_account_infos (uuid) :
    req = Requete()
    resultat = req.select("SELECT * FROM user WHERE uuid = ?", uuid)

    return resultat

# def update_account (datas) :
#     req = Requete()
#     return req.update("UPDATE favoris SET picture_name= ? WHERE uuid = ?", (datas['firstname'],datas['lastname']))