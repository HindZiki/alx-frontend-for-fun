#!/usr/bin/python3
import sys
import os

def convert_markdown_to_html(markdown_file, html_file):
    """
    Convertit un fichier Markdown en fichier HTML en traitant les titres (headings).
    """
    with open(markdown_file, 'r') as md_file, open(html_file, 'w') as html_output:
        for line in md_file:
            # Suppression des espaces en début et fin de ligne
            line = line.strip()
            
            # Gestion des titres
            if line.startswith('#'):
                # Compter le nombre de #
                heading_level = len(line.split(' ')[0])
                # Vérifier que le heading_level est valide (de 1 à 6)
                if 1 <= heading_level <= 6:
                    # Extraire le texte du titre
                    heading_text = line[heading_level:].strip()
                    # Générer le HTML correspondant
                    html_output.write(f'<h{heading_level}>{heading_text}</h{heading_level}>\n')
    
if __name__ == "__main__":
    # Vérification du nombre d'arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Vérification de l'existence du fichier Markdown
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Conversion du fichier Markdown en HTML
    convert_markdown_to_html(markdown_file, html_file)

    # Si tout est correct, quitter avec succès
    sys.exit(0)
