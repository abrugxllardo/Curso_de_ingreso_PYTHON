#Abril gallardo
'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''

import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        respuesta = "Si"
        bandera_vot = True
        
        acumulador_edad = 0
        contador_candidatos = 0
        acumulador_votos = 0
        


        while respuesta != None:
            candidatos = prompt("Tp 6", prompt="Ingrese su nombre")
            while candidatos.isalpha() == False or candidatos == None or len(candidatos) < 2 or candidatos == "":
                candidatos = prompt("Tp 6", prompt="Error. Ingrese el nombre de algun candidato")

            edad = prompt(title="Tp6", prompt= "Ingrese su edad")
            while edad == None or edad.isdigit() == False or int(edad) < 25 or edad == "":
                edad = int(prompt(title="Tp6", prompt= "Error. Ingrese su edad nuevamente"))

            votos = prompt(title="Tp6", prompt= "Ingrese la cantidad de votos")
            while votos == None or votos.isdigit() == False or int(votos) < 1 or votos == "":
                votos = int(prompt(title="Tp6", prompt= "Error. Ingrese su edad nuevamente"))
            
            if bandera_vot or votos > mas_votos:
                mas_votos = votos
                nombre_mas_votos = candidatos
            if bandera_vot or votos < min_votos:
                min_votos = votos
                nombre_menos_votos = candidatos
                edad_mas_votos = edad
                bandera_vot = False

            contador_candidatos += 1
            acumulador_edad += int(edad)
            acumulador_votos += int(votos)

            respuesta = prompt(title="Tp6", prompt=("Desea continuar?"))

            promedio_edades = acumulador_edad / contador_candidatos

            print(f"Candidato con mas votos: {nombre_mas_votos}\n Candidato con menos votos: {nombre_menos_votos}, su edad: {edad_mas_votos}\n Promedio edades: {promedio_edades}\n Total votos emitidos: {acumulador_votos}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
