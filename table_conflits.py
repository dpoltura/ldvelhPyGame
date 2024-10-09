import tkinter as tk
from tkinter import ttk

class TableConflits(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Table des Conflits", font=("Arial", 16, "bold")).pack(pady=10)

        # Création de la table
        frame_table = ttk.Frame(self)
        frame_table.pack(pady=10, padx=10)

        # En-têtes de colonnes
        ttk.Label(frame_table, text="Att/Def").grid(row=0, column=0)
        for i in range(1, 11):
            ttk.Label(frame_table, text=str(i)).grid(row=0, column=i)

        # En-têtes de lignes et valeurs
        for i in range(1, 11):
            ttk.Label(frame_table, text=str(i)).grid(row=i, column=0)
            for j in range(1, 11):
                value = min(max(i + j - 7, 1), 12)
                ttk.Label(frame_table, text=str(value)).grid(row=i, column=j)

        # Explication
        explication = """
        Pour utiliser la Table des Conflits :
        1. Trouvez la FORCE de l'attaquant dans la colonne de gauche.
        2. Trouvez la FORCE du défenseur dans la ligne du haut.
        3. L'intersection donne le chiffre à obtenir ou dépasser avec 2D6 pour réussir l'attaque.
        """
        ttk.Label(self, text=explication, wraplength=500, justify="left").pack(pady=20)

        # Calculateur
        frame_calc = ttk.LabelFrame(self, text="Calculateur")
        frame_calc.pack(pady=10, padx=10, fill="x")

        ttk.Label(frame_calc, text="FORCE Attaquant:").grid(row=0, column=0, padx=5, pady=5)
        self.force_att = tk.StringVar()
        ttk.Entry(frame_calc, textvariable=self.force_att, width=5).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_calc, text="FORCE Défenseur:").grid(row=1, column=0, padx=5, pady=5)
        self.force_def = tk.StringVar()
        ttk.Entry(frame_calc, textvariable=self.force_def, width=5).grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(frame_calc, text="Calculer", command=self.calculer).grid(row=2, column=0, columnspan=2, pady=10)

        self.resultat = tk.StringVar()
        ttk.Label(frame_calc, textvariable=self.resultat).grid(row=3, column=0, columnspan=2, pady=5)

    def calculer(self):
        try:
            att = int(self.force_att.get())
            def_ = int(self.force_def.get())
            if 1 <= att <= 10 and 1 <= def_ <= 10:
                resultat = min(max(att + def_ - 7, 1), 12)
                self.resultat.set(f"Résultat: {resultat}")
            else:
                self.resultat.set("Les valeurs doivent être entre 1 et 10")
        except ValueError:
            self.resultat.set("Veuillez entrer des nombres valides")