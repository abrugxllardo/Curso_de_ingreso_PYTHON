import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"Abril Gallardo"
'''
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        """ estaciones = self.combobox_estaciones.get()
        destinos = self.combobox_destino.get()
        precio_estadia = 15000
        

        match estaciones:
            case "Invierno":
                if destinos == "Bariloche":
                    aumento = 20
                elif destinos == "Cataratas" or destinos == "Cordoba":
                    descuento = 10
                else:
                    descuento = 20
            case "Verano":
                if destinos == "Bariloche":
                    descuento = 20
                elif destinos == "Cataratas" or destinos == "Cordoba":
                    aumento = 10
                else:
                    aumento = 20
            case _:
                if destinos != "Cordoba":
                    aumento = 10

        precio_descuento = precio_estadia - (precio_estadia * descuento / 100)
        precio_aumento = precio_estadia + (precio_estadia * aumento / 100)

        alert(title="Ejercicio 9", message= f"El precio total con descuento es: {precio_descuento}")
        alert(title="Ejercicio 9", message= f"El precio total con aumento es: {precio_aumento}") """
            
        estaciones = self.combobox_estaciones.get()
        destinos = self.combobox_destino.get()
        precio_estadia = 15000
        

        match estaciones:
            case "Invierno":
                if destinos == "Bariloche":
                    precio_total = precio_estadia + (precio_estadia * 20 /100)
                    mensaje = f"El precio total es de: {precio_total}"
                elif destinos == "Cataratas" or destinos == "Cordoba":
                    precio_total = precio_estadia - (precio_estadia * 10 /100)
                    mensaje = f"El precio total es de: {precio_total}"
                else:
                    precio_total = precio_estadia - (precio_estadia * 20 /100)
                    mensaje = f"El precio total es de: {precio_total}"
            case "Verano":
                if destinos == "Bariloche":
                    precio_total = precio_estadia - (precio_estadia * 20 /100)
                    mensaje = f"El precio total es de: {precio_total}"
                elif destinos == "Cataratas" or destinos == "Cordoba":
                    precio_total = precio_estadia + (precio_estadia * 10 /100)
                    mensaje = f"El precio total es de: {precio_total}"
                else:
                    precio_total = precio_estadia + (precio_estadia * 20 /100)
                    mensaje = f"El precio total es de: {precio_total}"
            case _:
                if destinos != "Cordoba":
                    precio_total = precio_estadia + (precio_estadia * 10 /100)
                    mensaje = f"El precio total es de: {precio_total}"
                else:
                    precio_total = precio_estadia
                    mensaje = f"El precio total es de: {precio_total}"

        alert(title= "Ejercicio 9", message= mensaje)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()