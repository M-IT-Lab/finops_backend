from flask import Flask
import pymssql
import os
from dotenv import load_dotenv

# Geheimnisse laden
load_dotenv()

# Hier erschaffen wir unseren Mini-Webserver
app = Flask(__name__)

# Diese Route definiert, was passiert, wenn jemand die Hauptseite aufruft
@app.route('/')
def datenbank_test():
    server = '127.0.0.1' 
    username = 'SA'
    password = os.getenv('SA_PASSWORD')
    
    try:
        conn = pymssql.connect(server=server, user=username, password=password, database='master')
        conn.close()
        # Statt 'print' nutzen wir 'return', um den Text als Webseite an den Browser zu schicken
        return "<h1>Bäm! Erfolg!</h1><p>Die Web-App läuft und die SQL-Datenbank antwortet!</p>"
    except Exception as e:
        return f"<h1>Fehler</h1><p>{e}</p>"

# Startbefehl für den Webserver
if __name__ == '__main__':
    # Wir lassen ihn lokal auf Port 5000 lauschen
    app.run(host='127.0.0.1', port=5000)
