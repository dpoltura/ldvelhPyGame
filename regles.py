import tkinter as tk
from tkinter import ttk
import PyPDF2

class Regles(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.regles_text = ""
        self.charger_regles()
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Règles du Jeu", font=("Arial", 16, "bold")).pack(pady=10)

        self.text_widget = tk.Text(self, wrap=tk.WORD, width=80, height=40)
        self.text_widget.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        self.text_widget.insert(tk.END, self.regles_text)
        self.text_widget.config(state=tk.DISABLED)  # Rendre le texte en lecture seule

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_widget.configure(yscrollcommand=scrollbar.set)

    def charger_regles(self):
        try:
            with open("livre.pdf", "rb") as file:
                reader = PyPDF2.PdfReader(file)
                for page_num in range(6, 13):  # Pages 7 à 13 (index 6 à 12)
                    page = reader.pages[page_num]
                    self.regles_text += page.extract_text() + "\n\n"
            self.regles_text = self.regles_text.replace("\n", " ").replace("  ", "\n\n")
        except Exception as e:
            self.regles_text = f"Erreur lors du chargement des règles : {str(e)}"