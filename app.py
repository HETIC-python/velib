from flask import Flask, render_template, request, redirect, url_for


app = Flask("velib")


@app.get("/")
def accueil() :
    return render_template('index.html.jinja')
    

@app.get("/carte")
def carte() :
     return render_template('carte.html.jinja')

@app.route("/carte/<station>")
def carte_station(station) :
    #Faire un truc avec la station
    return render_template('carte_station.html.jinja', station=station)

@app.get("/favoris")
def favoris() :
    #Requête(s) SQL pour aller chercher les favoris stockés en BDD
    user_stations = []  # Remplacer par la vraie requête pour récupérer les favoris
    return render_template('favoris.html.jinja', user_stations=user_stations)

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
    #traiter informations de connexion
    return f"""<h1>Traitement Connexion</h1>"""

@app.get("/login")
def login() :
    #Page de Connexion
    return render_template('login.html.jinja')

@app.get("/signup")
def inscription() :
    #s'inscrire à l'application
    return f"""<h1>Inscription</h1>"""

@app.post("/signup")
def traitement_inscription() :
    #traiter les information d'inscription et ajouter les cookies
     return render_template('signup.html.jinja')

@app.route("/Logout")
def deconnexion() :
    #traiter les information d'inscription et ajouter les cookies
    return f"""<h1>deconnexion</h1>"""


@app.put("/user")
def modification_information() :
    #traiter les information d'inscription et ajouter les cookies
    return f"""<h1>modification information</h1>"""