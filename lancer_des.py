import tkinter as tk
from tkinter import ttk
import random

class LancerDes(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Lancer de Dés", font=("Arial", 16, "bold")).pack(pady=10)

        # Frame pour le lancer de 1D6
        frame_1d6 = ttk.LabelFrame(self, text="Lancer 1D6")
        frame_1d6.pack(pady=10, padx=10, fill="x")

        ttk.Button(frame_1d6, text="Lancer 1D6", command=self.lancer_1d6).pack(pady=5)
        self.resultat_1d6 = ttk.Label(frame_1d6, text="Résultat: ")
        self.resultat_1d6.pack(pady=5)

        # Frame pour le lancer de 2D6
        frame_2d6 = ttk.LabelFrame(self, text="Lancer 2D6")
        frame_2d6.pack(pady=10, padx=10, fill="x")

        ttk.Button(frame_2d6, text="Lancer 2D6", command=self.lancer_2d6).pack(pady=5)
        self.resultat_2d6 = ttk.Label(frame_2d6, text="Résultat: ")
        self.resultat_2d6.pack(pady=5)

        # Frame pour le lancer personnalisé
        frame_personnalise = ttk.LabelFrame(self, text="Lancer Personnalisé")
        frame_personnalise.pack(pady=10, padx=10, fill="x")

        ttk.Label(frame_personnalise, text="Nombre de dés:").grid(row=0, column=0, padx=5, pady=5)
        self.nb_des = ttk.Entry(frame_personnalise, width=5)
        self.nb_des.grid(row=0, column=1, padx=5, pady=5)
        self.nb_des.insert(0, "1")

        ttk.Label(frame_personnalise, text="Nombre de faces:").grid(row=1, column=0, padx=5, pady=5)
        self.nb_faces = ttk.Entry(frame_personnalise, width=5)
        self.nb_faces.grid(row=1, column=1, padx=5, pady=5)
        self.nb_faces.insert(0, "6")

        ttk.Button(frame_personnalise, text="Lancer", command=self.lancer_personnalise).grid(row=2, column=0, columnspan=2, pady=5)
        self.resultat_personnalise = ttk.Label(frame_personnalise, text="Résultat: ")
        self.resultat_personnalise.grid(row=3, column=0, columnspan=2, pady=5)

    def lancer_1d6(self):
        resultat = random.randint(1, 6)
        self.resultat_1d6.config(text=f"Résultat: {resultat}")

    def lancer_2d6(self):
        resultat = random.randint(1, 6) + random.randint(1, 6)
        self.resultat_2d6.config(text=f"Résultat: {resultat}")

    def lancer_personnalise(self):
        try:
            nb_des = int(self.nb_des.get())
            nb_faces = int(self.nb_faces.get())
            if nb_des > 0 and nb_faces > 0:
                resultats = [random.randint(1, nb_faces) for _ in range(nb_des)]
                total = sum(resultats)
                self.resultat_personnalise.config(text=f"Résultat: {total} (Détails: {', '.join(map(str, resultats))})")
            else:
                self.resultat_personnalise.config(text="Erreur: Nombres invalides")
        except ValueError:
            self.resultat_personnalise.config(text="Erreur: Entrée invalide")