# Bloque_1  Primer_avance1

# Bienvenida al sistema
print('\n          BIENVENIDO AL SISTEMA DE REGISTRO DE HUEVOS POR MAYOR          \n')

# Cuenta existente para validar el ingreso del usuario
usuario_antiguo = "Anthony"
clave_antigua = "clave123"

# Preguntar si tiene cuenta limpiando espacios y pasando a minúsculas
tiene_cuenta_o_no = input('¿Ya tiene una cuenta creada? (si/no): ').strip().lower()



if tiene_cuenta_o_no == 'si':
    
    # Este bucle controla que se repita todo si el usuario o la contraseña están mal
    while True:
        usuario = input('Por favor, ingrese su usuario: ').strip()
        
        if usuario == usuario_antiguo:
            print('Usuario correcto. Por favor, ingrese su clave de acceso para ingresar al sistema.')
            
            # Bucle interno para validar la contraseña
            while True:
                Ingreso_de_contraseña = input('Ingrese la clave de acceso: ').strip()
                
                if Ingreso_de_contraseña == clave_antigua:
                    print('Acceso permitido')
                    break  # Rompe el bucle de la contraseña
                else:
                    print('Clave de acceso incorrecta. Intente nuevamente.')
            
            break  # Rompe el bucle principal del usuario una vez que el login fue exitoso
            
        else:
            print('El usuario ingresado no existe. Intente de nuevo.\n')



else:
    print('\n--- Registro de Nuevo Usuario ---')
    creacion_usuario = input('Cree un nombre de usuario: ').strip()
    creacion_clave_de_acceso = input('Cree una clave de acceso: ').strip()
    
    print(f'Bienvenido usuario {creacion_usuario}, su clave de acceso ha sido creada exitosamente.')
    print('Por favor, ingrese su clave de acceso para ingresar al sistema.')
    
    # Bucle para validar la contraseña del NUEVO usuario
    while True:
        Ingreso_de_contraseña = input('Ingrese la clave de acceso: ').strip()
        
        if Ingreso_de_contraseña == creacion_clave_de_acceso:
            print('Acceso permitido al sistema.')
            break
        else:
            print('Clave de acceso incorrecta. Intente nuevamente.')

# BLOQUE 2: MENÚ PRINCIPAL

print('\n          Cargando Menú Principal...          \n')

# Variables numéricas que representan el estado inicial de nuestro negocio
inventario_maples = 1000  # Cantidad inicial de maples de huevo en el almacén
ventas_totales = 0        # Contador de maples vendidos

while True:
    print('\n--- MENÚ DE GESTIÓN DE INVENTARIO ---')
    print('''1. Registrar venta Restar inventario
2. Registrar nuevo ingreso Sumar inventario
3. Ver estado del inventario
Escriba "SALIR" para cerrar el programa.''')
    
    opcion_elegida = input('\nIngrese la opción que desea realizar: ').strip().lower().replace(' ', '')  # Normalizamos la entrada para facilitar la comparación
    
    if opcion_elegida == '1' or opcion_elegida == 'registrar venta':
        cantidad_venta = input('¿Cuántos maples de huevo se vendieron?: ').strip()
        
        cantidad_venta = int(cantidad_venta)
        inventario_maples = inventario_maples - cantidad_venta  # Restamos al estado inicial
        ventas_totales = ventas_totales + cantidad_venta        # Sumamos a las ventas
        print(f'>>> Éxito: Se han restado {cantidad_venta} maples del inventario.')
            
    elif opcion_elegida == '2' or opcion_elegida == 'registrar nuevo ingreso':
        cantidad_ingreso = input('¿Cuántos maples de huevo nuevos llegaron al almacén?: ').strip()
        
        cantidad_ingreso = int(cantidad_ingreso)
        inventario_maples = inventario_maples + cantidad_ingreso # Sumamos al estado inicial
        print(f' Éxito: Se han sumado {cantidad_ingreso} maples al inventario.')
            
    elif opcion_elegida == '3' or opcion_elegida == 'ver estado':
        print('\n--- ESTADO ACTUAL DEL NEGOCIO ---')
        print(f'Maples disponibles en almacén: {inventario_maples}')
        print(f'Total de maples vendidos hoy: {ventas_totales}')
        print('---------------------------------')
        
    elif opcion_elegida == 'salir':
        print('\nCerrando el sistema de registro... ¡Que tenga un excelente día!')
        break
    else:
        print('\n' \
        ' Opción no válida. Por favor, intente de nuevo y elija 1, 2, 3 o SALIR.')
