import tkinter as tk
from tkinter import ttk, scrolledtext
import PyPDF2
import re
import json
import os

class LivreJeu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.paragraphes = {}
        self.dernier_paragraphe = "1"
        self.fichier_sauvegarde = "dernier_paragraphe.json"
        self.create_widgets()
        self.charger_paragraphes()
        self.charger_dernier_paragraphe()
        self.afficher_paragraphe(self.dernier_paragraphe)

    def create_widgets(self):
        ttk.Label(self, text="L'Horreur dans la Vallée", font=("Arial", 16, "bold")).pack(pady=10)

        self.texte_paragraphe = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=60, height=20)
        self.texte_paragraphe.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        frame_nav = ttk.Frame(self)
        frame_nav.pack(pady=10)

        ttk.Label(frame_nav, text="Aller au paragraphe :").pack(side=tk.LEFT)
        self.entree_paragraphe = ttk.Entry(frame_nav, width=5)
        self.entree_paragraphe.pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_nav, text="Go", command=self.aller_au_paragraphe).pack(side=tk.LEFT)

    def charger_paragraphes(self):
        try:
            with open("livre.pdf", "rb") as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages[13:]:  # Commencer à partir de la page 14 (index 13)
                    text += page.extract_text() + "\n"

                # Utiliser une expression régulière pour diviser le texte en paragraphes
                paragraphs = re.split(r'(?m)^\s*(\d+)\s*$', text)
                
                # Ignorer le premier élément qui est vide
                paragraphs = paragraphs[1:]
                
                for i in range(0, len(paragraphs), 2):
                    numero = paragraphs[i].strip()
                    contenu = paragraphs[i+1].strip() if i+1 < len(paragraphs) else ""
                    self.paragraphes[numero] = contenu

            print(f"Nombre de paragraphes chargés : {len(self.paragraphes)}")

        except FileNotFoundError:
            print("Le fichier 'livre.pdf' n'a pas été trouvé.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la lecture du PDF : {e}")

    def aller_au_paragraphe(self):
        numero = self.entree_paragraphe.get()
        self.afficher_paragraphe(numero)

    def afficher_paragraphe(self, numero):
        if numero in self.paragraphes:
            self.texte_paragraphe.delete('1.0', tk.END)
            self.texte_paragraphe.insert(tk.END, self.paragraphes[numero])
            self.dernier_paragraphe = numero
            self.sauvegarder_dernier_paragraphe()
        else:
            self.texte_paragraphe.delete('1.0', tk.END)
            self.texte_paragraphe.insert(tk.END, "Paragraphe non trouvé.")

    def sauvegarder_dernier_paragraphe(self):
        with open(self.fichier_sauvegarde, 'w') as f:
            json.dump({"dernier_paragraphe": self.dernier_paragraphe}, f)

    def charger_dernier_paragraphe(self):
        if os.path.exists(self.fichier_sauvegarde):
            with open(self.fichier_sauvegarde, 'r') as f:
                data = json.load(f)
                self.dernier_paragraphe = data.get("dernier_paragraphe", "1")
        else:
            self.dernier_paragraphe = "1"

    def on_closing(self):
        self.sauvegarder_dernier_paragraphe()