from flask import Flask, session, redirect, url_for, render_template,send_from_directory,make_response, request, abort
from functools import wraps
import lib.user as user
import re
import os
from uuid import uuid4

app = Flask("velib")
app.secret_key = b"ee18fcfbf6b7351ca99adb553a5a9d056538956ad9244fd622f4d93250ee3fce"


@app.get("/")
def accueil() :
    return """<h1>Accueil</h1>"""

@app.get("/carte")
def carte() :
    return render_template('index.html')

@app.route("/carte/<station>")
def carte_station(station) :
    #Faire un truc avec la station
    return f"""<h1>Carte + {station}</h1>"""

@app.get("/favoris")
def favoris() :
    #Requête(s) SQL pour aller chercher les favoris stockés en BDD
    return f"""<h1>Favoris</h1>"""

@app.get("/favoris/<station>")
def station_favorite() :
    #Get de la station selectionné pour lire le nombre de vélos
    return f"""<h1>Favoris</h1>"""

@app.post("/favoris/<Station>")
def ajout_station_favorite() :
    #Code pour ajouter un favoris à la BDD
    return f"""<h1>Ajout de Favoris</h1>"""


@app.put("/favoris/<Station>")
def modification_station_favorite() :
    #Modifier les informations d'une station
    return f"""<h1>Ajout de Favoris</h1>"""

@app.delete("/favoris/<Station>")
def suppression_station_favorite() :
    #Modifier les informations d'une station
    return f"""<h1>Ajout de Favoris</h1>"""


@app.post("/login")
def login_process() :    
    email = request.form["email"]
    password = request.form["password"] # j'attends la facon de crypter de paul pour ajuster
    current_user = ""

    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email) : # email valide ?
        current_user = user.login(email,password)
    else :
        return render_template("./auth/login.html.jinja", msg= "Email invalide 💀.")
    
    if not current_user :
        return render_template("./auth/login.html.jinja", msg= "Email ou mot de passe incorrect.")
    else :
        session['user'] = {
                        'nom' : current_user['lastname'],
                        "prenom" : current_user['firstname'],
                        "uuid" : current_user['uuid'],
                        "email" : current_user['email'],
                        }

        return redirect(url_for("accueil"))
    

@app.get("/login")
def login() :
    return render_template("./auth/login.html.jinja")

@app.get("/signup")
def inscription() :
    return render_template("./auth/signin.html.jinja")


@app.post("/signup")
def traitement_inscription() :
    #traiter les information d'inscription et ajouter les cookies
    return f"""<h1>Inscription</h1>"""

@app.route("/Logout")
def deconnexion() :
    #traiter les information d'inscription et ajouter les cookies
    return f"""<h1>deconnexion</h1>"""


@app.put("/user")
def modification_information() :
    #traiter les information d'inscription et ajouter les cookies
    return f"""<h1>modification information</h1>"""