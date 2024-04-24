from .requete import Requete
import json
import os
from lib.password import Password
stations=[]

def sign(datas):
  if is_existed_user(datas['email']) :
     return False
  else :
    req = Requete()
    req.insert("INSERT INTO user (uuid,first_name,last_name,email,password) VALUES (?, ?, ?, ?,?)", (datas['user_uuid'],datas['prenom'], datas['nom'], datas['email'],datas['motdepasse']))
    return True

def is_existed_user(email):
  req = Requete()
  resultat = req.select("SELECT * FROM user WHERE email = ?", (email))
  return len(resultat)>0

def login(email, password):
    req = Requete()
    resultat = req.select("SELECT * FROM user WHERE email = ?", (email))
    check_password = Password.check_password(email,password)
    if len(resultat) == 1 and check_password :
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