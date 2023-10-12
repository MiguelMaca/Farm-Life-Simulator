import sys

from animals import Animals, Pollo, Vaca, Oveja, Inicio, InicioP, Trigo, Arroz, Tomate, Avena, Maiz
from repeat_timer import RepeatTimer


cultiv = '🌽'
anima = '🐄'
merca = '🚚'
sal = '❌'


compra = Animals()
animal = Inicio()
planta = InicioP()
pollo1 = Pollo()
vaca1 = Vaca()
oveja1 = Oveja()
trigo1 = Trigo()
arroz1 = Arroz()
tomate1 = Tomate()
avena1 = Avena()
maiz1 = Maiz()

timer = RepeatTimer(compra.productop, pollo1.producto)
timer.start()
timer = RepeatTimer(compra.productov, vaca1.producto)
timer.start()
timer = RepeatTimer(compra.productoo, oveja1.producto)
timer.start()

while True:
    print('\033[1;34m================================================')
    print('\033[1;32m              MENU PRINCIPAL \n           FARM LIFE SIMULATOR ')

    print('\033[1;34m=================================================')
    print('\033[1;33m1.- Cultivos', cultiv)
    print('\033[1;33m2.- Animales', anima)
    print('\033[1;33m3.- Mercado', merca)
    print('\033[1;33m4.- Salir del juego', sal)

    print('\033[1;34m=================================================')
    opcion = int(input('¡BIENVENIDO! \n¡Por favor, ingrese una opcion para comenzar a jugar!: '))
    try:
        if opcion == 1:
            planta.menuplan()
        elif opcion == 2:
            animal.menuan()
        elif opcion == 3:
            print("1. Comprar")
            print("2. Vender")
            print("3. Mejora")
            opmerca = int(input("Que desea hacer: "))
    except ValueError:
        print('Datos incorrectos, vuelva a intentar')

        if opmerca == 1:
            que_desea = int(input("Productos para:\n1. Animales\n2. Plantas\nQue desea comprar: "))

            while que_desea > 2 or que_desea < 1:
                que_desea = int(input("Opcion invalida\nProductos para:\n1. Animales\n2. Plantas\nQue desea comprar: "))

            if que_desea == 1:
                que_desea_animales = int(input("1. Comida\n2. Medicamento\nQue desea obtener: "))

                while que_desea_animales > 2 or que_desea_animales < 1:
                    que_desea_animales = int(input("Opcion invalida\n1. Comida\n2. Medicamento\nQue desea obtener: "))

                if que_desea_animales == 1:
                    comida = int(input("1. Concentrado\n2. Heno\nQue comida desea: "))

                    while comida > 2 or comida < 1:
                        comida = int(input("Opcion invalida\n1. Concentrado\n2. Heno\nQue comida desea: "))

                    if comida == 1:
                        if compra.monedas >= 50:
                            compra.monedas -= 50
                            pollo1.concentra()
                            print("Tu dinero: ", compra.monedas)
                        else:
                            print("No tienes suficiente dinero!!!")

                    elif comida == 2:
                        if compra.monedas > 100:
                            compra.monedas -= 50
                            compra.henos()
                            print("Tu dinero: ", compra.monedas)
                        else:
                            print("No tienes suficiente dinero!!!")

                elif que_desea_animales == 2:

                    medicamentos = int(
                        input("1. Vacunas\n2. Vitaminas\3. Jarabe para la tos\nQue medicamento quiere: "))

                    while medicamentos > 3 or medicamentos < 1:
                        medicamentos = int(input(
                            "Opcion invalida\n1. Vacunas\n2. Vitaminas\3. Jarabe para la tos\nQue medicamento quiere: "))

                    if medicamentos == 1:
                        if compra.monedas > 100:
                            compra.monedas -= 100
                            compra.vacun()
                    elif medicamentos == 2:
                        if compra.monedas > 75:
                            compra.monedas -= 75
                            compra.vita()
                    elif medicamentos == 3:
                        if compra.monedas > 50:
                            compra.monedas -= 50
                            compra.jarabe()

            elif que_desea == 2:
                print("Fertilizante")
                print("1. Comprar")
                print("2. Salir")
                plantaop = int(input("Desea comprar fertilizante para las plantas?"))

                if plantaop == 1:
                    try:
                        if compra.monedas > 50:
                            trigo1.compra_fert()
                            arroz1.compra_fert()
                            tomate1.compra_fert()
                            avena1.compra_fert()
                            maiz1.compra_fert()
                            compra.monedas -= 25
                            print("A comprando 50 de fertilizante")
                            print("Tu dinero: ", compra.monedas)
                        else:
                            print("No tienes suficiente dinero!!!")
                    except ValueError:
                        print('Datos incorrectos')

        elif opmerca == 2:
            print("1. Huevos")
            print("2. Leche")
            print("3. Lana")
            que_deseav = int(input("Que desea vender en el mercado?"))
            if que_deseav == 1:
                if pollo1.huevos >= 1:
                    pollo1.venta()
                    compra.ganancia_pollo()
                else:
                    print("No tiene huevos en el inventario")
            elif que_deseav == 2:
                if vaca1.leche >= 1:
                    vaca1.venta()
                    compra.ganancia_vaca()
                else:
                    print("No tiene leche en el inventario")
            elif que_deseav == 3:
                if oveja1.lana >= 1:
                    oveja1.venta()
                    compra.ganancia_oveja()
                else:
                    print("No tienes lana en el inventario")
        elif opmerca == 3:
            compra.mejora()
    elif opcion == 4:
        sys.exit()
