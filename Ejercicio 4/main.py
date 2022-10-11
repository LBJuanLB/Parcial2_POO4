from cuentaBancaria import CuentaBancaria
from cuentaJoven import CuentaJoven

def CrearCuentaBancaria(self):
    self.cuentasCreadas+=1
    numCuenta=input("Ingrese el numero de cuenta:")
    nomTitular=input("Ingrese el nombre del titular:")
    return CuentaBancaria(numCuenta,nomTitular)

def CrearCuentaJoven(self):
    self.cuentasCreadas+=1
    numCuenta=input("Ingrese el numero de cuenta:")
    nomTitular=input("Ingrese el nombre del titular:")
    return CuentaJoven(numCuenta,nomTitular)

if __name__=='__main__':
    op=1
    Cuentas=[]
    CuentaMain=CuentaBancaria("","")

    while op>0 or op<8:
        print("")
        print("...[OPERACIONES]...")
        print("1. Crear una cuenta")
        print("2. Crear una cuenta joven")
        print("3. Ingresar saldo")
        print("4. Retirar saldo")
        print("5. Mostrar saldo")
        print("6. Mostrar total de cuentas creadas")
        print("7. Salir")
        print("")
        
        op=int(input("Elija una opcion:"))
        while(op<1 or op>7):
            op=int(input("Elija una opcion entre 1 y 7:"))
            print()

        if op==1:
            cuenta=CrearCuentaBancaria(CuentaMain)
            if Cuentas!=[]:
                for i in Cuentas:
                    if i.getNumeroCuenta()!=cuenta.getNumeroCuenta() or Cuentas==[]:
                        Cuentas.append(cuenta)
                        print("La cuenta bancaria se ha creado con exito")
                    else:
                        print("Ya exite una cuenta con ese numero de cuenta")
            else:
                Cuentas.append(cuenta)
                print("La cuenta bancaria se ha creado con exito")
        elif op==2:
            cuenta=CrearCuentaJoven(CuentaMain)
            if Cuentas!=[]:
                for i in Cuentas:
                    if i.getNumeroCuenta()!=cuenta.getNumeroCuenta() or Cuentas:
                        Cuentas.append(cuenta)
                        print("La cuenta bancaria joven se ha creado con exito")
                    else:
                        print("Ya exite una cuenta con ese numero de cuenta")
            else:
                Cuentas.append(cuenta)
                print("La cuenta bancaria joven se ha creado con exito")
        elif op==3:
            numCuenta=input("Ingresar numero de cuenta:")
            for i in Cuentas:
                if i.getNumeroCuenta() == numCuenta:
                    saldo=int(input("Saldo a ingresar:"))
                    if i.IngresarCantidad(saldo) == True:
                        print("Saldo ingresado con exito")
                    else:
                        print("No se ha podido ingresar el saldo")
                else:
                    print("No se ha encontrado la cuenta")
        elif op==4:
            numCuenta=input("Ingrese numero de cuenta:")
            for i in Cuentas:
                if i.getNumeroCuenta() == numCuenta:
                    saldo=int(input("Saldo a retirar:"))
                    if i.RetirarCantidad(saldo) == True:
                        print("Saldo retirado con exito")
                    else:
                        print("No se pudo retirar el saldo")
                else:
                    print("No se ha encontrado la cuenta")
        elif op==5:
            numCuenta=input("Ingrese numero de cuenta:")
            for i in Cuentas:
                if i.getNumeroCuenta() == numCuenta:
                    print("Saldo total:",i.getSaldo())
                else:
                    print("No se ha encontrado la cuenta")
        elif op==6:
            print("Cuentas creadas:",CuentaMain.getCuentasCreadas())
        elif op==7:
            break