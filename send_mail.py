import smtplib, ssl
import os

# Paramètres du serveur SMTP
port = 465
smtp_server = "smtp.gmail.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')

# Vérification des variables d'environnement
if not USERNAME or not PASSWORD:
    raise ValueError("Les variables d'environnement USER_EMAIL et USER_PASSWORD doivent être définies.")

# Contenu de l'email
message = """\
Subject: GitHub Email Report

This is your daily email report.
"""

# Création du contexte SSL
context = ssl.create_default_context()

try:
    # Connexion et envoi de l'email
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, USERNAME, message)
    print("Email envoyé avec succès!")
except Exception as e:
    print(f"Erreur lors de l'envoi de l'email: {e}")
