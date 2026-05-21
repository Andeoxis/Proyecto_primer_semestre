print('\n          BIENVENIDO AL SISTEMA DE REGISTRO DE HUEVOS POR MAYOR          \n')

clave_de_acceso = 'Holabebe'



while True:
    Ingreso_de_contraseña = input('''Ingrese la clave de acceso:
''')
    if Ingreso_de_contraseña == clave_de_acceso:
        print('Acceso permitido')
        break
    else:
        print('Clave de acceso incorrecta. Intente nuevamente.')
        


