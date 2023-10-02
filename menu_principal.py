from animals import Animals, Inicio, InicioP, Ventaja

cultiv = '🌽'
anima = '🐄'
merca = '🚚'
sal = '❌'

compra = Animals()
animal = Inicio()
planta = InicioP()
venta = Ventaja()

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
            venta.venda()
        elif opmerca == 3:
            venta.mejora()
    elif opcion == 4:
        break

print('\033[1;32mFARM LIFE SIMULATOR ')
