# BLOQUE 2: MENÚ PRINCIPAL SIMPLIFICADO


inventario_maples = 1000  # Inventario inicial

while True:
    print('\n--- MENÚ ---')
    print('1. Vender maples \n2. Ingresar maples \n3. Ver inventario \nEscriba "SALIR" para cerrar.')
    
    opcion = input('Opción: ').strip().lower()
    
    if opcion == '1':
        cantidad = int(input('¿Cuántos maples se vendieron?: ').strip())
        inventario_maples = inventario_maples - cantidad
        print(f'Listo. Quedan {inventario_maples} maples en almacén.')
        
    elif opcion == '2':
        cantidad = int(input('¿Cuántos maples ingresaron?: ').strip())
        inventario_maples = inventario_maples + cantidad
        print(f'Listo. Ahora hay {inventario_maples} maples en almacén.')
        
    elif opcion == '3':
        print(f'Inventario actual: {inventario_maples} maples.')
        
    elif opcion == 'salir':
        print('Cerrando sistema...')
        break
        
    else:
        print('Opción no válida. Elija 1, 2, 3 o SALIR.')
