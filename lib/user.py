# from .requete import Requete
# import json
# import os
# stations=[
# {
# "stationcode":"31104",
# "name":"Mairie de Rosny-sous-Bois",
# "is_installed":"OUI",
# "capacity":30,
# "numdocksavailable":10,
# "numbikesavailable":17,
# "mechanical":1,
# "ebike":16,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:23:05+00:00",
# "coordonnees_geo":{
# "lon":2.4865807592869,
# "lat":48.871256519012
# },
# "nom_arrondissement_communes":"Rosny-sous-Bois",
# "code_insee_commune":None
# },
# {
# "stationcode":"44015",
# "name":"Rouget de L'isle - Watteau",
# "is_installed":"OUI",
# "capacity":20,
# "numdocksavailable":15,
# "numbikesavailable":5,
# "mechanical":4,
# "ebike":1,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:23:27+00:00",
# "coordonnees_geo":{
# "lon":2.3963020229163,
# "lat":48.778192750803
# },
# "nom_arrondissement_communes":"Vitry-sur-Seine",
# "code_insee_commune":None
# },
# {
# "stationcode":"12109",
# "name":"Mairie du 12ème",
# "is_installed":"OUI",
# "capacity":30,
# "numdocksavailable":15,
# "numbikesavailable":14,
# "mechanical":14,
# "ebike":0,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:19:58+00:00",
# "coordonnees_geo":{
# "lon":2.3875549435616,
# "lat":48.840855311763
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"14111",
# "name":"Cassini - Denfert-Rochereau",
# "is_installed":"OUI",
# "capacity":25,
# "numdocksavailable":25,
# "numbikesavailable":0,
# "mechanical":0,
# "ebike":0,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:17:12+00:00",
# "coordonnees_geo":{
# "lon":2.3360354080796,
# "lat":48.837525839067
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"32017",
# "name":"Basilique",
# "is_installed":"OUI",
# "capacity":22,
# "numdocksavailable":6,
# "numbikesavailable":14,
# "mechanical":9,
# "ebike":5,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:21:14+00:00",
# "coordonnees_geo":{
# "lon":2.3588666820200914,
# "lat":48.93626891059109
# },
# "nom_arrondissement_communes":"Saint-Denis",
# "code_insee_commune":None
# },
# {
# "stationcode":"11104",
# "name":"Charonne - Robert et Sonia Delaunay",
# "is_installed":"OUI",
# "capacity":20,
# "numdocksavailable":19,
# "numbikesavailable":1,
# "mechanical":0,
# "ebike":1,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:22:56+00:00",
# "coordonnees_geo":{
# "lon":2.3925706744194,
# "lat":48.855907555969
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"8026",
# "name":"Messine - Place Du Pérou",
# "is_installed":"OUI",
# "capacity":12,
# "numdocksavailable":5,
# "numbikesavailable":5,
# "mechanical":4,
# "ebike":1,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:22:39+00:00",
# "coordonnees_geo":{
# "lon":2.315508019010038,
# "lat":48.875448033960744
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"13007",
# "name":"Le Brun - Gobelins",
# "is_installed":"OUI",
# "capacity":48,
# "numdocksavailable":44,
# "numbikesavailable":3,
# "mechanical":2,
# "ebike":1,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:21:20+00:00",
# "coordonnees_geo":{
# "lon":2.3534681351338,
# "lat":48.835092787824
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"7002",
# "name":"Vaneau - Sèvres",
# "is_installed":"OUI",
# "capacity":35,
# "numdocksavailable":24,
# "numbikesavailable":11,
# "mechanical":11,
# "ebike":0,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:22:20+00:00",
# "coordonnees_geo":{
# "lon":2.3204218259346,
# "lat":48.848563233059
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"5110",
# "name":"Lacépède - Monge",
# "is_installed":"OUI",
# "capacity":23,
# "numdocksavailable":20,
# "numbikesavailable":3,
# "mechanical":2,
# "ebike":1,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:18:44+00:00",
# "coordonnees_geo":{
# "lon":2.3519663885235786,
# "lat":48.84389286531899
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"6108",
# "name":"Saint-Romain - Cherche-Midi",
# "is_installed":"OUI",
# "capacity":17,
# "numdocksavailable":9,
# "numbikesavailable":8,
# "mechanical":7,
# "ebike":1,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:20:49+00:00",
# "coordonnees_geo":{
# "lon":2.321374788880348,
# "lat":48.84708159081946
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"41301",
# "name":"Bois de Vincennes - Gare",
# "is_installed":"OUI",
# "capacity":50,
# "numdocksavailable":29,
# "numbikesavailable":21,
# "mechanical":20,
# "ebike":1,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:23:01+00:00",
# "coordonnees_geo":{
# "lon":2.4708339950830287,
# "lat":48.836022242886884
# },
# "nom_arrondissement_communes":"Nogent-sur-Marne",
# "code_insee_commune":None
# },
# {
# "stationcode":"6021",
# "name":"Beaux-Arts - Bonaparte",
# "is_installed":"OUI",
# "capacity":20,
# "numdocksavailable":4,
# "numbikesavailable":13,
# "mechanical":11,
# "ebike":2,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:23:19+00:00",
# "coordonnees_geo":{
# "lon":2.334851883351803,
# "lat":48.856451985395786
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"25006",
# "name":"Place Nelson Mandela",
# "is_installed":"OUI",
# "capacity":22,
# "numdocksavailable":19,
# "numbikesavailable":3,
# "mechanical":0,
# "ebike":3,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:23:32+00:00",
# "coordonnees_geo":{
# "lon":2.1961666225454,
# "lat":48.862453313908
# },
# "nom_arrondissement_communes":"Rueil-Malmaison",
# "code_insee_commune":None
# },
# {
# "stationcode":"30002",
# "name":"Jean Rostand - Paul Vaillant Couturier",
# "is_installed":"OUI",
# "capacity":40,
# "numdocksavailable":15,
# "numbikesavailable":23,
# "mechanical":6,
# "ebike":17,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:23:14+00:00",
# "coordonnees_geo":{
# "lon":2.4530601033354,
# "lat":48.908168131015
# },
# "nom_arrondissement_communes":"Bobigny",
# "code_insee_commune":None
# },
# {
# "stationcode":"7003",
# "name":"Square Boucicaut",
# "is_installed":"OUI",
# "capacity":60,
# "numdocksavailable":19,
# "numbikesavailable":41,
# "mechanical":18,
# "ebike":23,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:23:18+00:00",
# "coordonnees_geo":{
# "lon":2.325061820447445,
# "lat":48.851296433665276
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"5016",
# "name":"Thouin - Cardinal Lemoine",
# "is_installed":"OUI",
# "capacity":17,
# "numdocksavailable":9,
# "numbikesavailable":8,
# "mechanical":1,
# "ebike":7,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:23:07+00:00",
# "coordonnees_geo":{
# "lon":2.3494647851273465,
# "lat":48.84504716661511
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"11025",
# "name":"Froment - Bréguet",
# "is_installed":"OUI",
# "capacity":43,
# "numdocksavailable":24,
# "numbikesavailable":17,
# "mechanical":15,
# "ebike":2,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:21:10+00:00",
# "coordonnees_geo":{
# "lon":2.37289470306807,
# "lat":48.8570414504784
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"8050",
# "name":"Boétie - Ponthieu",
# "is_installed":"OUI",
# "capacity":33,
# "numdocksavailable":1,
# "numbikesavailable":11,
# "mechanical":2,
# "ebike":9,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:20:35+00:00",
# "coordonnees_geo":{
# "lon":2.3076787590981,
# "lat":48.871417284355
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# },
# {
# "stationcode":"13101",
# "name":"Croulebarde - Corvisart",
# "is_installed":"OUI",
# "capacity":34,
# "numdocksavailable":31,
# "numbikesavailable":2,
# "mechanical":2,
# "ebike":0,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:23:04+00:00",
# "coordonnees_geo":{
# "lon":2.3481646925210953,
# "lat":48.830981659316855
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# }
# ]

# def lister_favoris(user_id):

#   req = Requete()
#   res = req.select("SELECT * FROM favoris WHERE user_id = ? ORDER BY created_at DESC", user_id)
#   print(res)
#   return res

# def new_favoris(user_id, station_code, uuid,image_name=''):
  
#   # ici on devrait demander les infos de la station à Bob à partir de son stationcode qu'on a
#   station =  {
# "stationcode":"13101",
# "name":"Croulebarde - Corvisart",
# "is_installed":"OUI",
# "capacity":34,
# "numdocksavailable":31,
# "numbikesavailable":2,
# "mechanical":2,
# "ebike":0,
# "is_renting":"OUI",
# "is_returning":"OUI",
# "duedate":"2024-04-17T12:23:04+00:00",
# "coordonnees_geo":{
# "lon":2.3481646925210953,
# "lat":48.830981659316855
# },
# "nom_arrondissement_communes":"Paris",
# "code_insee_commune":None
# }
  
#   req = Requete()
#   req.insert("INSERT INTO favoris (uuid,station_name,user_id,picture_name) VALUES (?, ?, ?, ?)", (uuid,station['name'], user_id, image_name))

# def delete_favoris(uuid_fav):
#   req = Requete()
#   req.insert("DELETE FROM favoris WHERE uuid = ?", uuid_fav)

# def get_favoris (uuid) :
#     req = Requete()
#     resultat = req.select("SELECT * FROM favoris WHERE uuid = ?", uuid)

#     return resultat

# def update_favoris (uuid, image_name) :
#     req = Requete()
#     return req.update("UPDATE favoris SET picture_name= ? WHERE uuid = ?", (image_name,uuid))