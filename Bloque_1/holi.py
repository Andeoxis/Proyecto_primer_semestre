print('\n---------- Bienvenido al sistema de registro de huevos por maayor ----------\n')

print(''' Escoge alguna de las opciones para continuar:
      1. Iniciar sesión
      2. Crear cuenta
      3. Salir del sistema''')

while True:
    seleccion = input('Ingrese el número de la opción que desea: ').strip()
    if seleccion == '1' or seleccion == '2' or seleccion == '3':
        break
    else:
        print('Opcion invalida intente nuevamente.')

if seleccion == '1':
    print('\n---- Iniciar sesión ----\n')
    while True:
            cuenta = input('''Ingrese su usuario: ''').strip()
            if cuenta == 'Anthony':
                print('Usuario correcto. Por favor, ingrese su clave de acceso para ingresar al sistema.')
                break
            else:
                print('El usuario ingresado no existe. Intente de nuevo.')

    while True:
        clave = input('Ingrese su clave de acceso: ').strip()
        if clave == 'clave123':
            print ('Acceso permitido al sistema.')
            break
        else:
            print('Clave de acceso incorrecta. Intente nuevamente.')

if seleccion == '2':
    print('\n---- Crear cuenta ----\n')
    nuevo_usuario = input('Crea un nombre de usuario: ').strip()
    nueva_clave = input('Crea una clave de acceso: ').strip()
    print(f'Bienvenido usuario {nuevo_usuario}, su clave de acceso ha sido creada exitosamente.')
    while True:
        clave_ingresada = input('Ingrese su clave de acceso para ingresar al sistema: ').strip()
        if clave_ingresada == nueva_clave:
            print('Acceso permitido al sistema.')
            break
        else:
            print('Clave de acceso incorrecta. Intente nuevamente.')
if seleccion == '3':
    print('Gracias por usar el sistema de registro de huevos por mayor, Hasta luego!')
    



