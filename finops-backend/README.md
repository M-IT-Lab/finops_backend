# 📊 FinOps Backend & Infrastructure Suite

Gehärtete REST-API zur Verfolgung, Budgetierung und Zuordnung von Cloud-Infrastruktur-Kosten (FinOps).

## 🏛️ Systemarchitektur
- Client / Gateway: cURL / Frontend-Interface für HTTP-Requests.
- API Engine (Flask): Validierung von API-Keys, Monatsbudgets & Kostenstellen.
- Database Layer (MySQL): Gehärtete DB für Transaktionen & Kundenstammdaten.

## 🛡️ Security & Hardening
- Credential Isolation: Sensible Zugangsdaten in .env gekapselt.
- Principle of Least Privilege: Nutzung des dedizierten DB-Users finops_api.
- Git Privacy & Transport: Anonymisierte E-Mail, .gitignore-Schutz & Ed25519-SSH-Key.

---
**M-IT Lab** – Enterprise Systems & IT-Management
