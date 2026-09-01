import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
import mysql.connector

load_dotenv()

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "finops_db")
    )


@app.route('/')
def index():
    return jsonify({"status": "Flask Backend läuft und ist startklar!"})


@app.route('/alarm')
def check_limit():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT k.Kunden_ID, k.Adresse, k.Kostenstelle, k.Monatsbudget, SUM(b.Betrag) AS Gesamtkosten
        FROM Kunden k
        JOIN Bestellungen b ON k.Kunden_ID = b.Kunden_ID
        GROUP BY k.Kunden_ID, k.Adresse, k.Kostenstelle, k.Monatsbudget
        HAVING Gesamtkosten >= k.Monatsbudget;
        """

        cursor.execute(query)
        res = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify({
            "status": "success",
            "budget_exceeded_customers": res
        })

    except Exception:
        return jsonify({"status": "error", "message": "Ein interner Serverfehler ist aufgetreten."}), 500


@app.route('/api/v1/usage', methods=['POST'])
def add_usage():
    try:
        data = request.get_json()
        kunden_id = data.get('kunden_id')
        betrag = data.get('betrag')

        if not kunden_id or not betrag:
            return jsonify({"status": "error", "message": "kunden_id und betrag erforderlich!"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO Bestellungen (Kunden_ID, Betrag) VALUES (%s, %s);"
        cursor.execute(query, (kunden_id, betrag))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"status": "success", "message": f"Kosten von {betrag} € für Kunde {kunden_id} verbucht!"}), 201

    except Exception:
        return jsonify({"status": "error", "message": "Ein interner Serverfehler ist aufgetreten."}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
