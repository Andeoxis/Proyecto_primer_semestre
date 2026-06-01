
print('\n          Cargando Menú Principal...          \n')

# Variables numéricas que representan el estado inicial de nuestro negocio
inventario_maples = 1000  # Cantidad inicial de maples de huevo en el almacén
ventas_totales = 0        # Contador de maples vendidos


while True:
    print('\n--- MENÚ DE GESTIÓN DE INVENTARIO ---')
    print('1. Registrar venta (Restar inventario)')
    print('2. Registrar nuevo ingreso (Sumar inventario)')
    print('3. Ver estado del inventario')
    print('Escriba "SALIR" para cerrar el programa.')
    
   
    opcion_elegida = input('\nIngrese la opción que desea realizar: ').strip().lower()
    
    
    if opcion_elegida == '1' or opcion_elegida == 'registrar venta':
        cantidad_venta = input('¿Cuántos maples de huevo se vendieron?: ').strip()
        
        
        if cantidad_venta.isdigit(): 
            cantidad_venta = int(cantidad_venta)
            inventario_maples = inventario_maples - cantidad_venta  # Restamos al estado inicial
            ventas_totales = ventas_totales + cantidad_venta        # Sumamos a las ventas
            print(f'>>> Éxito: Se han restado {cantidad_venta} maples del inventario.')
        else:
            print('>>> Error: Por favor ingrese solo números.')
            
    elif opcion_elegida == '2' or opcion_elegida == 'registrar nuevo ingreso':
        cantidad_ingreso = input('¿Cuántos maples de huevo nuevos llegaron al almacén?: ').strip()
        
        if cantidad_ingreso.isdigit():
            cantidad_ingreso = int(cantidad_ingreso)
            inventario_maples = inventario_maples + cantidad_ingreso # Sumamos al estado inicial
            print(f'>>> Éxito: Se han sumado {cantidad_ingreso} maples al inventario.')
        else:
            print('>>> Error: Por favor ingrese solo números.')
            
    elif opcion_elegida == '3' or opcion_elegida == 'ver estado':
        print('\n--- ESTADO ACTUAL DEL NEGOCIO ---')
        print(f'Maples disponibles en almacén: {inventario_maples}')
        print(f'Total de maples vendidos hoy: {ventas_totales}')
        print('---------------------------------')
        
    elif opcion_elegida == 'salir':
        print('\nCerrando el sistema de registro... ¡Que tenga un excelente día!')
        break  
        
    else:
        
        print('\n>>> Opción no válida. Por favor, intente de nuevo y elija 1, 2, 3 o SALIR.')