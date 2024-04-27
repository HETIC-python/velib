# velib


**Membres du groupe**

    - Abdul	Jiad
    - Benguigui	Avidan
    - Cieplucha	Hugo
    - Charbel	Paul
    - Charlery	Malcolm
    - Cherbonnier	Eva
    - GLIN-DAYI	Faithgot Letonsou


## Comment démarrer le projet : 

## Etape 1
- Charger le fichier `velib.sql`  du dossier `Alice/` comme base de données.
- Accéder au fichier `Alice/lib/requette.py` pour vérifier/reconfiguer les infos de connexion.

## Lancer les serveurs

## Etape 2
Installer les librairies disponibles dans le fichier `requirement.txt` avec :
```pip3 install -r requirements.txt``` (En étant à la source du projet).

## Etape 3
Par défaut l'api tourne sur le port `8081`, s'il est occupé :
    - Allez dans `api/app.py` et renseigner un port disponible 
    - Allez dans `Alice/lib/api.py` et adapter BOB_URL_SOURCE à votre nouveau port.
    
## Etape 4
Ouvrez un terminal pour chacun des dossiers

|       |   Alice |   Bob/api |
|---    |:-:    |:-:    |
|  Action 1   |   ```cd ./Alice```   |   ```cd ./api``` |
|   Action 2;   |   ```flask run --debug```  |   ```python app.py``` ou `python3 app.py` si besoin |

---


## Explication du projet : 
Le projet a essayé de respecter les normes et le contenu du cahier de charges. En plus des fonctionnalités minimum demandé, nous avons :
- Ajouté aux favoris l'option d'images, ce qui permet spécialement lors de la modification de changer l'image de notre station favoris (les infos reçues de l'opendata ne seront pas modifiées car elles ne dépendent pas de nous).
- Ajouté une fonctionnalité d'ajout automatique d'une station aux favoris
- Essayé de produire une interface visuelle plus simple pour la navigation
- Essayé d'optimiser au max la sécurité et d'insérer le plus de logiques possibles.

<img width="1440" alt="Capture d’écran 2024-04-27 à 20 05 37" src="https://github.com/HETIC-python/velib/assets/121299370/cb8598ee-fff2-4eff-af7e-67273deb837a">
<img width="1440" alt="Capture d’écran 2024-04-27 à 20 05 53" src="https://github.com/HETIC-python/velib/assets/121299370/60ff9c70-0236-4098-8ee5-8df8f236177e">
<img width="1440" alt="Capture d’écran 2024-04-27 à 20 06 35" src="https://github.com/HETIC-python/velib/assets/121299370/56ff596f-57a7-434b-96b7-ed5baaa8ab51">
<img width="1440" alt="Capture d’écran 2024-04-27 à 20 07 37" src="https://github.com/HETIC-python/velib/assets/121299370/9c7b472e-3234-46bb-b7f7-324a35f2463f">
<img width="1440" alt="Capture d’écran 2024-04-27 à 20 08 18" src="https://github.com/HETIC-python/velib/assets/121299370/8fc61d00-b101-4205-95f5-682787705040">
<img width="1440" alt="Capture d’écran 2024-04-27 à 20 17 38" src="https://github.com/HETIC-python/velib/assets/121299370/b37e04de-e596-464f-b6c6-8b244154d902">
<img width="1440" alt="Capture d’écran 2024-04-27 à 20 18 09" src="https://github.com/HETIC-python/velib/assets/121299370/f2c21ea8-89ff-4065-a81e-7ed1a568e3f2">
<img width="1440" alt="Capture d’écran 2024-04-27 à 20 18 28" src="https://github.com/HETIC-python/velib/assets/121299370/0001fd98-c641-44b6-9ea1-ae5e543ada1d">
