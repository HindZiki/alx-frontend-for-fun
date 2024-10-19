#!/usr/bin/python3
import sys
import os

if __name__ == "__main__":
    # Vérification du nombre d'arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Vérification de l'existence du fichier Markdown
    if not os.path.exists(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)
    
    # Si tout est correct, ne rien faire et quitter avec succès
    sys.exit(0)
