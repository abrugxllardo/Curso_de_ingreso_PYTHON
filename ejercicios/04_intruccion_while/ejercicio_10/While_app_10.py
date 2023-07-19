import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

#Abril Gallardo
'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        respuesta = "Si"
        acumulador_positivos = 0
        acumulador_negativos = 0
        contador_negativos = 0
        contador_positivos = 0
        contador_ceros = 0

        while respuesta != None:
            numero = int(prompt(title= "Ejercicio 10", prompt= "Ingrese un numero"))
            if numero > 0:
                acumulador_positivos += numero
                contador_positivos += 1
            elif numero < 0:
                acumulador_negativos += numero
                contador_negativos += 1
            else:
                contador_ceros += 1

            diferencia = contador_positivos - contador_negativos

            respuesta = prompt(title= "Ejercicio 10", prompt= "Desea continuar?")

        alert(title="Ejercicio 10", message= f"La suma acumulada de los negativos: {acumulador_negativos}\nLa suma acumulada de los positivos:{acumulador_positivos}\nCantidad de números positivos ingresados: {contador_positivos}\nCantidad de números negativos ingresados: {contador_negativos}\nCantidad de ceros: {contador_ceros}\nDiferencia entre la cantidad de los números positivos ingresados y los negativos: {diferencia}")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
