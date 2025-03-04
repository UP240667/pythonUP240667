print("programa 1")
#Declare your age as integer variable
edad = 18
print (edad)

print("programa 2")
#Declare your height as a float variable
altura = float(1.75)
print ("Tu altura es de:", altura)

print("programa 3")
#Declare a variable that store a complex number
# Complex numbers
print('Complex number: ', 2 + 3j)
print('Multiplying complex numbers: ',(2 + 3j) * (2 - 3j))

print("programa 4")
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle.
base = int(input("ingresa la base"))
haltura = int(input("ingresa la haltura"))
print (base,haltura)
area = (base*haltura/2)

print("programa 5")
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle.
a= int(input("Ingresa el valor a del triangulo"))
b= int(input("Ingresa el balor b de el triangulo"))
c= int(input("ingresa el valor c del triangulo"))
perimetro=(a + b + c)
print ("el perimetro del triangulo es",perimetro)

print("programa 6")
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
Largo=int(input("ingresa el largo de el rectangulo: "))
Ancho=int(input("ingresa el ancho de el rectangulo: "))
area= (Largo*Ancho)
perimetro= (2*(Largo+Ancho))
print("el area del rectangulo es",area)
print("el perimetro de el rectangulo es",perimetro)

print("programa 7")
# Get radius of a circle using prompe Calculate the area and circumference.
radio=int(input("Ingresa el radio del circulo:"))
pi=3.14
area=(pi*radio*radio)
circunferencia=(2*pi*radio)
print("el area del circulo es:",area)
print("la circunferencia del circulo es:",circunferencia)

print("programa 8")
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
pendiente=2
inty=-2
intx=(pendiente/inty)
print("la intx es:",intx)
print("la pendiente es de:",pendiente)

print("progama 9")
#Slope is (m = y2-y1/x2-x1). Find the slope and  between point (2, 2) and point (6,10) 
y1=2
y2=10
x1=2
x2=6
m=(y2-y1)/(x2-x1)
distancia=((x2-x1)**2+(y2-y1)**2)#aqui utilize la formula ecliliana mostrada en el link de la tarea.
print("la pendiente es:",m)
print("la distancia ecliliana es:",distancia)

print("programa10")
#Compare the slopes in tasks 8 and 9.
m1=(y2-y1)/(x2-x1)
m2=2
if m1>m2:
    comparacion="la primera pendiente es mayor"
elif m1 < m2:
    comparacion= "la segunda  pendiente es mayor"
else:
    comparacion="Las dos  pendientes son iguales"
print("pendiente 1:",m1)
print("pendiente 2:",m2)
print("distancia eclidiana:",distancia)
print("el resultado de la comparacion es que:",comparacion)

print("programa11")
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x=int(input("ingresa el valor de x"))
y=(x**2+ 6 + 9 )
print("el valor de y es :",y)

print("programa 12")
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python"))#se puede encontrar el número de elementos de cualquier iterable utilizando la función len
print(len("deagon"))
print("¿los dos tienen la misma longitud")
print(len("python")!=len("dragon"))

print("programa 13")
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print(("on in python,") and ("on in dragon,"))#calculamos si la foncion on es de paiton y si es funcion de dragon tambien.

print("Ejercicio 14")
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("I hope this course is not full ,""jargon,""I hope this course is not full of jargon")

print("Ejercicio 15")
#No hay 'on' tanto en  dragón como en python
print(("on not is found in python") and ("on no is a found in dragon"))

print("Ejercicio 16")
#Encuentre la longitud del texto python y convierta el valor en float y conviértalo en string
longitud=(len("python"))
print(float(longitud))
print(str(longitud))#str es la funcion de string esta sirve para convertir un valor en una cadena .

print("Ejercicio 17")
#Los números pares son divisibles por 2 y el resto es cero. ¿Cómo se comprueba si un número es par o no usando python?
numero=int(input("Ingrese el numero: "))
if numero % 2 == 0:     #el if se utiliza para iniciar una comparacion o operacion y verificar, si esta es verdadera se ejecutara el programa.
     print("el numero es par")
else:print("el numero es inpar")  #el else se utiliza para comprobar y verificar para ejecutar el programa cuandp la respuesta de if es falsa.

print("Ejercicio 18")
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7/3==(int(2.7)))
print(True or False)
print(True("el resultado es verdadero si son enteros"))
print(False("el resultado es falso el resultado no es entero."))

print("Ejercicio 19")
#Check if type of '10' is equal to type of 10
print(type(10)==type(10)) #el tipo de valor lo obtenemos con la funcion type esta nos alluda a determinar su tipo.
True=print("Es verdadero ambos valores son de el mismo tipo")
False=print("es falso los valores no son de el mismo tipo")

print("Ejercicio 20")
#Check if int('9.8') is equal to 10
resultado=(int(9.8)== 10)
fin=(True or False)   #con la funcion int saco el valor entero de un numero flotante o con desimales como en el ejercicio 
print(fin)

print("Ejercicio 21")
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
horas_trabajadas=int(input("ingrese las horas trabajadas: "))
tasa_por_hora=int(input("ingresa la tasa por hora: "))
Ganancias=(horas_trabajadas*tasa_por_hora)
print("Ganancia por el total de horas trabajadas: ",Ganancias)



