# PARTE 2
import random,csv
from statistics import geometric_mean

def Asignar(trabajadores):
    #Crear sueldos de forma aleatoria entre $300.000 y $2.500.000.
    lista_sueldos={}
    lista_reporte={}
    for trabajador in trabajadores:
        sueldo=random.randint(300000,2500000)
        lista_sueldos[trabajador]=sueldo
        salud=round(sueldo*0.07) #Descuento salud 7%
        afp=round(sueldo*0.12) #Descuento AFP 12%
        liquido=round(sueldo-salud-afp) #Sueldo base menos el descuento en salud y menos el descuento afp
        lista_reporte[trabajador]={
            'Sueldo Base':sueldo,
            'Descuento salud':salud,
            'Descuento AFP':afp,
            'Sueldo liquido':liquido
        }
    print('\nSueldos asignados:')
    for trabajador,sueldo in lista_sueldos.items():
        print(f'{trabajador}: ${sueldo}')
    #print(f'\n\n{lista_reporte}') #PARA VERIFICAR LISTA CON DESCUENTOS
    return(lista_sueldos,lista_reporte)


def Clasificar(lista_sueldos):
    #Mostrar la lista de empleados con su sueldo y su respectiva clasificación:
    menor800={}
    entre800y2M={}
    mayor2M={}
    menor=0
    entre=0
    mayor=0
    total=0
    for trabajador,sueldo in lista_sueldos.items():
        if sueldo < 800000:
            menor800[trabajador]=sueldo
            menor=menor+1
            total=total+sueldo
        elif sueldo >= 800000 and sueldo <= 2000000:
            entre800y2M[trabajador]=sueldo
            entre=entre+1
            total=total+sueldo
        elif sueldo > 2000000:
            mayor2M[trabajador]=sueldo
            mayor=mayor+1
            total=total+sueldo
    print(f'\nSueldos menores a $800.000 TOTAL:{menor}')
    print('\nNombre empleado\t\tSueldo')
    for trabajador,sueldo in menor800.items():
        print(f'{trabajador}\t\t${sueldo}')
    print(f'\nSueldos entre $800.000 y $2.000.000 TOTAL:{entre}')
    print('\nNombre empleado\t\tSueldo')
    for trabajador,sueldo in entre800y2M.items():
        print(f'{trabajador}\t\t${sueldo}')
    print(f'\nSueldos mayores a $2.000.000 TOTAL:{mayor}')
    print('\nNombre empleado\t\tSueldo')
    for trabajador,sueldo in mayor2M.items():
        print(f'{trabajador}\t\t${sueldo}')
    print(f'\nTOTAL SUELDOS: ${total}')

def Estadisticas(lista_sueldos):
    #Crear una función que permita mostrar por pantalla los siguientes datos con respecto a los sueldos:
    # Sueldo más alto - Sueldo más bajo - Promedio de sueldos - Media geométrica  
    sueldos=list(lista_sueldos.values())
    mayor=max(sueldos)
    menor=min(sueldos)
    promedio=round(sum(sueldos)/len(sueldos))
    media=round(geometric_mean(sueldos))
    print('\nEstadisticas:')
    print(f'Sueldo más alto: ${mayor}')
    print(f'Sueldo más bajo: ${menor}')
    print(f'Promedio de sueldos: ${promedio}')
    print(f'Media geométrica: ${media}\n')

def Reporte(lista_reporte):
    #Mostrar el detalle de los sueldos de los trabajadores
    #Estos datos se deberán exportar a un archivo CSV.
    print('\n---------------------------------------------------------------------------------------')
    print(f'Nombre empleado\t\tSueldo Base\tDesc. Salud\tDesc. AFP\tSueldo líquido')
    for trabajador,datos in lista_reporte.items():
        print(f'{trabajador}\t\t{datos['Sueldo Base']}\t\t{datos['Descuento salud']}\t\t{datos['Descuento AFP']}\t\t{datos['Sueldo liquido']}')
    print('----------------------------------------------------------------------------------------')
    print()
    with open('reporte.csv','w',newline='') as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(['Nombre empleado','Sueldo Base','Desc. Salud','Desc. AFP','Sueldo líquido'])
        for trabajador,datos in lista_reporte.items():
            base=datos['Sueldo Base']
            salud=datos['Descuento salud']
            afp=datos['Descuento AFP']
            liquido=datos['Sueldo liquido']
            escritor.writerow([trabajador,base,salud,afp,liquido])