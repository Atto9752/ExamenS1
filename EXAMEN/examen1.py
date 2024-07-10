# PARTE 1
import examen2 as fn
trabajadores = [
    'Juan Perez','Maria Garcia','Carlos Lopez','Ana Martinez','Pedro Rodriguez','Laura Hernandez',
    'Miguel Sanchez','Isabel Gomez','Francisco Diaz','Elena Fernandez'
    ] 

while True:
    print('********************************')
    print('             MENU')
    print('1.- Asignar sueldos aleatorios.')
    print('2.- Clasificar sueldos.')
    print('3.- Ver estadísticas.')
    print('4.- Reporte de sueldos.')
    print('5.- Salir.')
    print('********************************')

    while True:
        try:
            opcion=int(input('Seleccione una opción: '))
            if opcion >= 1 and opcion <= 5:
                break
            else:
                print('Ingrese una opción válida.')
        except ValueError:
            print('Ingrese una opción válida.')
    
    if opcion == 1:
        lista_sueldos,lista_reporte=fn.Asignar(trabajadores)
    elif opcion == 2:
        while True:
            try:
                fn.Clasificar(lista_sueldos)
                break
            except NameError:
                print('\nPOR FAVOR, ASIGNE PRIMERO LOS SUELDOS ALEATORIOS.\n')
                break
    elif opcion == 3:
        while True:
            try:
                fn.Estadisticas(lista_sueldos)
                break
            except NameError:
                print('\nPOR FAVOR, ASIGNE PRIMERO LOS SUELDOS ALEATORIOS.\n')
                break
    elif opcion == 4:
        while True:
            try:
                fn.Reporte(lista_reporte)
                break
            except NameError:
                print('\nPOR FAVOR, ASIGNE PRIMERO LOS SUELDOS ALEATORIOS.\n')
                break
    elif opcion == 5:
        print('---------------------------------')
        print('Finalizando programa...')
        print('Desarrollado por Antonia Faúndes')
        print('RUT 20.773.519-1')
        print('---------------------------------')
        break