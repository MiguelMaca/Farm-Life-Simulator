from animals import Pollo, Vaca, Oveja
from repeat_timer import RepeatTimer
from economia_comercio import JugadorMonedas
# Primero nombre del archivo, segundo nombre de la clase


def main():
    print('Farm Life Simulator')
    pollo1 = Pollo()
    vaca1 = Vaca()
    oveja1 = Oveja()

    timer = RepeatTimer(5, pollo1.respirar)
    timer.start()
    timer = RepeatTimer(5, vaca1.respirar)
    timer.start()
    timer = RepeatTimer(5, oveja1.respirar)
    timer.start()

    timer = RepeatTimer(10, pollo1.aburrirse)
    timer.start()
    timer = RepeatTimer(10, vaca1.aburrirse)
    timer.start()
    timer = RepeatTimer(10, oveja1.aburrirse)
    timer.start()

    timer = RepeatTimer(60, pollo1.crecer)
    timer.start()
    timer = RepeatTimer(60, vaca1.crecer)
    timer.start()
    timer = RepeatTimer(60, oveja1.crecer)
    timer.start()

    timer = RepeatTimer(60, pollo1.producto)
    timer.start()
    timer = RepeatTimer(60, vaca1.producto)
    timer.start()
    timer = RepeatTimer(60, oveja1.producto)
    timer.start()

    while True:
        print("Que animal desea ver?")
        print("1. Gallina")
        print("2. Vaca")
        print("3. Oveja")
        opcionan = int(input("Ingrese una opcion: "))

        while True:

            if opcionan == 1:
                print('-----Opciones Gallina-----')
                print('0. Estadisticas de Gallina')
                print('1. Jugar')
                print('2. Alimentar Animales')
                print('3. Animales Descansen')
                print('4. Llevar al Veterinario')
                print('5. Producto')
                print('10. Salir')
                opcion = int(input('Ingrese una opcion: '))

                if opcion == 0:
                    pollo1.estadisticas()
                elif opcion == 1:
                    pollo1.jugar()
                elif opcion == 2:
                    pollo1.comer()
                elif opcion == 3:
                    pollo1.dormir()
                elif opcion == 4:
                    pollo1.dogtor()
                elif opcion == 5:
                    pollo1.producto()
                elif opcion == 10:
                    print('Adios')
                    break

            elif opcionan == 2:
                print('-----Opciones Vaca-----')
                print('0. Estadisticas de la Vaca')
                print('1. Jugar')
                print('2. Alimentar Animales')
                print('3. Animales Descansen')
                print('4. Llevar al Veterinario')
                print('5. Producto')
                print('10. Salir')
                opcion = int(input('Ingrese una opcion: '))

                if opcion == 0:
                    vaca1.estadisticas()
                elif opcion == 1:
                    vaca1.jugar()
                elif opcion == 2:
                    vaca1.comer()
                elif opcion == 3:
                    vaca1.dormir()
                elif opcion == 4:
                    vaca1.dogtor()
                elif opcion == 5:
                    vaca1.producto()
                elif opcion == 10:
                    print('Adios')
                    break

            elif opcionan == 3:
                print('-----Opciones Oveja-----')
                print('0. Estadisticas de la Oveja')
                print('1. Jugar')
                print('2. Alimentar Animales')
                print('3. Animales Descansen')
                print('4. Llevar al Veterinario')
                print('5. Producto')
                print('10. Salir')
                opcion = int(input('Ingrese una opcion: '))

                if opcion == 0:
                    oveja1.estadisticas()
                elif opcion == 1:
                    oveja1.jugar()
                elif opcion == 2:
                    oveja1.comer()
                elif opcion == 3:
                    oveja1.dormir()
                elif opcion == 4:
                    oveja1.dogtor()
                elif opcion == 5:
                    oveja1.producto()
                elif opcion == 10:
                    print('Adios')
                    break

main()