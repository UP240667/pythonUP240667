print("Ejercicio 1")
#Concatene la cadena 'Thirty', 'Days', 'Of', 'Python' en una sola cadena, 'Thirty Days Of Python'
primer_adena="Thirty"
segunda_cadena=" Days "  #la concatenacion de cadenas es simplemente la unin de palbras mediante una suma de las mismas.
tercera_cadena="of "
cuata_cadena="Python"
todas_las_cadenas=(primer_adena+segunda_cadena+tercera_cadena+cuata_cadena)
print(todas_las_cadenas)

print("Ejercicio 2")
#Concatene la cadena 'Coding', 'For' , 'All' en una sola cadena, 'Coding For All'.
C1="Coding "
C2="For "
C3="All"
Concatenacion=(C1+C2+C3)
print(Concatenacion)

print("Ejercicio 3")
#Declare una variable denominada company y asígnela a un valor inicial "Coding For All".
nombre="Company"
nombre="Coding For All"

print("Ejercicio 4")
#Imprime la variable company usando print().
nombre="Company"
nombre="Coding For All"
print(nombre="Coding For All")

print("Ejercicio 5")
#Imprima la longitud de la cadena de la empresa utilizando el método len() y print().
cadena="Coding For All"
print(len(cadena))

print("Ejercicio 6")
#Cambie todos los caracteres a letras mayúsculas usando el método upper().
Caracteres="Coding For All"
print(Caracteres.upper())#EL METODO upper() se utilisa para hacer mayuscula una cadena.

print("Ejercicio 7")
#Cambie todos los caracteres a letras minúsculas usando el método lower().
Caracteres="Coding For All"
print(Caracteres.lower())#el metodo lower() hace todo lo contrario que upper()ya que este comberte toda la cadena en minusculas.

print("Ejercicio 8")
#Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All.
cadena="Coding For All"
print(cadena.capitalize()) #capitalize(): Convierte el primer carácter de la cadena en letra mayúscula
print(cadena.title()) #title(): Devuelve una cadena de título con mayúsculas y minúsculas
print(cadena.swapcase()) #swapcase(): Convierte todos los caracteres en mayúsculas a minúsculas y todos los caracteres en minúsculas a caracteres en mayúsculas

print("Ejercicio 9")
#Corta la primera palabra de la cadena Coding For All.
palabra="Coding For All"
corte=palabra[6:]#con este ###palabra-##[x:] podemos eliminar a antidad de palabras que queramos , osea esto dice que ba a iniciar de el numero x en adelante lo que quede atras no lo leera.
print(corte)

print("Ejercicio 10")
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
#Compruebe si la cadena Codificación para todos contiene una palabra Codificación mediante el método index, find u otros métodos.
Cadena="Codificación"
palabra="Codificación"
Cadena.index(palabra)
print(True or False)

print("Ejercicio 11")
#Replace the word coding in the string 'Coding For All' to Python.
string="coding"
new=string.replace("Coding For All")# el metodo ###replace se utilisa para remplasar una cosa a otra sigiendo esta secuencia x.replase(y)

print("Ejercicio 12")
#Change Python for Everyone to Python for All using the replace method or other methods.
oracion="Python for everyone"
change_for="Python For All"
oracion.replace("Python For All")

print("Ejercicio 13")
#Split the string 'Coding For All' using space as the separator (split()) .
String="Coding For All"
space=String.split()  #el metodo ###split se utilisa para semarar cadenas co esa estructura x.split()
print(space)

print("Ejercicio 14")
#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
string__="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
new_string_with_split=string__.split()
print(new_string_with_split)

print("Ejercicio 15")
#What is the character at index 0 in the string Coding For All.
string_15="Coding For All"
Caracteres=string_15[0]#el metodo ###caracteres se utiliza para la ubucacion de caracteres con la sontaxis de el ejercicio.
print(Caracteres)

print("Ejercicio 16")
#What is the last index of the string Coding For All.
string_16="Coding For All"
last_index=len(string_16)#el metodo len() es utilizado para medir la longitud de una cadena
print(last_index)

print("Ejercicio 17")
#What character is at index 10 in "Coding For All" string.
string_17="Coding For All"
Caracteres=string_17[10]
print(Caracteres)

print("Ejercicio 18")
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
name="Python For Everyone"
avreviacion=(name[0]+name[7]+name[11])
print(avreviacion)

print("Ejercicio 19")
#Create an acronym or an abbreviation for the name 'Coding For All'.
names="Coding For All"
abbreviation=names[0]+names[7]+names[10]
print(abbreviation)

print("Ejercicio 20")
#Use index to determine the position of the first occurrence of C in Coding For All.
cadenna="Coding For All".index("C")###index se utilisa para determinar la pocicion de una letra en una cadena
print(cadenna)

print("Ejercicio 21")
#Use index to determine the position of the first occurrence of F in Coding For All.
cad="Coding For All".index("F")
print(cad)

print("Ejercicio 22")
#Use rfind to determine the position of the last occurrence of l in Coding For All People.
cade="Coding For All".rfind("l")#Este metodo se utiliza para la verificacion de la ubicacion de una letra en una cadena el rfind("") es parecido a el metodo index("")
print(cade)

print("Ejercicio 23")
#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
oracion="You cannot end a sentence with because because because is a conjunction".index("because")
print(oracion)

print("Ejercicio 24")
#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
orac="You cannot end a sentence with because because because is a conjunction".rindex("because")
print(orac) #este metodo rindex nos sirve para verificar la ultima aparicion de una letra o palabra dentro de una cadena

print("Ejercicio 25")
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
oracionn="You cannot end a sentence with because because because is a conjuction"
oracion_nueva=oracionn.replace("because because because", "")#este metodo .replace("") nos sirve para eliminar palabras o letras de una cadena
print(oracion_nueva)

print("Ejercicio 26")
#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence= 'You cannot end a sentence with because because because is a conjunction'
because_in_sentence=sentence.find("because")
print(because_in_sentence)#este metdo se utiliza para la ubicacion de una subcadena o mas bien una palabra dentro de una cadena

print("Ejercicio 27")
#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentencee='You cannot end a sentence with because because because is a conjunction'
because_3=sentencee.strip("because because because")# el metodo .strip()se utiliza para eliminar caracteres dentro de una cadena.
print(because_3)

print("Ejercicio 28")
#Does ''Coding For All' start with a substring Coding?
coding="Coding For All".startswith("Coding")#El metodo .startswith() se utiliza para verificar su una oracion o cadena comienza con una palabra o subcadena especifica.
print(coding)

print("Ejercicio 29")
#Does 'Coding For All' end with a substring coding?
codigo="Coding For All".endswith("coding")#Este .endswith() metodo funciona para verificar si una cadena termina con una sub cadena especifica osea lo contrario de .startswith()
print(codigo)

print("Ejercicio 30")
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
cadene='   Coding For All      '
sin_espacios=cadene.strip()#el metodo strip() se utiliza para eliminar los espacios en una cadena
print(sin_espacios)

print("Ejercicio 31")
#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
variable1="30DaysOfPython"
variable2="thirty_days_of_python"
print(variable1.isidentifier())
print(variable2.isidentifier())#este metodo se utiliza para identificar si una cadena de texto es valida en python

print("Ejercicio 32")
#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
librerias='Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'
resultado="#".join(librerias)#la funcion join funciona para concatenar(Unir) una lista de texto en una sola cadena.
print(resultado)

print("Ejercicio 33")
#Use the new line escape sequence to separate the following sentences.
#I am enjoying this challenge.
#I just wonder what is next.
oraciom="I am enjoying this challenge\n I just wonder what is next"#la operacion \n reprecenta un salto de linea
print(oraciom)

print("Ejercicio 34")
#Use a tab escape sequence to write the following lines.
#Name      Age     Country   City
#Asabeneh  250     Finland   Helsinki
print("Name/Asabeneh")
print("Age/250")
print("Country/Finland")
print("City/Helsinki")

print("Ejercicio 35")
#Use the string formatting method to display the following:
#radius = 10
#area = 3.14 * radius ** 2
#The area of a circle with radius 10 is 314 meters square.
radio=15
area=3.14*radio**2
area_final="El area de el circulo con radio de %r is %a metros"%(radio,area)# aqui utilize los porcentajes para denominarlos como una variable para el radio y el area.
print(area_final)

print("Ejercicio 36")
#Make the following using string formatting methods:
#8 + 6 = 14
#8 - 6 = 2
#8 * 6 = 48
#8 / 6 = 1.33
#8 % 6 = 2
#8 // 6 = 1
#8 ** 6 = 262144
a=10
b=7
print(f"{a}+{b}={a+b}")#la f permite la incorporacion de expreciones dentro de las cadenas de texto {expreciones}
print(f"{a}-{b}={a-b}")
print(f"{a}*{b}={a*b}")
print(f"{a}/{b}={a/b}")
print(f"{a}%{b}={a%b}")
print(f"{a}//{b}={a//b}")
print(f"{a}**{b}={a**b}")

print("Final de el dia 4")


