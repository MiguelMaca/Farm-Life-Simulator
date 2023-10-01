import sys
from comercio import JugadorMonedas
from animals import Inicio
from plants import InicioP

cultiv = '🌽'
anima = '🐄'
merca = '🚚'
sal = '❌'

compra = JugadorMonedas()
animal = Inicio()
planta = InicioP()

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
        compra.compra()
    elif opcion == 4:
        sys.exit()
