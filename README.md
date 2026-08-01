# FinOps Backend: Automatisierte Server-Infrastruktur

## 📌 Projektübersicht
Dieses Projekt stellt ein stabiles Backend für die Verarbeitung von Rechnungs- und Verbrauchsdaten bereit. Der Fokus der Entwicklung liegt auf einer ausfallsicheren Systemarchitektur, effizienter Datenverarbeitung und sauberen Datenbank-Prozessen.

## 🏗️ Systemarchitektur (Logistikzentrum)
Die Anwendung wurde vom manuellen Entwicklungsbetrieb in einen vollautomatisierten Produktionsstatus überführt. 

* **Betriebssystem:** Ubuntu Linux
* **Datenbank:** MySQL (Relationales Datenbankdesign)
* **Applikationsserver (Gunicorn):** Eingerichtet mit 3 parallelen "Workern" zur gleichzeitigen Verarbeitung mehrerer Datenpakete (Requests) ohne Rückstau.
* **Systemdienst (Systemd):** Einbindung als nativer Hintergrunddienst. Das System wird 24/7 überwacht, startet bei einem Server-Reboot automatisch und verfügt über eine Selbstheilungs-Funktion (`Restart=always`) bei Abstürzen.

## ⚙️ Server-Inbetriebnahme
Die Infrastruktur wird über `systemctl` gesteuert.

**Status prüfen:**
`sudo systemctl status finops`

**Dienst neu starten (z.B. nach Updates):**
`sudo systemctl restart finops`

## 🗄️ Datenstruktur
Die empfangenen Daten werden sicher getrennt und strukturiert in einer normalisierten MySQL-Datenbank abgelegt, um spätere Abrufe (GET-Endpunkte) effizient zu gestalten.
