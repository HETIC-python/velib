import mariadb

class Requete:
  def __init__(self):
    # Configuration des infos de connexion
    self.config = {
      "host": "127.0.0.1",
      "port": 3306,
      "user": "root",
      "password": "",
      "database": "api_PDF"
    }
    # Alias pour favoriser/factoriser d'autres requettes
    self.insert = self.action
    self.update = self.action
    self.delete = self.action

  
  def debut(self):
    self.connexion = mariadb.connect(**self.config)
    self.curseur = self.connexion.cursor()

  def fin(self):
    self.curseur.close()
    self.connexion.close()

  def exec(self, requete, params):
    if not params is None and not isinstance(params, tuple):
      params = (params,)
    self.curseur.execute(requete, params)


  def select(self, requete, params=None):
    self.debut()
    self.exec(requete, params)
    description = self.curseur.description
    liste = self.curseur.fetchall()
    self.fin()
    entetes = list(map(lambda h: h[0], description))
    resultats = list(map(lambda l: dict(zip(entetes, l)), liste))
    return resultats

  # Pour les auitres types d'actions
  def action(self, requete, params=None):
    self.debut()
    self.exec(requete, params)
    self.connexion.commit()
    self.fin()