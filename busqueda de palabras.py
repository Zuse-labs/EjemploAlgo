# Realizar un programa que le solicite una frase al usuario y luego un término para buscar.
# El sistema deberá imprimir por pantalla las palabras de la frase que comienzan con el término que el usuario buscó.
# Ej: ‘mi capacidad para resolver parciales es interminable’ Luego el usuario puede buscar el término: par
# El sistema deberá imprimir por pantalla las palabras: para parciales
#mifrase="pablito clavo un clavito"

mifrase = input(print("ingrese una frase por favor")) 
busqueda = input(print("ingrese una palabra o término a buscar")) 

lista_palabras = mifrase.split(" ")

for palabra in lista_palabras:
    if (busqueda == palabra[0:len(busqueda)-1]):
        print(palabra)
            
    
#en caso que nos pidan una función!:
def MiFuncion(frase,buscar):
    lista_palabras = mifrase.split(" ")

    resultado = []
    for palabra in lista_palabras:
        if (busqueda == palabra[0:len(busqueda)-1]):
            resultado.append(palabra)
    
    return resultado

#programa principal
frase = "pablito clavó un clavito"
buscar = "cla"
print(MiFuncion(frase,buscar)