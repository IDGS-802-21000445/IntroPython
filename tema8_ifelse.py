print("Leer Numeros")

num1=int(input("Ingrese el valor de n1: "))
num2=int(input("Ingrese el valor de n2: "))

if num1>num2:
    print("El numero {} es mayor que {}".format(num1,num2))

elif num1<num2:
    print("El numero {} es menor que {}".format(num1,num2))

print("------------------------ pedir una edad ------------------------")

edad=int(input("Ingrese su edad: "))
if edad>18:
    print("Es mayor de edad")
elif edad<18:
    print("Tienes 18 años")
else:
    print("No eres mayor de edad")    