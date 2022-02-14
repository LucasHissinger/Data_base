import sqlite3

List_Table = [
              ["Titre", "Prix", "Id_genre", "Id_editeur"],
              ["Nom_editeur", "Pays_editeur", "Adresse_editeur"],
              ["Nom_auteur", 'Prenom_auteur', "Pays_auteur"],
              ["Categorie"],
              ["Nom_emprunteur", "Prenom_emprunteur", "Nombre_livre_emprunte"],
              ["Id_livre", "Id_auteur"],
              ["Id_livre", "Id_emprunteur", "Emprunt_date_debut", "Statut"]
             ]

List_Script = [
                """INSERT INTO Livre(Titre, Prix, Id_genre, Id_editeur) VALUES(?, ?, ?, ?)""",
                """INSERT INTO Editeur(Nom_editeur, Pays_editeur, Adresse_editeur) VALUES(?, ?, ?)""",
                """INSERT INTO Auteur(Nom_auteur, Prenom_auteur, Pays_auteur) VALUES(?, ?, ?)""",
                """INSERT INTO Genre(Categorie) VALUES(?)""",
                """INSERT INTO Emprunteur(Nom_emprunteur, Prenom_emprunteur, Nombre_livre_emprunte) VALUES(?, ?, ?)""",
                """INSERT INTO Ecrit_par(Id_livre, Id_auteur) VALUES(?, ?)""",
                """INSERT INTO Emprunter_par(Id_livre, Id_emprunteur, Emprunt_date_debut, Statut) VALUES(?, ?, ?, ?)"""
              ]

List_UpdateScript = [
                     """UPDATE Livre SET Titre = ?, Prix = ?, Id_genre = ?, Id_editeur = ? WHERE Id_livre = ?""",
                     """UPDATE Editeur SET Nom_editeur = ?, Pays_editeur = ?, Adresse_editeur = ? WHERE Id_editeur = ?""",
                     """UPDATE Auteur SET Nom_auteur = ?, Prenom_auteur = ?, Pays_auteur = ? WHERE Id_auteur = ?""",
                     """UPDATE Genre SET Categorie = ? WHERE Id_genre = ?""",
                     """UPDATE Emprunteur SET Nom_emprunteur = ?, Prenom_emprunteur = ?, Nombre_livre_emprunte = ? WHERE Id_emprunteur = ?""",
                     """UPDATE Emprunter_par SET Emprunt_date_debut = ?, Statut = ? WHERE Id_livre = ? AND Id_emprunteur = ?""",
                    ]

List_AffScript = [
                """SELECT * FROM Livre""",
                """SELECT * FROM Editeur""",
                """SELECT * FROM Auteur""",
                """SELECT * FROM Genre""",
                """SELECT * FROM Emprunteur""",
                """SELECT * FROM Ecrit_par""",
                """SELECT * FROM Emprunter_par"""
              ]

'''----------------------------------------------------------------------'''

def afficher(cursor, choice_user_table):

    cursor.execute(List_AffScript[choice_user_table])

    print("\n\n\n")
    for i in cursor.fetchall():
        print(i)

'''----------------------------------------------------------------------'''

def afficher_table(conn):

    choice_user_table = input("0: Livre\n 1: Editeur\n 2: Auteur\n 3: Genre\n 4: Emprunteur\n 5: Ecrit_par\n 6: Emprunter_par")
    while choice_user_table not in [str(i) for i in range(7)]:
        choice_user_table = input("0: Livre\n 1: Editeur\n 2: Auteur\n 3: Genre\n 4: Emprunteur\n 5: Ecrit_par\n 6: Emprunter_par")
    choice_user_table = int(choice_user_table)

    afficher(conn.cursor(), choice_user_table)


'''----------------------------------------------------------------------'''

def choose_id(cursor, choice_user_table):

    afficher(cursor, choice_user_table)

    cursor.execute(List_AffScript[choice_user_table])

    List_id = [str(i[0]) for i in cursor.fetchall()]
    choice_user_id = input("Quelle id ? : ")

    while choice_user_id not in List_id:
        choice_user_id = input("Quelle id ? : ")

    return int(choice_user_id)

'''----------------------------------------------------------------------'''

def inserer(conn):

    cursor = conn.cursor()

    choice_user_table = input("0: Livre\n 1: Editeur\n 2: Auteur\n 3: Genre\n 4: Emprunteur\n 5: Ecrit_par\n 6: Emprunter_par")
    while choice_user_table not in [str(i) for i in range(7)]:
        choice_user_table = input("0: Livre\n 1: Editeur\n 2: Auteur\n 3: Genre\n 4: Emprunteur\n 5: Ecrit_par\n 6: Emprunter_par")
    choice_user_table = int(choice_user_table)

    List_choix = []

    for i in List_Table[choice_user_table]:
        message = "Entrer : " + i
        List_choix.append(str(input(message)))


    cursor.execute(List_Script[choice_user_table], tuple(List_choix))
    conn.commit()

'''----------------------------------------------------------------------'''

def maj(conn):

    cursor = conn.cursor()

    action = input("0: Supprimer\n 1: Modifier")
    while action not in ["0", "1"]:
        action = input("0: Supprimer\n 1: Modifier")
    action = int(action)

    choice_user_table = input("0: Livre\n 1: Editeur\n 2: Auteur\n 3: Genre\n 4: Emprunteur\n  5: Ecrit_par" if action == 0 else "0: Livre\n 1: Editeur\n 2: Auteur\n 3: Genre\n 4: Emprunteur\n 5: Emprunter_par" )
    while choice_user_table not in [str(i) for i in range(5 if action == 0 else 7)]:
        choice_user_table = input("0: Livre\n 1: Editeur\n 2: Auteur\n 3: Genre\n 4: Emprunteur\n  5: Ecrit_par" if action == 0 else "0: Livre\n 1: Editeur\n 2: Auteur\n 3: Genre\n 4: Emprunteur\n 5: Emprunter_par" )
    choice_user_table = int(choice_user_table)

    if action == 0:

        supprimer(conn, choice_user_table)

    else:

        modifier(conn, choice_user_table if choice_user_table != 5 else 6)

#--------------------------------------------------------------------------#

def modifier(conn, choice_user_table):

    cursor = conn.cursor()
    choice_user_id = choose_id(cursor, choice_user_table)

    if choice_user_table == 6:

        cursor.execute("""SELECT * FROM Emprunter_par WHERE Id_livre = ?""", str(choice_user_id))
        print("\n\n\n")
        List_id_emprunteur = []
        for i in cursor.fetchall():
            List_id_emprunteur.append(str(i[1]))
            print(i)

        choice_user_emprunteur = input("Quel emprunteur ?")
        while choice_user_emprunteur not in List_id_emprunteur:
            choice_user_emprunteur = input("Quel emprunteur ?")
        choice_user_emprunteur = int(choice_user_emprunteur)


        List_choix = []
        for i in List_Table[6][2:]:
            message = "Entrer : " + i
            List_choix.append(str(input(message)))


        List_choix.append(str(choice_user_id))
        List_choix.append(str(choice_user_emprunteur))
        cursor.execute(List_UpdateScript[5], tuple(List_choix))

    else:

        List_choix = []
        for i in List_Table[choice_user_table]:
            message = "Entrer : " + i
            List_choix.append(str(input(message)))

        List_choix.append(str(choice_user_id))
        cursor.execute(List_UpdateScript[choice_user_table], tuple(List_choix))

    conn.commit()

#--------------------------------------------------------------------------#

def supprimer(conn, choice_user_table):

    cursor = conn.cursor()

    choice_user_id = choose_id(cursor, choice_user_table)

    List_DelScript = [
                """DELETE FROM Livre WHERE Id_livre = ?""",
                """DELETE FROM Editeur WHERE Id_editeur = ?""",
                """DELETE FROM Auteur WHERE Id_auteur = ?""",
                """DELETE FROM Genre WHERE Id_genre = ?""",
                """DELETE FROM Emprunteur WHERE Id_Emprunteur = ?""",
              ]

    cursor.execute(List_DelScript[choice_user_table], str(choice_user_id))
    conn.commit()

'''----------------------------------------------------------------------'''

def moyenne_livre(conn):

    cursor = conn.cursor()
    cursor.execute("""SELECT AVG(Prix) FROM Livre""")
    print("Moyenne prix des livres : " + str(round(cursor.fetchone()[0], 2)) + "€")

'''----------------------------------------------------------------------'''

def livre_genre(conn):

    cursor = conn.cursor()
    afficher(cursor, 3)

    cursor.execute("""SELECT Id_genre FROM Genre""")
    List_id_genre = [str(i[0]) for i in cursor.fetchall()]
    choice_user = input("Quel genre ?(écrire id)")
    while choice_user not in List_id_genre:
        choice_user = input("Quel genre ?(écrire id)")



    cursor.execute("""SELECT * FROM Livre WHERE Id_genre = ?""", choice_user)
    for i in cursor.fetchall():
        print(i)

'''----------------------------------------------------------------------'''

def livre_emprunte(conn):

    cursor = conn.cursor()

    cursor.execute("""SELECT Livre.Id_livre, Titre, Prix, Id_genre, Id_editeur FROM Livre JOIN Emprunter_par ON Livre.Id_livre = Emprunter_par.Id_livre WHERE Emprunter_par.Statut = 1""")
    for i in cursor.fetchall():
        print(i)

'''----------------------------------------------------------------------'''

def emprunter_livre(conn):

    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM Livre EXCEPT SELECT Livre.Id_livre, Titre, Prix, Id_genre, Id_editeur FROM Livre JOIN Emprunter_par ON Livre.Id_livre = Emprunter_par.Id_livre WHERE Emprunter_par.Statut = 1""")
    List_id_livre = []
    for i in cursor.fetchall():
        List_id_livre.append(str(i[0]))
        print(i)



    choice_user_livre = input("Quel livre voulez-vous emprunter ?(écrire id)")
    while choice_user_livre not in List_id_livre:
        choice_user_livre = input("Quel livre voulez-vous emprunter ?(écrire id)")

    afficher(cursor, 4)
    cursor.execute("""SELECT Id_emprunteur FROM Emprunteur""")
    List_id_emprunteur = [str(i[0]) for i in cursor.fetchall()]
    choice_user_emprunteur = input("Quel emprunteur êtes-vous ?(écrire id)")
    while choice_user_emprunteur not in List_id_emprunteur:
        choice_user_emprunteur = input("Quel emprunteur êtes-vous ?(écrire id)")


    choice_user_date = input("Quelle Date ? (YYYY/MM/DD)")
    while [choice_user_date[4], choice_user_date[7]] != ["/", "/"] or choice_user_date[:4] not in [str(1995 + i) for i in range(27)] or choice_user_date[5:7] not in [str(i) if i>9 else "0" + str(i) for i in range(13)] or choice_user_date[8:] not in [str(i) if i>9 else "0" + str(i) for i in range(32)]:
        choice_user_date = input("Quelle Date ? (YYYY/MM/DD)")

    emprunte = [choice_user_livre, choice_user_emprunteur, choice_user_date]

    choice_user_table = 6
    cursor.execute("""SELECT * FROM Emprunter_par WHERE Id_livre = ? AND Id_Emprunteur = ?""", (emprunte[0], emprunte[1]))
    result_statut = cursor.fetchone()
    cursor.execute("""SELECT Nombre_livre_emprunte FROM Emprunteur WHERE Id_emprunteur = ?""", (emprunte[1]))
    result_nombre_livre = cursor.fetchone()
    if result_nombre_livre[0] <= 2:
        if result_statut != None:
            if result_statut[3] == 0:
                cursor.execute("""UPDATE Emprunter_par SET Statut = 1 WHERE Id_livre = ? AND Id_emprunteur = ?""", (emprunte[0], [emprunte[1]]))
            else:
                print("Vous avez déjà ce livre !!")
            return
        else:
            List_choix = [emprunte[0], emprunte[1], emprunte[2], 1]
            cursor.execute("""UPDATE Emprunteur SET Nombre_livre_emprunte = Nombre_livre_emprunte + 1 WHERE Id_emprunteur = ?""", (emprunte[1]))
    else:
        print("Vous ne pouvez plus emprunter de livre pour l'instant !! max 3")
        return

    cursor.execute("""INSERT INTO Emprunter_par(Id_livre, Id_emprunteur, Emprunt_date_debut, Statut) VALUES(?, ?, ?, ?)""", tuple(List_choix))
    conn.commit()

'''----------------------------------------------------------------------'''

def restituer_livre(conn):

    cursor = conn.cursor()
    afficher(cursor, 4)
    cursor.execute("""SELECT Id_emprunteur FROM Emprunteur""")
    List_id_emprunteur = [str(i[0]) for i in cursor.fetchall()]
    choice_user_emprunteur = input("Quel emprunteur êtes-vous ?(écrire id)")
    while choice_user_emprunteur not in List_id_emprunteur:
        choice_user_emprunteur = input("Quel emprunteur êtes-vous ?(écrire id)")

    cursor.execute("""SELECT Livre.Id_livre, Titre, Prix FROM Emprunter_par JOIN Livre On Emprunter_par.Id_livre = Livre.Id_livre WHERE Id_emprunteur = ? AND Statut = 1""", (choice_user_emprunteur))
    List_id_livre = []
    for i in cursor.fetchall():
        List_id_livre.append(str(i[0]))
        print(i)

    choice_user_livre = input("Quel livre voulez-vous restituer ?(écrire id)")
    while choice_user_livre not in List_id_livre:
        choice_user_livre = input("Quel livre voulez-vous restituer ?(écrire id)")

    cursor.execute("""UPDATE Emprunter_par SET Statut = 0 WHERE Id_emprunteur = ? AND Id_livre = ?""", (choice_user_emprunteur, choice_user_livre))
    conn.commit()
    cursor.execute("""UPDATE Emprunteur SET Nombre_livre_emprunte = Nombre_livre_emprunte - 1 WHERE Id_emprunteur = ?""", (choice_user_emprunteur))
    conn.commit()

'''----------------------------------------------------------------------'''

def livre_emprunte_et_emprunteur(conn):

    cursor = conn.cursor()

    cursor.execute("""SELECT  Titre, Nom_emprunteur, Prenom_emprunteur FROM Emprunteur JOIN Emprunter_par ON Emprunteur.Id_Emprunteur = Emprunter_par.Id_Emprunteur JOIN Livre ON Emprunter_par.Id_livre = Livre.Id_livre WHERE Emprunter_par.Statut = 1""")
    for i in cursor.fetchall():
        print(i)

'''----------------------------------------------------------------------'''

def livre_plus_emprunte(conn):

    cursor = conn.cursor()
    cursor.execute("""SELECT Id_livre, Titre, MAX(count) FROM (SELECT Livre.Id_livre AS Id_livre, Titre AS Titre, COUNT(*) AS count FROM Emprunter_par JOIN Livre ON Emprunter_par.Id_livre = Livre.Id_livre GROUP BY Livre.Id_livre)""")
    for i in cursor.fetchall():
        print(i)