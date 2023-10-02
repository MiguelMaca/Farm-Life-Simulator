import sys

from animals import Animals, Pollo, Vaca, Oveja, Inicio, InicioP, Ventaja
from repeat_timer import RepeatTimer

cultiv = '🌽'
anima = '🐄'
merca = '🚚'
sal = '❌'

compra = Animals()
animal = Inicio()
planta = InicioP()
venta = Ventaja()
pollo1 = Pollo()
vaca1 = Vaca()
oveja1 = Oveja()
animalt = Animals()

timer = RepeatTimer(animalt.productop, pollo1.producto)
timer.start()
timer = RepeatTimer(animalt.productov, vaca1.producto)
timer.start()
timer = RepeatTimer(animalt.productoo, oveja1.producto)
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
                pollo1.venta()
            elif que_deseav == 2:
                vaca1.venta()
            elif que_deseav == 3:
                oveja1.venta()
        elif opmerca == 3:
            venta.mejora()
    elif opcion == 4:
        sys.exit()

#print('\033[1;32mFARM LIFE SIMULATOR ')

