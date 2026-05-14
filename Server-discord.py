import sys
import os

def main():
    print("=== BUILDER INTERFACE - CONSOLE VERSION ===")
    print()

    # Entrer le webhook Discord
    webhook = input("Entrer webhook Discord: ").strip()

    if not webhook:
        print("Erreur: Webhook manquant")
        return

    # Demander le fichier à modifier
    script_path = input("Chemin du script Python à modifier (ex: Stealer_discord.py): ").strip()

    if not os.path.exists(script_path):
        print(f"Erreur: Fichier '{script_path}' introuvable")
        return

    try:
        # Lire le fichier
        with open(script_path, "r", encoding="utf-8") as f:
            code = f.read()

        # Remplacer le placeholder
        if "WEBHOOK_URL_PLACEHOLDER" in code:
            code = code.replace("WEBHOOK_URL_PLACEHOLDER", webhook)

            # Sauvegarder le fichier modifié
            output_path = script_path.replace(".py", "_built.py")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(code)

            print(f"✓ Script construit avec succès: {output_path}")
            print(f"✓ Webhook intégré: {webhook}")
        else:
            print("Erreur: Placeholder 'WEBHOOK_URL_PLACEHOLDER' non trouvé dans le fichier")

    except Exception as e:
        print(f"Erreur lors du traitement: {e}")

if __name__ == "__main__":
    main()
    input("\nAppuyez sur Entrée pour quitter...")
