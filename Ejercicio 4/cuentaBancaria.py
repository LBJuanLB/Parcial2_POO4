class CuentaBancaria:
    def __init__(self,numeroCuenta,nombreTitular):
        """Inicializador de la clase CuentaBancaria
        Args:
            self.numeroCuenta(string): Numero de la cuenta bancaria
            self.nombreTitular(string): Nombre del titular de la cuenta bancaria
        """
        self.numeroCuenta=numeroCuenta
        self.nombreTitular=nombreTitular
        self.saldo=0                        #self.saldo (double): Saldo de la cuenta bancarias, se inicializa en 0
        self.numeroOperaciones=0            #self.numeroOperaciones (int): Numero de operaciones que se han realizado, se inicia en 0
        self.MAXIMOREINTEGRO=5000           #self.MAXIMOREINTEGRO (double): Es la maxima cantidad de dinero que se permite retirar, se inicia en 5000
        self.cuentasCreadas=0               #self.cuentasCReadas (int): Cuenta cuantas cuentas se han creado, se inicia en 0
    '''
    GETERS
    getNumeroCuenta -> string: Retorna el numero de cuenta
    getNombreTitular -> string: Retorna el nombre del titular de la cuenta
    getSaldo -> double: Retorna el saldo que hay en la cuenta
    getNumeroOperaciones -> int: Retorna el total de operaciones realizadas
    getCuentasCreadas -> int: Retorna el total de cuentas creadas
    '''
    def getNumeroCuenta(self):
        return self.numeroCuenta
    def getNombreTitular(self):
        return self.nombreTitular
    def getSaldo(self):
        return self.saldo
    def getNumeroOperaciones(self):
        return self.numeroOperaciones
    def getCuentasCreadas(self):
        return self.cuentasCreadas
    '''
    SETERS
    setSaldo -> none: Modifica el saldo de la cuenta
    setCuentasCreadasNull -> none: Cambia el valor de las cuentas creadas a 0
    '''
    def setSaldo(self,saldo):
        self.saldo=saldo
    def setCuentasCreadasNull(self):
        self.cuentasCreadas=0
    '''
    IngresarCantidad -> bool: Ingresa una cantidad de dinero a la cuenta, retorna un boleano dependiendo si la operacion fue exitosa
    '''
    def IngresarCantidad(self,cantidad):
        if cantidad > 0:
            self.saldo+=cantidad
            self.numeroOperaciones+=1
            return True
        else:
            return False
    '''
    RetirarCantidad -> bool: Retira una cantidad de dinero de la cuenta, retorna un boleano dependiendo si la operacion fue exitosa
    '''
    def RetirarCantidad(self,cantidad):
        if (self.saldo-cantidad)>=0 and cantidad<=self.MAXIMOREINTEGRO:
            self.saldo-=cantidad
            self.numeroOperaciones+=1
            return True
        else:
            return False
