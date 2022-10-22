class Cuenta:

    def __init__(self, numeroCuenta, saldo):
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo

    def ingresarSaldo(self, cantidad):
        self.saldo = self.saldo + cantidad
        return self.saldo

    def retirarSaldo(self, cantidad):
        self.saldo = self.saldo - cantidad
        return self.saldo

    def consultarSaldo(self):
        print(f'El saldo de su cuenta es: { self.saldo }')