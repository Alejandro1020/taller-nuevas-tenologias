from cuenta import Cuenta
from cliente import Cliente


print("***MENU***")
print("1. Ingresar cliente")
print("2. Mostrar info del cliente")
print("3. Mostrar saldo")
print("4. Ingresar saldo")
print("5. Retirar saldo")
print("6. SALIR")
opcion=100

while(opcion != 0):
    opcion =int(input("Digite una opcion: "))
    if(opcion==1):
        nombre = input("Digite el nombre del cliente: ") 
        apellido = input("Digite los apellidos del cliente: ")
        cedula = input("Digite la cedula del cliente: ")
        ciudad = input("Digite la ciudad: ")

        cliente = Cliente(nombre, apellido, cedula, ciudad)

        numeroCuenta = int(input("Digite su numero de cuenta: "))
        saldo = int(input("Digite su saldo actual: "))

        cuenta = Cuenta(numeroCuenta, saldo)
    elif(opcion==2):
        cliente.mostarCliente()
        cuenta.consultarSaldo()
    elif(opcion==3):
        cuenta.consultarSaldo()
    elif(opcion==4):
        cantida = int(input("Digite la cantidad de dinero que desea consignar: "))
        cuenta.ingresarSaldo(cantida)
    elif(opcion==5):
        cantida = int(input("Digite la cantidad de dinero que desea retirar: "))
        cuenta.retirarSaldo(cantida)
    elif(opcion==6):
        opcion=0
    else:
        print('Opcion no valida')
