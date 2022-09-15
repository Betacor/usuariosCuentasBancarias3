from CuentaBancaria import CuentaBancaria

class Usuario:		
	
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.cuenta = CuentaBancaria(tasa_interes = 0.01, balance = 0, cta_corriente = 0, cta_ahorros = 0)


    def hacer_deposito(self, monto_deposito, tipo_cuenta):
        self.cuenta.depósito(monto_deposito, tipo_cuenta)
        return self

    def hacer_retiro(self, monto_retiro, tipo_cuenta):
        self.cuenta.retiro(monto_retiro, tipo_cuenta)
        return self

    def mostrar_balance_usuario(self):
        print(f"El balance actual de {self.nombre} {self.apellido} es de:\nCuenta Corriente = {self.cuenta.cta_corriente} pesos \nCuenta de Ahorros = {self.cuenta.cta_ahorros} pesos \nTotal = {round(self.cuenta.balance)} pesos")
        return self

    def generar_interes(self):
        self.cuenta.generar_interes()
        return self

