from CuentaBancaria import CuentaBancaria
from Usuario import Usuario


alicia = Usuario("Alicia", "Araya")
bernardo = Usuario("Bernardo", "Borquez")
carlos = Usuario("Carlos", "Carmona")

alicia.hacer_deposito(50000, "corriente").hacer_deposito(20000, "ahorros").hacer_retiro(30000, "ahorros").generar_interes().mostrar_balance_usuario()


bernardo.hacer_deposito(80000, "ahorros").hacer_retiro(90000, "corriente").generar_interes().mostrar_balance_usuario()


carlos.hacer_deposito(55000, "corriente").hacer_deposito(40000, "ahorros").hacer_retiro(90000, "ahorros").generar_interes().mostrar_balance_usuario()


