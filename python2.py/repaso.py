import datetime #tiempo

import  re

#clase para peel nombre de la persona 
class Persona:   
    def __init__(self, nombre):
        self.nombre = nombre
    def getNombre_persona(self):
       print("Su nombre es:",self.nombre)

usuario = Persona(input("Cual es su nombre:"))
     


#clase para el apellido
class Apellido:
    def __init__(self, apellido):
        self.apellido = apellido
    def getapellido_persona(self):
        print("Su apellido es:",self.apellido)

apellidos = Apellido(input("Cual es su apellido:"))


 #clase para calcular la edad      
class nacimiento:
    def __init__(self):
        fecha = input("Introduzca su fecha de nacimiento (en formato dd/mm/yyyy): ")
        self.Nacimiento = datetime.datetime.strptime(fecha, '%d/%m/%Y')
    
    def getNacimiento(self):
        print(self.Nacimiento.strftime('%d/%m/%Y'))
    
    def getEdad(self):
        hoy = datetime.datetime.now()
        edad = hoy.year - self.Nacimiento.year - ((hoy.month, hoy.day) < (self.Nacimiento.month, self.Nacimiento.day))
        print("Fecha de nacimiento:", self.Nacimiento.strftime('%d/%m/%Y'))
        print("Edad:", edad)

fecha_nacimiento = nacimiento()


#clase para el numero celular        
class Celular:
    def __init__(self, celular):
        self.celular = celular
    def getcelular(self):
        print("Su numero telefonico es:",self.celular)

Movil = Celular(input("Cual es su numero de telefono:"))

#clase para la provincia 
class Provincia:
    def __init__(self, estado):
        self.estado = estado
    def getestado(self):
        print("Su Provincia es:",self.estado)
ciudad = Provincia(input("Cual es su Provincia:"))



#correo electronico
class correo_electronico:
    def __init__(self,correo):
        self.correo = correo

    def getcorreo(self):
        print("Su correo es:",self.correo)
    
while True:
    correo = input("Ingrese su correo (obligatorio: @clasepython.com): ")
    if re.search("@clasepython.com", correo):
        Correo = correo_electronico(correo)
        break
    else:
        print("Correo no válido. Por favor, ingrese un correo con terminacion @clasepython.com")


    


        
#imprimir todos los datos 
usuario.getNombre_persona()     
apellidos.getapellido_persona()  
fecha_nacimiento.getEdad()    
Movil.getcelular()
ciudad.getestado()
Correo.getcorreo()
