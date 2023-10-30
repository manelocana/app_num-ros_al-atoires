#importamos
import random
from tkinter import *
import tkinter.messagebox as msg

# ventana
root = Tk()
root.title("Numéros aléatoires") 
root.resizable(False, False)
ancho_ventana = 400
alto_ventana = 100 

# pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()                       
                                                                            # le sacamos el centro dinamico a la pantalla
cordenadas_x = int((ancho_pantalla/2) - (ancho_ventana/2))
cordenadas_y = int((alto_pantalla/2) - (alto_ventana/2))
root.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, cordenadas_x, cordenadas_y))

# mensaje inicio juego
msg.showinfo("Devinez le numéro", "Entrez un numéro de 1 à 100:")

# entrada usuario
entrada = Entry(root)   # la entrada en ventana principal
entrada.insert(0, "Ecrire un numéro: ")    #un input
entrada.bind("<Button-1>", lambda d: entrada.delete(0, END))    # que se borre el text predeterminado al hacer click al raton
entrada.pack()
  
#numero aleatorio
numeros = random.randint(1, 100)        # metodo .randint (aleatorio)
intentos = 0
#print(numeros)

#bucle para dar pistas al usuario
def accion_boton():
    global intentos     # usamos global, ya q la variable esta declarada fuera de la funcion

    try:
        usuario = int(entrada.get())    # usamos el entry/input

        if usuario < numeros:
            msg.showinfo("Essayer à nouveau" , "Le numéro que vous recherchez est plus grand")      # envez de hacer print, llamamos al modulo 
            intentos += 1                                                               # messagebox y hacemos showinfo
                                                                                         
        elif usuario > numeros:
            msg.showinfo("Essayer à nouveau" , "Le numéro que vous recherchez est inférieur")
            intentos += 1

        else:
            msg.showinfo("Olee!", "Tu as deviné!")
            intentos += 1
            msg.showinfo("Tentatives:", "Tu as essayé {} fois".format(intentos))
            
    except:
        msg.showerror("Erreur", "Caractére non valide")

#botones
boton =  Button(root, text="Envoyer", command=accion_boton).pack()

# bucle ventana principal
root.mainloop()