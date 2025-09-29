# 🐍 Flask – Un des frameworks Python les plus populaires

Parmi les frameworks les plus utilisés en Python, **Flask** occupe une place de choix.  
À la fois **léger** et **puissant**, il permet de créer des applications web en quelques lignes de code.  

---

## 🚀 Qu’est-ce que Flask ?
Flask est un **micro-framework open source** écrit en Python.  

👉 On parle de *micro framework* car il inclut seulement les fonctionnalités essentielles au développement web :  
- Gestion des **requêtes HTTP**  
- **Serveur web** intégré  
- Gestion des **cookies**  

L’idée est de fournir un noyau minimaliste mais **extensible** grâce à des **extensions** (base de données, authentification, formulaires, upload de fichiers…).  

📌 Anecdote : Flask est né d’un défi lancé par **Armin Ronacher**, qui voulait créer un framework web complet… en un seul fichier Python.  

---

## ✅ Les avantages de Flask
Flask est très apprécié car il combine **simplicité** et **flexibilité**.  

- **Léger** : installe seulement ce dont tu as besoin  
- **Extensible** : de nombreuses extensions disponibles  
- **Flexible** : aucune décision imposée, c’est toi qui choisis  
- **Populaire** : utilisé par Pinterest, LinkedIn, et élu *framework web le plus populaire* (Python Developers Survey, 2018)  

---

## ⚙️ Comment fonctionne Flask ?
### 1. Installation
Il est recommandé d’utiliser **Python ≥ 3.6**.  

```bash
# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows

# Installer Flask
pip install flask
Flask installe automatiquement :

Jinja (moteur de templates)

Werkzeug (WSGI, interface standard Python ↔ serveur)

MarkupSafe (sécurité contre les injections)

ItsDangerous (intégrité des données)

Click (CLI pour scripts Python)

### 2. Exemple minimal
Un "Hello World" en Flask :

python
Copier le code
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
👉 Lance le serveur :

bash
Copier le code
python app.py
Puis ouvre dans ton navigateur :

cpp
Copier le code
http://127.0.0.1:5000

### 3. Tests
Flask facilite l’ajout de tests automatisés pour vérifier ton code :

python
Copier le code
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, Flask!" in response.data
⚡ Les tests permettent d’avancer par itérations agiles sans tout casser.

### 🔌 Extensions utiles pour Flask
Voici quelques extensions populaires pour enrichir tes applications :

Extension	Utilité principale
Flask-SQLAlchemy	Gestion base de données relationnelle
Flask-Login	Authentification et gestion des sessions
Flask-WTF	Gestion avancée des formulaires
Flask-Migrate	Migration des bases de données
Flask-Mail	Envoi d’emails
Flask-Caching	Mise en cache pour améliorer les performances

### 📚 Sources
Datascientest – Avantages et fonctionnement de Flask