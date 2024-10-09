import tkinter as tk
from tkinter import ttk
import random

class LancerDesSimple(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Lancer de Dés", font=("Arial", 12, "bold")).pack(pady=5)

        frame_1d6 = ttk.Frame(self)
        frame_1d6.pack(fill="x", padx=5, pady=2)
        ttk.Button(frame_1d6, text="1D6", command=lambda: self.lancer_des(1, 6)).pack(side="left")
        self.resultat_1d6 = ttk.Label(frame_1d6, text="")
        self.resultat_1d6.pack(side="left", padx=5)

        frame_2d6 = ttk.Frame(self)
        frame_2d6.pack(fill="x", padx=5, pady=2)
        ttk.Button(frame_2d6, text="2D6", command=lambda: self.lancer_des(2, 6)).pack(side="left")
        self.resultat_2d6 = ttk.Label(frame_2d6, text="")
        self.resultat_2d6.pack(side="left", padx=5)

    def lancer_des(self, nombre, faces):
        resultats = [random.randint(1, faces) for _ in range(nombre)]
        total = sum(resultats)
        if nombre == 1:
            self.resultat_1d6.config(text=f"Résultat: {total}")
        else:
            self.resultat_2d6.config(text=f"Résultat: {total} ({'+'.join(map(str, resultats))})")