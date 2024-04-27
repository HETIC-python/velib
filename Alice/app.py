from flask import Flask, session, redirect, url_for, render_template,send_from_directory,make_response, request, abort
from functools import wraps
import lib.user as user
import lib.favorite as fav
from lib.password import Password  
import lib.api as api
import re
import os
from uuid import uuid4

app = Flask("velib")
app.secret_key = b"ee18fcfbf6b7351ca99adb553a5a9d056538956ad9244fd622f4d93250ee3fce"

# list de stations faite suivant les normes d'opendatas en attendant que Bob soit opérationnel

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
  index_favoris_path = "index.html.jinja" 
  return render_template("index.html.jinja",stations = api.get_all_stations())

@app.get("/carte")
def carte() :
    stations = api.get_all_stations()
    return render_template('carte.html.jinja', stations = stations)

@app.route("/<stationcode>")
def carte_station(stationcode) :
    #Faire un truc avec la station
  station = api.get_one_station(stationcode)
  return render_template(os.path.join("station", "infos.html.jinja"), station=station )


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
  if not 'user' in session : return render_template(os.path.join("auth", "login.html.jinja"), msg= "Connectez-vous pour avoir accès à cette fonctionnalité")
  create_favoris_path = os.path.join("favoris", "create.html.jinja") 
  return render_template(create_favoris_path, stations = api.get_all_stations())

@app.post("/fav/new")
def new_fav_post():
  if not 'user' in session : return render_template(os.path.join("auth", "login.html.jinja"), msg= "Connectez-vous pour avoir accès à cette fonctionnalité")
  if fav.is_existed_favoris(request.form["stationcode"]) : return redirect(url_for("liste_fav"))

  image = request.files['image']
  uuid = str(uuid4())
  fav.new_favoris(session["user"], request.form["stationcode"],uuid) if image.filename == "" else fav.new_favoris(session["user"]['uuid'], request.form["stationcode"],uuid,sauvegarder_image(image,1, uuid))

  return redirect(url_for("liste_fav"))

# Modifier un favoris à base de son uuid | form get et validation en Post
@app.get("/fav/update/<uuid>")
def update_fav_form(uuid):
  if not 'user' in session : return render_template(os.path.join("auth", "login.html.jinja"), msg= "Connectez-vous pour avoir accès à cette fonctionnalité")
  fav.get_favoris(uuid)
  modify_favoris_path = os.path.join("favoris", "modify.html.jinja") 
  return render_template(modify_favoris_path, station = api.get_all_stations())
  
@app.post("/fav/update/<uuid>")
def update_fav_put(uuid):

  if not 'user' in session : return render_template(os.path.join("auth", "login.html.jinja"), msg= "Connectez-vous pour avoir accès à cette fonctionnalité")

  image = request.files['image']
  if image.filename != "" :
    image_folder = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), "uploads"),f"{uuid}")
    vider_dossier(image_folder)
    fav.update_favoris(uuid,sauvegarder_image(image,1, str(uuid)))
    
  return redirect(url_for("get_fav", uuid=uuid))

# Suppression d'un favoris 
@app.get("/fav/delete/<uuid>")
def delete_fav(uuid):
  if not 'user' in session : return render_template(os.path.join("auth", "login.html.jinja"), msg= "Connectez-vous pour avoir accès à cette fonctionnalité")
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
  if not 'user' in session : return render_template(os.path.join("auth", "login.html.jinja"), msg= "Connectez-vous pour avoir accès à cette fonctionnalité")
  favoris = fav.get_favoris(uuid)
  image_url = os.path.join(uuid,favoris[0]['picture_name'])
  infos_favoris_path = os.path.join("favoris", "infos.html.jinja") 
  station = {
     "stationcode" : favoris[0]['stationcode'],
     "name" : favoris[0]['station_name'],
     "numbikesavailable" : favoris[0]['numbikesavailable'],
     "coordonnees_geo" :{
        "lon" : favoris[0]['longitude'],
        "lat" : favoris[0]['latitude'],
     }
  }

  return render_template(infos_favoris_path, favoris = favoris[0], image_url = image_url, update_url = url_for("update_fav_put", uuid=uuid), station=station )


#Création automatique d'un favoris à partir de la liste complete de station
@app.get("/fav/auto/<stationcode>")
def new_fav_auto (stationcode) :
  if not 'user' in session : return render_template(os.path.join("auth", "login.html.jinja"), msg= "Connectez-vous pour avoir accès à cette fonctionnalité")
  if fav.is_existed_favoris(stationcode) : return redirect(url_for("liste_fav"))
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
    if 'user' in session  : return render_template("index.html.jinja",stations = api.get_all_stations())   
    return render_template(os.path.join("auth", "login.html.jinja"))

@app.get("/signup")
def inscription() :
  if 'user' in session  : return render_template("index.html.jinja",stations = api.get_all_stations())   
  return render_template(os.path.join("auth", "signin.html.jinja"))


@app.post("/signup")
def traitement_inscription() :
    #traiter les information d'inscription et ajouter les cookies
    if 'user' in session  : return render_template("index.html.jinja",stations = api.get_all_stations())   

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
   


@app.get("/user")
def profil_user() :
    if not 'user' in session : return render_template(os.path.join("auth", "login.html.jinja"), msg= "Connectez-vous pour avoir accès à cette fonctionnalité")
    return render_template("profil.html.jinja")

@app.get("/logout")
def logout() :
    if not 'user' in session  : return render_template("index.html.jinja",stations = api.get_all_stations())   

    session.pop('user',None)
    return redirect(url_for('accueil'))
