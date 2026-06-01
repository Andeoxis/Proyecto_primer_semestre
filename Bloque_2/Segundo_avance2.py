# BLOQUE 2: MENÚ PRINCIPAL

print('\n          Cargando Menú Principal...          \n')

# Variables numéricas que representan el estado inicial de nuestro negocio
inventario_maples = 1000  # Cantidad inicial de maples de huevo en el almacén
ventas_totales = 0        # Contador de maples vendidos

# Menú Principal Continuo que no permite avanzar hasta escribir "salir"
while True:
    print('\n--- MENÚ DE GESTIÓN DE INVENTARIO ---')
    print('''1. Registrar venta Restar inventario
2. Registrar nuevo ingreso Sumar inventario
3. Ver estado del inventario
Escriba "SALIR" para cerrar el programa.''')
    
    # Recibimos la opción del usuario aplicando limpieza de datos (espacios y minúsculas)
    opcion_elegida = input('\nIngrese la opción que desea realizar: ').strip().lower()
    
    # Estructura if-elif-else para manejar las opciones del menú
    if opcion_elegida == '1' or opcion_elegida == 'registrar venta':
        cantidad_venta = input('¿Cuántos maples de huevo se vendieron?: ').strip()
        
        # Convertimos el texto a número entero directamente
        cantidad_venta = int(cantidad_venta)
        inventario_maples = inventario_maples - cantidad_venta  # Restamos al estado inicial
        ventas_totales = ventas_totales + cantidad_venta        # Sumamos a las ventas
        print(f'>>> Éxito: Se han restado {cantidad_venta} maples del inventario.')
            
    elif opcion_elegida == '2' or opcion_elegida == 'registrar nuevo ingreso':
        cantidad_ingreso = input('¿Cuántos maples de huevo nuevos llegaron al almacén?: ').strip()
        
        # Convertimos el texto a número entero directamente
        cantidad_ingreso = int(cantidad_ingreso)
        inventario_maples = inventario_maples + cantidad_ingreso # Sumamos al estado inicial
        print(f'>>> Éxito: Se han sumado {cantidad_ingreso} maples al inventario.')
            
    elif opcion_elegida == '3' or opcion_elegida == 'ver estado':
        print('\n--- ESTADO ACTUAL DEL NEGOCIO ---')
        print(f'Maples disponibles en almacén: {inventario_maples}')
        print(f'Total de maples vendidos hoy: {ventas_totales}')
        print('---------------------------------')
        
    elif opcion_elegida == 'salir':
        print('\nCerrando el sistema de registro... ¡Que tenga un excelente día!')
        break  # Este break rompe el bucle infinito y termina el programa
        
    else:
        # Opción por defecto si el usuario escribe algo que no está en el menú
        print('\n>>> Opción no válida. Por favor, intente de nuevo y elija 1, 2, 3 o SALIR.')