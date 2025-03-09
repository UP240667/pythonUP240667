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
