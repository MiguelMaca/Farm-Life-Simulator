import sys

from animals import Animals, Pollo, Vaca, Oveja, Inicio, InicioP
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
    if opcion == 1:
        planta.menuplan()
    elif opcion == 2:
        animal.menuan()
    elif opcion == 3:
        print("1. Comprar")
        print("2. Vender")
        print("3. Mejora")
        opmerca = int(input("Que desea hacer: "))
        if opmerca == 1:
            compra.compra()
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


