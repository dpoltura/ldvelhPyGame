import tkinter as tk
from tkinter import ttk

class FeuilleRencontre(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Titre
        ttk.Label(self, text="Feuille de Rencontre", font=("Arial", 16, "bold")).pack(pady=10)

        # Caractéristiques de l'adversaire
        frame_adv = ttk.LabelFrame(self, text="Adversaire")
        frame_adv.pack(pady=10, padx=10, fill="x")

        caracteristiques = [
            ("Nom", "nom_adv"),
            ("FORCE", "force_adv"),
            ("ENDURANCE", "endurance_adv"),
            ("PSYCHISME", "psychisme_adv"),
            ("RESISTANCE", "resistance_adv"),
            ("DEXTERITE", "dexterite_adv")
        ]

        for i, (nom, var_name) in enumerate(caracteristiques):
            ttk.Label(frame_adv, text=nom).grid(row=i, column=0, sticky="w", padx=5, pady=2)
            setattr(self, var_name, tk.StringVar(value=""))
            ttk.Entry(frame_adv, textvariable=getattr(self, var_name), width=15).grid(row=i, column=1, padx=5, pady=2)

        # Armes de l'adversaire
        frame_armes_adv = ttk.LabelFrame(self, text="Armes de l'adversaire")
        frame_armes_adv.pack(pady=10, padx=10, fill="x")

        self.armes_adv_text = tk.Text(frame_armes_adv, height=3, width=50)
        self.armes_adv_text.pack(padx=5, pady=5)

        # Notes de combat
        frame_notes = ttk.LabelFrame(self, text="Notes de combat")
        frame_notes.pack(pady=10, padx=10, fill="both", expand=True)

        self.notes_combat_text = tk.Text(frame_notes, height=10, width=50)
        self.notes_combat_text.pack(padx=5, pady=5, fill="both", expand=True)

        # Boutons
        ttk.Button(self, text="Nouvelle rencontre", command=self.nouvelle_rencontre).pack(pady=10)

    def nouvelle_rencontre(self):
        for var_name in ["nom_adv", "force_adv", "endurance_adv", "psychisme_adv", "resistance_adv", "dexterite_adv"]:
            getattr(self, var_name).set("")
        self.armes_adv_text.delete("1.0", tk.END)
        self.notes_combat_text.delete("1.0", tk.END)