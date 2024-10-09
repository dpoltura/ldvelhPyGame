import tkinter as tk
from tkinter import ttk
import json

class FeuilleAventureSimple(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.fichier_sauvegarde = "feuille_aventure.json"
        self.create_widgets()
        self.charger_donnees()

    def create_widgets(self):
        ttk.Label(self, text="Feuille d'Aventure", font=("Arial", 12, "bold")).pack(pady=5)

        caracteristiques = [
            ("FORCE", "force"),
            ("ENDURANCE", "endurance"),
            ("PSYCHISME", "psychisme"),
            ("RESISTANCE", "resistance"),
            ("DEXTERITE", "dexterite")
        ]

        for nom, var_name in caracteristiques:
            frame = ttk.Frame(self)
            frame.pack(fill="x", padx=5, pady=2)
            ttk.Label(frame, text=nom).pack(side="left")
            entry = ttk.Entry(frame, width=5)
            entry.pack(side="right")
            entry.bind("<KeyRelease>", self.sauvegarder_donnees)
            setattr(self, var_name, entry)

        ttk.Label(self, text="Équipement").pack(pady=5)
        self.equip_text = tk.Text(self, height=5, width=25)
        self.equip_text.pack(padx=5, pady=2)
        self.equip_text.bind("<KeyRelease>", self.sauvegarder_donnees)

        ttk.Label(self, text="Armes").pack(pady=5)
        self.armes_text = tk.Text(self, height=5, width=25)
        self.armes_text.pack(padx=5, pady=2)
        self.armes_text.bind("<KeyRelease>", self.sauvegarder_donnees)

    def get_values(self):
        return {
            "force": self.force.get(),
            "endurance": self.endurance.get(),
            "psychisme": self.psychisme.get(),
            "resistance": self.resistance.get(),
            "dexterite": self.dexterite.get(),
            "equipement": self.equip_text.get("1.0", tk.END),
            "armes": self.armes_text.get("1.0", tk.END)
        }

    def set_values(self, values):
        self.force.delete(0, tk.END)
        self.force.insert(0, values["force"])
        self.endurance.delete(0, tk.END)
        self.endurance.insert(0, values["endurance"])
        self.psychisme.delete(0, tk.END)
        self.psychisme.insert(0, values["psychisme"])
        self.resistance.delete(0, tk.END)
        self.resistance.insert(0, values["resistance"])
        self.dexterite.delete(0, tk.END)
        self.dexterite.insert(0, values["dexterite"])
        self.equip_text.delete("1.0", tk.END)
        self.equip_text.insert("1.0", values["equipement"])
        self.armes_text.delete("1.0", tk.END)
        self.armes_text.insert("1.0", values["armes"])

    def sauvegarder_donnees(self, event=None):
        values = self.get_values()
        with open(self.fichier_sauvegarde, 'w') as f:
            json.dump(values, f)

    def charger_donnees(self):
        try:
            with open(self.fichier_sauvegarde, 'r') as f:
                values = json.load(f)
                self.set_values(values)
        except FileNotFoundError:
            pass  # Fichier non trouvé, on utilise les valeurs par défaut