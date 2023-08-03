import os
import genanki
from pathlib import Path

# Define the path to the folder containing the memrise CSV files
# Onde você deve colocar os arquivos csv no seguinte formato:
# Good morning !!!, Bom dia
# This is good, Isso é bom
# A partir do formato acima com as vírgulas separando a tradução
# Será criado na pasta apkg o novo baralho no Anki 
# Caso não conheça o Anki é um programa que auxilia no aprendizado de novos idiomas
# Tem funcionalidades bem práticas como por exemplo de acrescentar 
# áudios das frases novo idioma em aprendizado. 
Caminho_do_Projeto = Path(__file__)
home = Path(__file__)
ideias = home.parent
print('Caminho home:', ideias)
memrise_folder = ideias / "memrise"
print('Caminho home:', memrise_folder)
# Define the path to the folder where the output APKG files will be saved
apkg_folder = ideias / "apkg"

ver = os.listdir(memrise_folder)
print('Caminho:', ver)
# Loop through all CSV files in the memrise folder
for filename in os.listdir(memrise_folder):
    if filename.endswith(".csv"):
        # Create a new deck for each file
        deck = genanki.Deck(
            1, # Unique ID for the deck
            filename.replace(".csv", "") # Name of the deck (same as the CSV filename without the extension)
        )

        # Read the CSV file and add the data as notes to the deck
        with open(os.path.join(memrise_folder, filename), "r") as f:
            lines = f.readlines()[1:] # Skip the header line
            for line in lines:
                fields = line.strip().split(",")
                note = genanki.Note(
                    model=genanki.Model(
                        1, # Unique ID for the model
                        "Basic",
                        fields=[{"name": "Front"}, {"name": "Back"}],
                        templates=[{
                            "name": "Card 1",
                            "qfmt": "{{Front}}",
                            "afmt": "{{FrontSide}}<hr id=\"answer\">{{Back}}"
                        }]
                    ),
                    fields=[fields[0], fields[1]]
                )
                deck.add_note(note)

        # Save the deck as an APKG file in the apkg folder
        apkg_file_path = os.path.join(apkg_folder, filename.replace(".csv", ".apkg"))
        genanki.Package(deck).write_to_file(apkg_file_path)