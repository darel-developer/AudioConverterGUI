import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter import filedialog

def convert_text_to_audio(text):
    # Initialisation du moteur de synthèse vocale
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def convert_file_to_audio(file_path):
    # Lecture du fichier
    file_extension = file_path.split('.')[-1].lower()

    if file_extension == 'pdf':
        # Conversion d'un fichier PDF en audio
        pdf_file = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Conversion et lecture de chaque page du PDF en audio en temps réel
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            convert_text_to_audio(text)

        pdf_file.close()
    else:
        # Conversion d'un fichier texte en audio
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            convert_text_to_audio(text)

def choose_file():
    # Ouverture de la boîte de dialogue pour sélectionner le fichier
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte et PDF", "*.txt;*.pdf")])
    if file_path:
        convert_file_to_audio(file_path)

def convert_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        convert_text_to_audio(text)

# Création de la fenêtre principale de l'application
window = tk.Tk()
window.title("Conversion en Audio")
window.geometry("400x350")

# Étiquette et bouton pour choisir le fichier
file_label = tk.Label(window, text="Choisir un fichier:")
file_label.pack()

file_button = tk.Button(window, text="Parcourir", command=choose_file)
file_button.pack()

# Étiquette et champ de saisie pour le texte
text_label = tk.Label(window, text="Saisir le texte:")
text_label.pack()

text_entry = tk.Text(window, height=5)
text_entry.pack()

# Bouton pour convertir le texte en audio
convert_button = tk.Button(window, text="Convertir Texte", command=convert_text)
convert_button.pack()

# Lancement de la boucle principale de l'application
window.mainloop()