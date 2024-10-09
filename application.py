import tkinter as tk
from tkinter import ttk
from feuille_aventure import FeuilleAventureSimple
from lancer_des_simple import LancerDesSimple
from feuille_rencontre import FeuilleRencontre
from table_conflits import TableConflits
from livre_jeu import LivreJeu
from lancer_des import LancerDes
from regles import Regles

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("L'Horreur dans la Vallée - Feuilles de jeu")
        self.geometry("1200x900")

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.paned_window = ttk.PanedWindow(self.main_frame, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

        self.notebook = ttk.Notebook(self.paned_window)
        self.paned_window.add(self.notebook, weight=3)

        self.side_frame = ttk.Frame(self.paned_window)
        self.paned_window.add(self.side_frame, weight=1)

        self.feuille_aventure = FeuilleAventureSimple(self.side_frame)
        self.feuille_aventure.pack(fill=tk.BOTH, expand=True)

        self.lancer_des_simple = LancerDesSimple(self.side_frame)
        self.lancer_des_simple.pack(fill=tk.X, pady=10)

        self.livre_jeu = LivreJeu(self.notebook)
        self.feuille_rencontre = FeuilleRencontre(self.notebook)
        self.table_conflits = TableConflits(self.notebook)
        self.lancer_des = LancerDes(self.notebook)
        self.regles = Regles(self.notebook)

        self.notebook.add(self.livre_jeu, text="Livre-Jeu")
        self.notebook.add(self.feuille_rencontre, text="Feuille de Rencontre")
        self.notebook.add(self.table_conflits, text="Table des Conflits")
        self.notebook.add(self.lancer_des, text="Lancer de Dés")
        self.notebook.add(self.regles, text="Règles")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.feuille_aventure.sauvegarder_donnees()
        self.destroy()

if __name__ == "__main__":
    app = Application()
    app.mainloop()