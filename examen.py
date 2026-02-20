class CuentaBancaria:
    def __init__(self, titular,numero_cuenta,saldo):
        self.titular=titular
        self.numero_cuenta=numero_cuenta
        self.saldo=saldo
    def mostrar_info(self):
        print(f"Titular: {self.titular} | Número de cuenta: {self.numero_cuenta} | Saldo: {self.saldo}")
    def depositar(self,monto):
        if monto>0:
            self.saldo+=monto
            print(f"Deposito exitoso nuevo saldo: {self.saldo}")
        else:
            print(f"El monto debe ser mayor a 0")
    def retirar(self,monto):
        if monto>self.saldo:
            print(f"Error monto insuficiente")
        elif monto<=0:
            print(f"Error el monto debe ser mayor a 0")
        else:
            self.saldo-=monto
            print(f"Retiro exitoso nuevo saldo: {self.saldo}")
cuentas = []
def crear_cuenta():
    titular = input("Ingrese nombre del titular: ")
    numero = input("Ingrese numero de cuenta: ")
    saldo = float(input("Ingrese saldo inicial: "))
    nueva_cuenta = CuentaBancaria(titular,numero,saldo)
    cuentas.append(nueva_cuenta)
    print("Cuenta creada con exito")
def mostrar_cuentas():
    if not cuentas:
        print("No hay cuentas registradas")
    else:
        for cuenta in cuentas:
            cuenta.mostrar_info()
def buscar_cuenta(numero):
    for cuenta in cuentas:
        if cuenta.numero_cuenta==numero:
            return cuenta
        return None
def realizar_deposito()
    numero= input("Ingrese el numero de cuenta")
    cuenta=buscar_cuenta(numero)
    if cuenta:
        monto=float(input("Monto a depositar: "))
        cuenta.depositar(monto)
    else:
        print("La cuenta no existe")
def realizar_retiro():
    numero= input("Ingrese el numero de cuenta")
    cuenta=buscar_cuenta(numero)
    if cuenta:
        monto=float(input("Monto a retirar: "))
        cuenta.retirar(monto)
    else:
        print("La cuenta no existe")
def menu():
    while True:
        print("\nMenu")
        print("1. Crear cuenta")
        print("2. Mostrar cuenta")
        print("3. Depositar dinero")
        print("4. Retirar dinero")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion=="1":
            crear_cuenta()
        elif opcion=="2":
            mostrar_cuentas()
        elif opcion=="3":
            realizar_deposito()
        elif opcion=="4":
            realizar_retiro()
        elif opcion=="5":
            print("Saliendo del programa...")
            break
        else
            print("Opcion no valida.")
if __name__== "__main__":
    menu()
