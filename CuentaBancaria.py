class CuentaBancaria:

    def __init__(self, tasa_interes, balance, cta_corriente, cta_ahorros):
        self.tasa_interes = tasa_interes
        self.balance = balance
        self.cta_corriente = cta_corriente
        self.cta_ahorros = cta_ahorros


    def depósito(self, monto_deposito, tipo_cuenta):
        if tipo_cuenta == "corriente":
            self.cta_corriente += monto_deposito
            self.balance += monto_deposito
        else:
            self.cta_ahorros += monto_deposito
            self.balance += monto_deposito

        return self

    def retiro(self, monto_retiro, tipo_cuenta):
        if self.balance > monto_retiro: 
        
            if tipo_cuenta == "corriente":
                if self.cta_corriente > monto_retiro:
                    self.cta_corriente -= monto_retiro
                    self.balance -= monto_retiro
                else:         
                    print("Fondos insuficientes en Cuenta Corriente. Intente otro monto.")

            else:
                if self.cta_ahorros > monto_retiro:
                    self.cta_ahorros -= monto_retiro
                    self.balance -= monto_retiro
                else:         
                    print("Fondos insuficientes en Cuenta de Ahorros. Intente otro monto.")
        
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        return self


    def mostrar_info_cuenta(self):
        print(f"Su balance actual es de {round(self.balance)} pesos")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)
        return self

