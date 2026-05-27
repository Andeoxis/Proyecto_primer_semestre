# Bloque_1  Primer_avance1

# Bienvenida al sistema
print('\n          BIENVENIDO AL SISTEMA DE REGISTRO DE HUEVOS POR MAYOR          \n')

# Cuenta existente para validar el ingreso del usuario
usuario_antiguo = "Anthony"
clave_antigua = "clave123"

# Bucle para validar que solo se ingrese 'si' o 'no'
while True:
    tiene_cuenta_o_no = input('¿Ya tiene una cuenta creada? (si/no): ').strip().lower()
    
    # Validación usando el operador 'or' en lugar de una lista
    if tiene_cuenta_o_no == 'si' or tiene_cuenta_o_no == 'no':
        break  # Rompe el bucle si la respuesta es exactamente 'si' o 'no'
    else:
        print('Opción no válida. Por favor, escriba únicamente "si" o "no".\n')


if tiene_cuenta_o_no == 'si':
    
    # Este bucle controla que se repita todo si el usuario o la contraseña están mal
    while True:
        usuario = input('Por favor, ingrese su usuario: ').strip()
        
        if usuario == usuario_antiguo:
            print('Usuario correcto. Por favor, ingrese su clave de acceso para ingresar al sistema.')
            
            
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



elif tiene_cuenta_o_no == 'no':
    print('\n--- Registro de Nuevo Usuario ---')
    creacion_usuario = input('Cree un nombre de usuario: ').strip()
    creacion_clave_de_acceso = input('Cree una clave de acceso: ').strip()
    
    print(f'Bienvenido usuario {creacion_usuario}, su clave de acceso ha sido creada exitosamente.')
    print('Por favor, ingrese su clave de acceso para ingresar al sistema.')
    
    
    while True:
        Ingreso_de_contraseña = input('Ingrese la clave de acceso: ').strip()
        
        if Ingreso_de_contraseña == creacion_clave_de_acceso:
            print('Acceso permitido al sistema.')
            break
        else:
            print('Clave de acceso incorrecta. Intente nuevamente.')



