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



