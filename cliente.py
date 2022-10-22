class Cliente:
    def __init__(self, nombre=None, apellido=None, cedula=None, ciudad=None):
        self.nombre = nombre   
        self.apellido = apellido   
        self.cedula = cedula   
        self.ciudad = ciudad   

    def mostarCliente(self):
        print(f'Nombre: {self.nombre}, Apellido: {self.apellido}, Cedula: {self.cedula}, Ciudad. {self.ciudad}')