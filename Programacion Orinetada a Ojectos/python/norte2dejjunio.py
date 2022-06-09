""" lenar un vector de N elemntos iprime la posicion y su el valor del elemnto mayor que se almacena en en el venctor """
hastaelemnto=int(input("cuantos numro quiieres ingresar"))
numero=0
lista=[]

while numero < hastaelemnto:
    elementos=int(input("ingrese el valor "))
    lista.append(elementos)
    numero+=1

maximo=max(lista)
print(lista.index(maximo))





print(maximo)

