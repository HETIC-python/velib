import bcrypt
from .requete import Requete
from flask import Flask, session, redirect, url_for, render_template, send_from_directory, make_response, request, abort


###### Je dois encore tout regler et améliorer mais j'ai fait cette version précaire pour éviter de trop vous ralentir, ne me crucifiez pas si j'ai fait des erreurs ou des incohérences SVP
class Password:
    '''Classe permettant de gérer les mots de passe que ce soit en les ajoutant ou en les vérifiant'''
    def __init__(self):
        self._password = None

    #Erreur si le MDP n'est pas fourni
    @property
    def password(self):
        if self._password is None:
            #À Ajouter Chemin d'erreur pérsonnalisé -------------------------------
            raise AttributeError('No password has been given')
        return self._password

    #Assignation du nouveau mot de passe chiffré
    @password.setter
    def password(self, value):
        self._password = value

    #Chiffrement du mot de passe
    def set_password(motdepasse):
        password_bytes = motdepasse.encode('utf-8')
        password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return password

    #Verification du mot de passe
    def check_password(email, password):
        req = Requete()
        hashed_password = req.select("SELECT password FROM user WHERE email = ?", (email,))
        if not hashed_password:
            return False
        print(hashed_password[0]["password"])
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password[0]["password"].encode("utf-8"))