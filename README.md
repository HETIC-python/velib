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
    - Charger le fichier `velib.sql` comme base de données.
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

