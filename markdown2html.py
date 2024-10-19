#!/usr/bin/python3
import sys
import os

if __name__ == "__main__":
    # Vérifier si le nombre d'arguments est inférieur à 3 (car sys.argv[0] est le nom du script)
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    # Récupérer les arguments
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Vérifier si le fichier Markdown n'existe pas
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Si tout est correct, quitter avec succès (code 0)
    sys.exit(0)
