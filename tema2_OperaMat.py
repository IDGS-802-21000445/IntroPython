num1 = 20
num2=4

print("La suma es: " , (num1 + num2))
print("La resta es: ", (num1 - num2))
print("La multiplicacion es: ", (num1 * num2))
print("La division es: ", (num1 / num2))
print("La division exacta es: ", (num1 // num2))
print("La potencia es: ", (num1 ** num2))

#Concatenacion en Python

texto1="Hola"
texto2="Mundo"
texto_final = texto1+" " + texto2

print(texto_final)
print("El saludo es : %s %s" % (texto2, texto_final))

saludo_final = "Salud {} {}" .format(texto1, texto2)
print(saludo_final)

saludo_final2 = "Salud {x} {y}" .format(x=texto1, y=texto2)
print(saludo_final2)