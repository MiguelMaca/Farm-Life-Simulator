from animals import Animals
from repeat_timer import RepeatTimer
# Primero nombre del archivo, segundo nombre de la clase

def main():
    print('Bienvenido al simulador de mascotas')
    nombre = str(input('Ingrese el nombre de su mascota: '))
    mascota = Animals(nombre)

    mascota.sexo()

    timer = RepeatTimer(5, mascota.respirar)
    timer.start()

    timer = RepeatTimer(10, mascota.aburrirse)
    timer.start()

    timer = RepeatTimer(60, mascota.crecer)
    timer.start()

    while True:
        print('Mi mascota:')
        print('-----Opciones-----')
        print('0. Estadisticas de mi Mascota')
        print('1. Jugar')
        print('2. Alimentar Mascota')
        print('3. Mascota Descanse')
        print('4. Llevar al Veterinario')
        print('10. Abandonar Mascota :( ')
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