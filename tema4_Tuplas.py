"""
    Las tuplas son inmutables, no se pueden modificar
"""

tupla = ("uno","dos","tres")
print(tupla)
print(type(tupla))

tuplas_Varios_Tipos = (12,True,"Nombre",3.0,12+3j)
print(tuplas_Varios_Tipos)

tuplas__con_tuplas=(1,2,3,4,(1,2,3))
print(tuplas__con_tuplas)

print(tuplas__con_tuplas[3])
print(tuplas__con_tuplas[-2])
print(tuplas__con_tuplas[0:2])

a,b,c = tupla
print(a)
print(b)
print(c)