saldo = 1000.0  
historial = []  

def consultar_saldo():
    global saldo  
    print(f"Tu saldo actual es: ${saldo:.2f}")
    

def depositar_dinero():
    
    global saldo 
    cantidad = float(input("Ingresa el valor o cantidad que desea depositar: $"))
    if cantidad > 0:
        saldo += cantidad
        historial.append(f"Depósito: +${cantidad:.2f}")
        print(f"Ha depositado: ${cantidad:.2f}")
    else:
        print("El valor o la cantidad que desea depositar debe ser positiva.")
        
        
def retirar_dinero():
   
    global saldo  
    cantidad = float(input("Ingresa el valor o cantidad que desea retirar: $"))
    if 0 < cantidad <= saldo:
        saldo -= cantidad
        historial.append(f"Retiro: -${cantidad:.2f}")
        print(f"Has retirado: ${cantidad:.2f}")
    elif cantidad > saldo:
        print("No tienes suficiente fondo para retirar esa cantidad.")
    else:
        print("El valor o cantidad que desea retirar debe ser positiva.")
        
def ver_historial():
    
    if historial:
        print("Historial de transacciones:")
        for transaccion in historial:
            print(transaccion)
    else:
        print("No hay transacciones realizadas.")
        
def menu():
    
    while True:  
        print("\nBienvenido al Cajero Automático VIP")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Ver Historial de Transacciones")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            consultar_saldo()
        elif opcion == '2':
            depositar_dinero()
        elif opcion == '3':
            retirar_dinero()
        elif opcion == '4':
            ver_historial()
        elif opcion == '5':
            print("Gracias por usar el Cajero Automático VIP. ¡Hasta luego!")
            break  
        else:
            print("Opción inválida, por favor elige nuevamente.")
            

menu() 
        