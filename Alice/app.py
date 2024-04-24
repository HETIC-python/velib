from flask import Flask, session, redirect, url_for, render_template,send_from_directory,make_response, request, abort
from functools import wraps
import lib.user as user
import lib.favorite as fav
from lib.password import Password  
import re
import os
from uuid import uuid4

app = Flask("velib")
app.secret_key = b"ee18fcfbf6b7351ca99adb553a5a9d056538956ad9244fd622f4d93250ee3fce"

# list de stations faite suivant les normes d'opendatas en attendant que Bob soit opérationnel
stations=[
{
"stationcode":"31104",
"name":"Mairie de Rosny-sous-Bois",
"is_installed":"OUI",
"capacity":30,
"numdocksavailable":10,
"numbikesavailable":17,
"mechanical":1,
"ebike":16,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:23:05+00:00",
"coordonnees_geo":{
"lon":2.4865807592869,
"lat":48.871256519012
},
"nom_arrondissement_communes":"Rosny-sous-Bois",
"code_insee_commune":None
},
{
"stationcode":"44015",
"name":"Rouget de L'isle - Watteau",
"is_installed":"OUI",
"capacity":20,
"numdocksavailable":15,
"numbikesavailable":5,
"mechanical":4,
"ebike":1,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:23:27+00:00",
"coordonnees_geo":{
"lon":2.3963020229163,
"lat":48.778192750803
},
"nom_arrondissement_communes":"Vitry-sur-Seine",
"code_insee_commune":None
},
{
"stationcode":"12109",
"name":"Mairie du 12ème",
"is_installed":"OUI",
"capacity":30,
"numdocksavailable":15,
"numbikesavailable":14,
"mechanical":14,
"ebike":0,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:19:58+00:00",
"coordonnees_geo":{
"lon":2.3875549435616,
"lat":48.840855311763
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"14111",
"name":"Cassini - Denfert-Rochereau",
"is_installed":"OUI",
"capacity":25,
"numdocksavailable":25,
"numbikesavailable":0,
"mechanical":0,
"ebike":0,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:17:12+00:00",
"coordonnees_geo":{
"lon":2.3360354080796,
"lat":48.837525839067
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"32017",
"name":"Basilique",
"is_installed":"OUI",
"capacity":22,
"numdocksavailable":6,
"numbikesavailable":14,
"mechanical":9,
"ebike":5,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:21:14+00:00",
"coordonnees_geo":{
"lon":2.3588666820200914,
"lat":48.93626891059109
},
"nom_arrondissement_communes":"Saint-Denis",
"code_insee_commune":None
},
{
"stationcode":"11104",
"name":"Charonne - Robert et Sonia Delaunay",
"is_installed":"OUI",
"capacity":20,
"numdocksavailable":19,
"numbikesavailable":1,
"mechanical":0,
"ebike":1,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:22:56+00:00",
"coordonnees_geo":{
"lon":2.3925706744194,
"lat":48.855907555969
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"8026",
"name":"Messine - Place Du Pérou",
"is_installed":"OUI",
"capacity":12,
"numdocksavailable":5,
"numbikesavailable":5,
"mechanical":4,
"ebike":1,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:22:39+00:00",
"coordonnees_geo":{
"lon":2.315508019010038,
"lat":48.875448033960744
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"13007",
"name":"Le Brun - Gobelins",
"is_installed":"OUI",
"capacity":48,
"numdocksavailable":44,
"numbikesavailable":3,
"mechanical":2,
"ebike":1,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:21:20+00:00",
"coordonnees_geo":{
"lon":2.3534681351338,
"lat":48.835092787824
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"7002",
"name":"Vaneau - Sèvres",
"is_installed":"OUI",
"capacity":35,
"numdocksavailable":24,
"numbikesavailable":11,
"mechanical":11,
"ebike":0,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:22:20+00:00",
"coordonnees_geo":{
"lon":2.3204218259346,
"lat":48.848563233059
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"5110",
"name":"Lacépède - Monge",
"is_installed":"OUI",
"capacity":23,
"numdocksavailable":20,
"numbikesavailable":3,
"mechanical":2,
"ebike":1,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:18:44+00:00",
"coordonnees_geo":{
"lon":2.3519663885235786,
"lat":48.84389286531899
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"6108",
"name":"Saint-Romain - Cherche-Midi",
"is_installed":"OUI",
"capacity":17,
"numdocksavailable":9,
"numbikesavailable":8,
"mechanical":7,
"ebike":1,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:20:49+00:00",
"coordonnees_geo":{
"lon":2.321374788880348,
"lat":48.84708159081946
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"41301",
"name":"Bois de Vincennes - Gare",
"is_installed":"OUI",
"capacity":50,
"numdocksavailable":29,
"numbikesavailable":21,
"mechanical":20,
"ebike":1,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:23:01+00:00",
"coordonnees_geo":{
"lon":2.4708339950830287,
"lat":48.836022242886884
},
"nom_arrondissement_communes":"Nogent-sur-Marne",
"code_insee_commune":None
},
{
"stationcode":"6021",
"name":"Beaux-Arts - Bonaparte",
"is_installed":"OUI",
"capacity":20,
"numdocksavailable":4,
"numbikesavailable":13,
"mechanical":11,
"ebike":2,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:23:19+00:00",
"coordonnees_geo":{
"lon":2.334851883351803,
"lat":48.856451985395786
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"25006",
"name":"Place Nelson Mandela",
"is_installed":"OUI",
"capacity":22,
"numdocksavailable":19,
"numbikesavailable":3,
"mechanical":0,
"ebike":3,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:23:32+00:00",
"coordonnees_geo":{
"lon":2.1961666225454,
"lat":48.862453313908
},
"nom_arrondissement_communes":"Rueil-Malmaison",
"code_insee_commune":None
},
{
"stationcode":"30002",
"name":"Jean Rostand - Paul Vaillant Couturier",
"is_installed":"OUI",
"capacity":40,
"numdocksavailable":15,
"numbikesavailable":23,
"mechanical":6,
"ebike":17,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:23:14+00:00",
"coordonnees_geo":{
"lon":2.4530601033354,
"lat":48.908168131015
},
"nom_arrondissement_communes":"Bobigny",
"code_insee_commune":None
},
{
"stationcode":"7003",
"name":"Square Boucicaut",
"is_installed":"OUI",
"capacity":60,
"numdocksavailable":19,
"numbikesavailable":41,
"mechanical":18,
"ebike":23,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:23:18+00:00",
"coordonnees_geo":{
"lon":2.325061820447445,
"lat":48.851296433665276
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"5016",
"name":"Thouin - Cardinal Lemoine",
"is_installed":"OUI",
"capacity":17,
"numdocksavailable":9,
"numbikesavailable":8,
"mechanical":1,
"ebike":7,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:23:07+00:00",
"coordonnees_geo":{
"lon":2.3494647851273465,
"lat":48.84504716661511
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"11025",
"name":"Froment - Bréguet",
"is_installed":"OUI",
"capacity":43,
"numdocksavailable":24,
"numbikesavailable":17,
"mechanical":15,
"ebike":2,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:21:10+00:00",
"coordonnees_geo":{
"lon":2.37289470306807,
"lat":48.8570414504784
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"8050",
"name":"Boétie - Ponthieu",
"is_installed":"OUI",
"capacity":33,
"numdocksavailable":1,
"numbikesavailable":11,
"mechanical":2,
"ebike":9,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:20:35+00:00",
"coordonnees_geo":{
"lon":2.3076787590981,
"lat":48.871417284355
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
},
{
"stationcode":"13101",
"name":"Croulebarde - Corvisart",
"is_installed":"OUI",
"capacity":34,
"numdocksavailable":31,
"numbikesavailable":2,
"mechanical":2,
"ebike":0,
"is_renting":"OUI",
"is_returning":"OUI",
"duedate":"2024-04-17T12:23:04+00:00",
"coordonnees_geo":{
"lon":2.3481646925210953,
"lat":48.830981659316855
},
"nom_arrondissement_communes":"Paris",
"code_insee_commune":None
}
]
 
#----------- Function créée pour manager les images ----------

def sauvegarder_image(fichier, contact_id,fav_uuid):
  dossier_upload = os.path.join(os.path.dirname(os.path.realpath(__file__)), "uploads")

  #En terme de création auto de favoris et de sa modification, il est important de tester si le dossier du favoris existe dejà
  if not os.path.isdir(os.path.join(dossier_upload, f"{fav_uuid}")) :
    os.mkdir(os.path.join(dossier_upload, f"{fav_uuid}"))
    
  dossier_upload = os.path.join(dossier_upload, f"{fav_uuid}")

  # Construit le path complet du fichier, l'enregistre et le retourne
  nom_fichier = ".".join((str(contact_id), fichier.filename.rsplit(".")[1]))
  fichier_nom_complet = os.path.join(dossier_upload, nom_fichier)
  fichier.save(fichier_nom_complet)
  return nom_fichier

def vider_dossier (dossier) :
  if os.path.isdir(dossier) :
    for filename in os.listdir(dossier) :
        try :
            os.remove(os.path.join(dossier, filename))  
        except :
            abort(404,"Dossier ou fichier inexistant")

def supprimer_dossier (dossier) :
  vider_dossier(dossier)
  if os.path.isdir(dossier) :
    os.rmdir(dossier)
  
#----------------------------------------------

# S'occuper de l'affichage des images.
@app.route("/image/<path:chemin>")
def images(chemin):
  return send_from_directory("uploads", chemin)

#afficher la liste des stations
@app.get("/")
def accueil () :
  # Je trouve très important de le faire comme ça que de mettre le chemin directement car les séparateurs
  # ne sont pas les memes : / sur mac et \ sur windows
  index_favoris_path = os.path.join("favoris", "index.html.jinja") 
  return render_template(index_favoris_path,stations = stations)

@app.get("/carte")
def carte() :
    return render_template('index.html')

@app.route("/carte/<station>")
def carte_station(station) :
    #Faire un truc avec la station
    return f"""<h1>Carte + {station}</h1>"""


# /liste affiche la liste des favoris
@app.get("/fav")
def liste_fav():
  # Vérifier si le client est connecté avant d'effectuer les actions
  if not "user" in session:
    return redirect(url_for("accueil"))
  
  liste = fav.lister_favoris(session["user"]['uuid'])
  liste = list(map(lambda fav_x: {"libelle": fav_x["station_name"], "url_suppression": url_for("delete_fav", uuid=fav_x["uuid"]), "url_view": url_for("get_fav", uuid=fav_x["uuid"]),"img_url" : os.path.join(fav_x["uuid"],fav_x['picture_name'])}, liste))
  liste_favoris_path = os.path.join("favoris", "liste.html.jinja") 
  return render_template(liste_favoris_path, liste = liste)


# Ajouter un favoris | Form en get et validation en post
@app.get("/fav/new")
def new_fav_form():
  create_favoris_path = os.path.join("favoris", "create.html.jinja") 
  return render_template(create_favoris_path, stations = stations)

@app.post("/fav/new")
def new_fav_post():
  if not "user" in session: abort(403)

  image = request.files['image']
  uuid = str(uuid4())
  fav.new_favoris(session["user"], request.form["stationcode"],uuid) if image.filename == "" else fav.new_favoris(session["user"]['uuid'], request.form["stationcode"],uuid,sauvegarder_image(image,1, uuid))

  return redirect(url_for("liste_fav"))

# Modifier un favoris à base de son uuid | form get et validation en Post
@app.get("/fav/update/<uuid>")
def update_fav_form(uuid):
  fav.get_favoris(uuid)
  modify_favoris_path = os.path.join("favoris", "modify.html.jinja") 
  return render_template(modify_favoris_path, station = stations)
  
@app.post("/fav/update/<uuid>")
def update_fav_put(uuid):

  if not "user" in session: abort(403)

  image = request.files['image']
  if image.filename != "" :
    image_folder = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), "uploads"),f"{uuid}")
    vider_dossier(image_folder)
    fav.update_favoris(uuid,sauvegarder_image(image,1, str(uuid)))
    
  return redirect(url_for("get_fav", uuid=uuid))

# Suppression d'un favoris 
@app.get("/fav/delete/<uuid>")
def delete_fav(uuid):
  if not "user" in session: abort(403,'Acces refusé')
  fav.delete_favoris(uuid)
  image_folder = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), "uploads"),f"{uuid}")
  supprimer_dossier(image_folder)

# reformuler ma liste
  liste = fav.lister_favoris(session["user"]['uuid'])
  liste = list(map(lambda fav_x: {"libelle": fav_x["station_name"], "url_suppression": url_for("delete_fav", uuid=fav_x["uuid"]), "url_view": url_for("get_fav", uuid=fav_x["uuid"]),"img_url" : os.path.join(fav_x["uuid"],fav_x['picture_name']  if fav_x['picture_name'] != None else '_')}, liste))
  liste_favoris_path = os.path.join("favoris", "liste.html.jinja") 
  return render_template(liste_favoris_path, liste = liste)

# Obtenir les infos d'une station favoris
@app.get("/fav/<uuid>")
def get_fav(uuid):
  if not "user" in session: abort(403,'Acces refusé')
  favoris = fav.get_favoris(uuid)
  image_url = os.path.join(uuid,favoris[0]['picture_name'])
  infos_favoris_path = os.path.join("favoris", "infos.html.jinja") 
  return render_template(infos_favoris_path, favoris = favoris[0], image_url = image_url, update_url = url_for("update_fav_put", uuid=uuid) )


#Création automatique d'un favoris à partir de la liste complete de station
@app.get("/fav/auto/<stationcode>")
def new_fav_auto (stationcode) :
  if not 'user' in session : return render_template(os.path.join("auth", "login.html.jinja"), msg= "Connectez-vous pour avoir accès à cette fonctionnalité")
  uuid = uuid4()
  fav.new_favoris(session['user']['uuid'],stationcode,str(uuid))

  return redirect(url_for("liste_fav"))


@app.post("/login")
def login_process() :
    email = request.form["email"]
    password = request.form["password"] # j'attends la facon de crypter de paul pour ajuster
    current_user = ""

    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email) : # email valide ?
        current_user = user.login(email,password)
    else :
        return render_template(os.path.join("auth", "login.html.jinja"), msg= "Email invalide 💀.")
    
    if not current_user :
        return render_template(os.path.join("auth", "login.html.jinja"), msg= "Email ou mot de passe incorrect.")
    else :
        session['user'] = {
                        'nom' : current_user['last_name'],
                        "prenom" : current_user['first_name'],
                        "uuid" : current_user['uuid'],
                        "email" : current_user['email'],
                        }

        return redirect(url_for("accueil"))
    

@app.get("/login")
def login() :
    if 'user' in session  : return render_template(os.path.join("favoris", "index.html.jinja"),stations = stations)   
    return render_template(os.path.join("auth", "login.html.jinja"))

@app.get("/signup")
def inscription() :
    return render_template(os.path.join("auth", "signin.html.jinja"))


@app.post("/signup")
def traitement_inscription() :
    #traiter les information d'inscription et ajouter les cookies
    email = request.form["email"]
    motdepasse = Password()
    motdepasse =  Password.set_password(request.form["motdepasse"])  
    prenom = request.form["prenom"] 
    nom = request.form["nom"] 
    user_uuid = uuid4().hex
    current_user = ""

    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    # email valide ?
    if re.fullmatch(regex, email) : 
        is_signed = user.sign({"email" : email,
                "motdepasse" : motdepasse,
                "prenom" : prenom,
                "nom" : nom,
                "user_uuid" : user_uuid} )
        
        if not is_signed :
            return render_template(os.path.join("auth", "signin.html.jinja"), msg= "Cet utilisateur existe déjà. Connectez-vous.")
        else :
            current_user = user.login(email,request.form["motdepasse"]) #ça ne peut qu'etre succès, c'est la 1ere connexion
            #Assignation des valeurs de session
            session['user'] = {
                            'nom' : current_user['last_name'],
                            "prenom" : current_user['first_name'],
                            "uuid" : current_user['uuid'],
                            "email" : current_user['email'],
                            }

            return redirect(url_for("accueil"))
    else :
       return render_template(os.path.join("auth", "signin.html.jinja"), msg= "Email invalide 💀.")
   


@app.put("/user")
def modification_information() :
    #traiter les information d'inscription et ajouter les cookies
    return f"""<h1>modification information</h1>"""

@app.get("/logout")
def logout() :
    session.pop('user',None)
    return redirect(url_for('accueil'))
