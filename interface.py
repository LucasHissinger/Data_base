from tkinter import *
from tkinter import font
from functools import partial
import Projet
import sqlite3

conn = sqlite3.connect('BDD.db')

class Fenetre:
    def __init__(self, size):
        self.root = Tk()
        self.root.geometry(size)
        self.root.resizable(False, False)

    def create_buttons(self):
        List_Button_Name = [
                            ["Insérer", Projet.inserer],
                            ["Mettre à jour", Projet.maj],
                            ["Afficher", Projet.afficher_table],
                            ["Moyenne des prix des livres", Projet.moyenne_livre],
                            ["Livres filtrés selon genre", Projet.livre_genre],
                            ["Livres empruntés", Projet.livre_emprunte],
                            ["Emprunter un livre", Projet.emprunter_livre],
                            ["Restituer un livre", Projet.restituer_livre],
                            ["Emprunteurs et livres empruntés", Projet.livre_emprunte_et_emprunteur],
                            ["Le(s) livre(s) le(s) plus emprunté(s)", Projet.livre_plus_emprunte]
                           ]
        for i in List_Button_Name:

            Bouton = Button(self.root, text = i[0], font = ("Courier", 20), bg = "#C0C0C0", command = partial(i[1], conn))
            Bouton.pack(fill = 'x', ipady = 2, pady = 2)

fenetre = Fenetre("650x600")
fenetre.create_buttons()
fenetre.root.mainloop()

conn.close()

