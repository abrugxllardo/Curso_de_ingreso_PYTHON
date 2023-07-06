import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random


'''
nombre: Abril
apellido:Gallardo
---
Ejercicio: instrucion_if_09
---
Al presionar el botón  'Calcular', se deberá mostrar (utilizando el Dialog alert) un número
aleatorio entre el 1 y el 10 inclusive
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        import random
        num_random = random.randint(1, 10)
        alert(title= "Ejercicio 9", message= num_random)
        

#RANDOM
#genera numeros aleatorios

# import random

# random_float = random.random()
# print(random_float)
#Solo entre cero y uno 
#flotante

# random_int = random.randint(1, 6)
# print("El resultado del dado es: ", random_int)
#numeros enteros

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()