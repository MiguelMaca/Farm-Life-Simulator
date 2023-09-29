from animals import Animals, Pollo, Vaca, Oveja
from repeat_timer import RepeatTimer
# Primero nombre del archivo, segundo nombre de la clase


def main():
    print('Bienvenido al simulador de mascotas')
    mascota = Animals()
    pollo1 = Pollo()
    vaca1 = Vaca()
    oveja1 = Oveja()

    timer = RepeatTimer(5, mascota.respirar)
    timer.start()

    timer = RepeatTimer(10, mascota.aburrirse)
    timer.start()

    timer = RepeatTimer(60, mascota.crecer)
    timer.start()

    timer = RepeatTimer(60, pollo1.producto)
    timer.start()

    timer = RepeatTimer(60, vaca1.producto)
    timer.start()

    timer = RepeatTimer(60, oveja1.producto)
    timer.start()

    while True:
        print('-----Opciones-----')
        print('0. Estadisticas de mis Animales')
        print('1. Jugar')
        print('2. Alimentar Animales')
        print('3. Animales Descansen')
        print('4. Llevar al Veterinario')
        print('10. Salir')
        opcion = int(input('Ingrese una opcion: '))

        if opcion == 0:
            mascota.estadisticas()
        elif opcion == 1:
            mascota.jugar()
        elif opcion == 2:
            mascota.comer()
        elif opcion == 3:
            mascota.dormir()
        elif opcion == 4:
            mascota.dogtor()
        elif opcion == 10:
            print('Adios :( ')
            break
main()