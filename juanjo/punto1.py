###Nombre, edad, País, Equipo y tiempo

def datos(cant):
    for i in range(cant):
        ciclista = {}
        ciclista['nombre']=input("digite nombre del ciclista: ")
        ciclista['edad']=int(input("digite la edad del ciclista: "))
        ciclista['pais']=input("digite el pais del ciclista: ")
        ciclista['equipo']=input("digite el equipo del ciclista: ")
        ciclista["tiempo"]=int(input("ingrese el tiempo del ciclista: "))
        ciclistas.append(ciclista)
ciclistas = []

def mostrar(ciclistas_list):
    tiempo_menor = ciclistas_list[0]['tiempo']
    nombre = ciclistas_list[0]['nombre']
    for ciclista in ciclistas_list:
        if ciclista['tiempo']< tiempo_menor:
            tiempo_menor = ciclista['tiempo']
            nombre = ciclista['nombre']
    print("el ciclista con menor tiempo es: ",nombre,"con un tiempo de: ",tiempo_menor)

cant = int(input("ingrese la cantidad de ciclistas: "))
list = ciclistas = []
datos(cant)
mostrar(list)
