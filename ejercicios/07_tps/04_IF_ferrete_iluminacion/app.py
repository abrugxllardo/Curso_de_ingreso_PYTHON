import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

"ABRIL GALLARDO"
'''
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        """ cant_lamparas = int(self.combobox_cantidad.get())
        marca = self.combobox_marca.get()
        importe = cant_lamparas * 800

        if cant_lamparas >= 6:
            porcentaje = importe * 50 /100
            descuento = importe - porcentaje
            mensaje = f"El total a pagar es: {descuento}"
        elif cant_lamparas == 5 and marca == "ArgentinaLuz":
            porcentaje = importe * 40 / 100
            descuento = importe - porcentaje
            mensaje = f"El total a pagar es: {descuento}"
        elif cant_lamparas == 5 and marca != "ArgentinaLuz":
            porcentaje = importe * 30 / 100
            descuento = importe - porcentaje
            mensaje = f"El total a pagar es: {descuento}"
        elif cant_lamparas == 4 and marca == "ArgentinaLuz" or marca == "FelipeLamparas":
            porcentaje = importe * 25 /100
            descuento = importe - porcentaje
            mensaje = f"El total a pagar es: {descuento}"
        elif cant_lamparas == 4 and marca == "JeLuz" or marca == "HazIluminacion" or marca == "Osram":
            porcentaje = importe * 20 /100
            descuento = importe - porcentaje
            mensaje = f"El total a pagar es: {descuento}"
        elif cant_lamparas == 3 and marca == "ArgentinaLuz":
            porcentaje = importe * 15 /100
            descuento = importe - porcentaje
            mensaje = f"El total a pagar es: {descuento}"
        elif cant_lamparas == 3 and marca == "FelipeLamparas":
            porcentaje = importe * 10 /100
            descuento = importe - porcentaje
            mensaje = f"El total a pagar es: {descuento}"
        elif cant_lamparas == 3 and marca == "JeLuz" or marca == "HazIluminacion" or marca == "Osram":
            porcentaje = importe * 5 /100
            descuento = importe - porcentaje
            mensaje = f"El total a pagar es: {descuento}"
        
        if descuento >= 4000:
            desc_adicional = descuento * 5 /100
            total = descuento - desc_adicional
            mensaje = f"El total a pagar con el descuento adicional es: {total}"

        alert(title= "Trabajo Practico 4", message= mensaje) """
            



        cant_lamparas = int(self.combobox_cantidad.get())
        marca = self.combobox_marca.get()
        importe = cant_lamparas * 800

        match cant_lamparas:
            case 1 | 2:
                porcentaje = 1
            case 5:
                match marca:
                    case "ArgentinaLuz":
                        porcentaje = 0,6
                    case _:
                        porcentaje = 0,7
            case 4:
                match marca:
                    case "ArgentinaLuz" | "FelipeLamparas":
                        porcentaje = 0,75
                    case _:
                        porcentaje = 0,8
            case 3: 
                match marca:
                    case "ArgentinaLuz":
                        porcentaje = 0,85
                    case "FelipeLamparas":
                        porcentaje = 0,9
                    case _:
                        porcentaje = 0,95
            case _:
                porcentaje = 0,5

        precio_final =  importe * porcentaje 

        if precio_final >= 4000:
            desc_adicional = precio_final * 5 /100
            total = precio_final - desc_adicional
            mensaje = f"El total a pagar con el descuento adicional es: {total}"

        alert(title= "Tp 4", message= mensaje)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()