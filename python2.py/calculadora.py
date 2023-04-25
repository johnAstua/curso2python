def restar(a, b):  #funcion para restar 2 numeros elegidos por el usuario
    return a - b
    
def division(a, b): #funcion para dividir 2 numeros elegidos por el usuario
    return (a / b)

def tabla_multiplicar(numero, rango): #funcion para hacer una tabla de multiplicar
    print(f"Tabla de multiplicar del {numero}:") #imprime de cual numero es la tabla de multiplicar
    for i in range(rango + 1): #es para el rango desde el 0 hasta el numero seleccionado
        resultado = numero * i #esto es para que se vayan haciendo las multiplicaciones de la tabla 
        print(f"{numero} * {i} = {resultado}") #imprime la tabla hasta el numero elegido 
    

#interfaz
eleccion = 0 #la eleccion no a sido realizada

while eleccion != 5: #tiene que ser un numero del 1 al 5  
    print("""
        Calculadora

Indique la operacion a realizar  

1)Suma         
2)Resta  
3)Division
4)Funcion tabla
5)Salir        
""")
#suma de dos digitos
    eleccion =int(input()) #convierte el numero en un entero para selecionar una de las opciones 

    if eleccion == 1: #si la eleccion es 1
        suma = 0 #la suma no ha sido realizada
        suma_numero1 = int(input("Ingrese el primer numero:")) #primer numero para sumar
        suma_numero2 =int(input("iIngrese el segundo numero:")) #segundo numero para sumar
        suma_final = suma_numero1 + suma_numero2 #se realiza la suma entre los 2 numeros ingresados 
        print(f"{suma_numero1} + {suma_numero2} = {suma_final} ") #se imprime el procedimiento y el resultado
                         
#resta de dos digitos
    if eleccion ==2: #si la eleccion es 2
        resta_numero1 = int(input("Ingrese el primer numero:")) #primer numero para restar
        resta_numero2 = int(input("Ingrese el segundo numero:"))#segundo numero para restar
        print(f"{resta_numero1} - {resta_numero2} =", restar(resta_numero1, resta_numero2)) #se imprime el procedimiento y el resultado

#division de dos digitos
    if eleccion == 3: #si la eleccion es 3
        division_numero1 = int(input("Ingrese el primer numero:")) #primer numero para la division 
        division_numero2 = int(input("Dividido entre:")) #el primer numero dividido entre 
        print(f"{division_numero1} ÷ {division_numero2} =", division(division_numero1, division_numero2)) #imprime el procedimiento y el resultado 

#funcion tabla 
    if eleccion == 4: #si la eleccion es 4
        tabla_numero = int(input("Ingrese el número para la tabla de multiplicar: ")) #se ingresa de que numero es la tabla de multiplicar
        tabla_rango = int(input("Ingrese el rango de multiplicación: ")) #se ingresa hasta que numero debe de llegar la tabla del numero seleccionado 
        tabla_multiplicar(tabla_numero, tabla_rango) #imprime la tabla 

#salir
    if eleccion == 5: #si el usuario ingresa 5 saldra de la calculadora 
        print("apagada") 
        break #termina el bucle 