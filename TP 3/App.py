from tkinter import *

fenetre = Tk()
fenetre.title("TP 3")
fenetre.geometry("200x200")

def calculer():
    long = int(entry_longueur.get())
    larg = int(entry_largeur.get())
    res = long * larg
    label_resultat.config(text = "L'aire du rectangle est " + str(res) + " cm²")


label_longueur = Label(fenetre, text = "Longueur : ")
label_longueur.place(x = 20, y = 10)

label_largeur = Label(fenetre, text = "Largeur : ")
label_largeur.place(x = 20, y = 40)

entry_longueur = Entry(fenetre, bg = "white")
entry_longueur.place(x = 100, y = 10, width = 50)

entry_largeur = Entry(fenetre, bg = "white")
entry_largeur.place(x = 100, y = 40, width = 50)

label_longueur_cm = Label(fenetre, text = "cm")
label_longueur_cm.place(x = 160, y = 10)

label_largeur_cm = Label(fenetre, text = "cm")
label_largeur_cm.place(x = 160, y = 40)

button_calculer = Button(fenetre, text = "CALCULER", command = calculer)
button_calculer.place(x = 60, y = 70, width = 80, height = 20)

label_resultat = Label(fenetre, text = "L'aire du rectangle est 0 cm²")
label_resultat.place(x = 20, y = 100, width = 160)

fenetre.mainloop()