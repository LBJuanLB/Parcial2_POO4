from cuentaBancaria import CuentaBancaria

class CuentaJoven(CuentaBancaria):
    def __init__(self, numeroCuenta, nombreTitular):
        super().__init__(numeroCuenta, nombreTitular)
    
    def IngresarCantidad(self, cantidad):
        return super().IngresarCantidad(cantidad)

    def RetirarCantidad(self, cantidad):
        return super().RetirarCantidad(cantidad)