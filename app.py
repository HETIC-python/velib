from flask import Flask
app = Flask("velib")


@app.get("/")
def accueil() :
    return """<h1>Accueil</h1>"""

@app.get("/carte")
def carte() :
    return """<h1>Carte</h1>"""

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
    #traiter informations de connexion
    return f"""<h1>Traitement Connexion</h1>"""

@app.get("/login")
def login() :
    #Page de Connexion
    return f"""<h1>Se connecter</h1>"""

@app.get("/signup")
def inscription() :
    #s'inscrire à l'application
    return f"""<h1>Inscription</h1>"""

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