# Aca lo que hago es dar la bienvenida al usuario y la \n la uso para saltar lineas, depende si lo coloco atras o adalante salta un espacio arriba o abajo.
print('\n          BIENVENIDO AL SISTEMA DE REGISTRO DE HUEVOS POR MAYOR          \n')
# Aca estoy guardando cual es la contraseña correcta que permitira entrar al sistema.
clave_de_acceso = 'Holabebe'


 # Aca estamos usando el while True, ya que este hace que el programa se ejecute de manera indefinida hasta que se cumpla la condicion de romper el ciclo, en este caso es cuando el usuario ingresa la contraseña correcta, si no es asi, el programa seguira pidiendo la contraseña y mostrando un mensaje de error.
while True:
    Ingreso_de_contraseña = input('''Ingrese la clave de acceso:
''')
    if Ingreso_de_contraseña == clave_de_acceso:
        print('Acceso permitido')
        break
    else:
        print('Clave de acceso incorrecta. Intente nuevamente.')



