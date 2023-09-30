#from Jugador_monedas import Economia_comercio

class Animals: #La clase inicia con mayuscula y en singular
    def __init__(self):
        self.edad = 0
        self.salud = 100
        self.entretenimeinto = 100
        self.energia = 100
        self.vacunas = 0
        self.vitaminas = 0
        self.jarabe = 0
        self.heno = 0
        self.concentrado = 0


class Pollo(Animals):
    def __init__(self):
        super().__init__()
        self.huevos = 0

    def producto(self):
        self.huevos = self.huevos =+ 1
        print("Tu gallina acaba de producir huevos")

    def estadisticas(self):
        print("Pollo")
        print("Edad:", self.edad)
        print("Salud:", self.salud)
        print("Entretenimiento:", self.entretenimeinto)
        print("Energia:", self.energia)

    def respirar(self):
        if self.energia > 0:
            self.energia -= 1
        else:
            if self.salud <= 0:
                print("Tu Gallina murio de enfermedad")
            else:
                self.salud -= 2

    def aburrirse(self):
        if self.entretenimeinto > 0:
            self.entretenimeinto -= 1
        else:
            if self.salud <= 0:
                print("Tu Gallina murio de aburrimiento")
            else:
                self.salud -= 1

    def crecer(self):
        print("Tu gallina ha crecido")
        self.edad += 1

    def comer(self):
        print('1. Concentrado')
        print('2. Heno')
        comida = int(input('Ingrese que va a comer la gallina: '))

        if comida == 1:
            if self.concentrado == 0:
                print("No tienes suficiente concentrado para tu gallina")
            elif self.energia >= 100 or self.salud >= 100:
                print('Tu gallina no tiene hambre')
            else:
                self.energia += 10
                self.salud += 1
                print('"la gallina come"')
        elif comida == 2:
            if self.heno == 0:
                print("No tienes suficiente heno para tu gallina")
            elif self.energia or self.salud >= 100:
                print('Tu gallina no tiene hambre')
            else:
                self.energia += 20
                self.salud += 5
                print('"la gallina come"')
        else:
            print('Opcion no Valida')

    def jugar(self):
        print('-----Acariciar-----')

        if self.entretenimeinto >= 0 or self.entretenimeinto <= 80:
            print('-----¡Acertaste!-----')
            print('Al la gallina le agradas')
            print('Aumentó 25 de entretenimiento')
            self.entretenimeinto += 25
        elif self.entretenimeinto >= 80:
            print('-----Fallaste-----')
            print('La gallina se molesto')
            print('Perdiste Entretenimiento')
            print('Perdiste Energia')
            self.entretenimeinto -= 10
            self.energia -= 10

        if self.entretenimeinto >= 100:
            self.entretenimeinto = 100

    def dogtor(self):
        if self.salud >= 96:
            print('---Tu gallina tiene buena salud---')
            print('---No necesita ir al veterinario---')
        else:
            print('1. Vitaminas')
            print('2. Jarabe para la Tos')
            print('3. Vacuna')
            medicina = int(input('Ingrese el medicamento para la gallina:'))

            if medicina == 1:
                if self.salud >= 95:
                    self.salud = 100
                    print('Tu gallina tiene buena salud')
                else:
                    self.salud += 5
                    print('Tu gallina recupero salud')

            elif medicina == 2:
                if self.salud >= 80:
                    print('Tu gallina tiene buena salud')
                    self.salud = 100
                else:
                    self.salud += 20
                    print('Tu gallina recupero salud')

            elif medicina == 3:
                if self.salud >= 50:
                    print('Tu gallina tiene muy buena salud')
                    self.salud = 100
                else:
                    print('Tu gallina recupero salud')
                    self.salud += 50

            else:
                print('Opcion no Valida')

    def dormir(self):
        print('1. Una Hora')
        print('2. Dos Horas')
        print('3. Tres Horas a Cinco')
        print('6. Seis Horas a Siete')
        print('8. Ocho Horas')
        print('9. Nueve horas o más')
        hora = int(input('Cuantas Horas va a dormir el cerdo aproximadamente: '))

        if hora == 1:
            self.energia += 10
            print('Tu gallina recupero energia')
        elif hora == 2:
            self.energia += 25
            print('Tu gallina recupero energia')
        elif hora == 3:
            self.energia += 40
            print('Tu gallina recupero energia')
        elif hora == 6:
            self.energia += 50
            print('Tu gallina recupero energia')
        elif hora == 8:
            self.energia += 100
            print('Tu gallina recupero energia')
        elif hora == 9:
            self.energia += 100
            self.salud -= 5
            print('Tu gallina recupero energia')
        if self.energia >= 100:
            self.energia = 100
            print('Tu gallina tiene la energia completa')
        else:
            print('Opcion no Valida')

class Vaca(Animals):
    def __init__(self):
        super().__init__()
        self.leche = 0

    def producto(self):
        self.leche = self.leche + 1
        print("Tu vaca acaba de producir Leche")

    def estadisticas(self):
        print("Oveja")
        print("Edad:", self.edad)
        print("Salud:", self.salud)
        print("Entretenimiento:", self.entretenimeinto)
        print("Energia:", self.energia)

    def respirar(self):
        if self.energia > 0:
            self.energia -= 1
        else:
            if self.salud <= 0:
                print("Tu vaca murio de enfermedad")
            else:
                self.salud -= 2

    def aburrirse(self):
        if self.entretenimeinto > 0:
            self.entretenimeinto -= 1
        else:
            if self.salud <= 0:
                print("Tu vaca murio de aburrimiento")
            else:
                self.salud -= 1

    def crecer(self):
        print("Tu vaca ha crecido")
        self.edad += 1

    def comer(self):
        print('1. Concentrado')
        print('2. Heno')
        comida = int(input('Ingrese que va a comer la vaca: '))

        if comida == 1:
            if self.concentrado == 0:
                print("No tienes suficiente concentrado para tu vaca")
            elif self.energia >= 100 or self.salud >= 100:
                print('Tu vaca no tiene hambre')
            else:
                self.energia += 10
                self.salud += 1
                print('"la vaca come"')
        elif comida == 2:
            if self.heno == 0:
                print("No tienes suficiente heno para tu vaca")
            if self.energia or self.salud >= 100:
                print('Tu vaca no tiene hambre')
            else:
                self.energia += 20
                self.salud += 5
                print('"la vaca come"')
        else:
            print('Opcion no Valida')

    def jugar(self):
        print('-----Acariciar-----')

        if self.entretenimeinto >= 0 or self.entretenimeinto <= 80:
            print('-----¡Acertaste!-----')
            print('A la vaca le agradas')
            print('Aumentó 25 de entretenimiento')
            self.entretenimeinto += 25
        elif self.entretenimeinto >= 80:
            print('-----Fallaste-----')
            print('la vaca se molesto')
            print('Perdiste Entretenimiento')
            print('Perdiste Energia')
            self.entretenimeinto -= 10
            self.energia -= 10

        if self.entretenimeinto >= 100:
            self.entretenimeinto = 100

    def dogtor(self):
        if self.salud >= 96:
            print('---Tu vaca tiene buena salud---')
            print('---No necesita ir al veterinario---')
        else:
            print('1. Vitaminas')
            print('2. Jarabe para la Tos')
            print('3. Vacuna')
            medicina = int(input('Ingrese el medicamento para la vaca:'))

            if medicina == 1:
                if self.salud >= 95:
                    self.salud = 100
                    print('Tu vaca tiene buena salud')
                else:
                    self.salud += 5
                    print('Tu vaca recupero salud')

            elif medicina == 2:
                if self.salud >= 80:
                    print('Tu vaca tiene buena salud')
                    self.salud = 100
                else:
                    self.salud += 20
                    print('Tu vaca recupero salud')

            elif medicina == 3:
                if self.salud >= 50:
                    print('Tu vaca tiene muy buena salud')
                    self.salud = 100
                else:
                    print('Tu vaca recupero salud')
                    self.salud += 50

            else:
                print('Opcion no Valida')

    def dormir(self):
        print('1. Una Hora')
        print('2. Dos Horas')
        print('3. Tres Horas a Cinco')
        print('6. Seis Horas a Siete')
        print('8. Ocho Horas')
        print('9. Nueve horas o más')
        hora = int(input('Cuantas Horas va a dormir la vaca aproximadamente: '))

        if hora == 1:
            self.energia += 10
            print('Tu vaca recupero energia')
        elif hora == 2:
            self.energia += 25
            print('Tu vaca recupero energia')
        elif hora == 3:
            self.energia += 40
            print('Tu vaca recupero energia')
        elif hora == 6:
            self.energia += 50
            print('Tu vaca recupero energia')
        elif hora == 8:
            self.energia += 100
            print('Tu vaca recupero energia')
        elif hora == 9:
            self.energia += 100
            self.salud -= 5
            print('Tu vaca recupero energia')
        if self.energia >= 100:
            self.energia = 100
            print('Tu vaca tiene la energia completa')
        else:
            print('Opcion no Valida')


class Oveja(Animals):
    def __init__(self):
        super().__init__()
        self.lana = 0

    def producto(self):
        self.lana = + 1
        print("Tu oveja acaba de producir lana")

    def estadisticas(self):
        print("Oveja")
        print("Edad:", self.edad)
        print("Salud:", self.salud)
        print("Entretenimiento:", self.entretenimeinto)
        print("Energia:", self.energia)

    def respirar(self):
        if self.energia > 0:
            self.energia -= 1
        else:
            if self.salud <= 0:
                print("Tu oveja murio de enfermedad")
            else:
                self.salud -= 2

    def aburrirse(self):
        if self.entretenimeinto > 0:
            self.entretenimeinto -= 1
        else:
            if self.salud <= 0:
                print("Tu oveja murio de aburrimiento")
            else:
                self.salud -= 1

    def crecer(self):
        print("Tu oveja ha crecido")
        self.edad += 1

    def comer(self):
        print('1. Concentrado')
        print('2. Heno')
        comida = int(input('Ingrese que va a comer la oveja: '))

        if comida == 1:
            if self.concentrado == 0:
                print("No tienes suficiente concentrado para tu oveja")
            elif self.energia >= 100 or self.salud >= 100:
                print('Tu oveja no tiene hambre')
            else:
                self.energia += 10
                self.salud += 1
                print('"la oveja come"')
        elif comida == 2:
            if self.concentrado == 0:
                print("No tienes suficiente heno para tu oveja")
            if self.energia or self.salud >= 100:
                print('Tu oveja no tiene hambre')
            else:
                self.energia += 20
                self.salud += 5
                print('"la oveja come"')
        else:
            print('Opcion no Valida')

    def jugar(self):
        print('-----Acariciar-----')

        if self.entretenimeinto >= 0 or self.entretenimeinto <= 80:
            print('-----¡Acertaste!-----')
            print('A la oveja le agradas')
            print('Aumentó 25 de entretenimiento')
            self.entretenimeinto += 25
        elif self.entretenimeinto >= 80:
            print('-----Fallaste-----')
            print('La oveja se molesto')
            print('Perdiste Entretenimiento')
            print('Perdiste Energia')
            self.entretenimeinto -= 10
            self.energia -= 10

        if self.entretenimeinto >= 100:
            self.entretenimeinto = 100

    def dogtor(self):
        if self.salud >= 96:
            print('---Tu oveja tiene buena salud---')
            print('---No necesita ir al veterinario---')
        else:
            print('1. Vitaminas')
            print('2. Jarabe para la Tos')
            print('3. Vacuna')
            medicina = int(input('Ingrese el medicamento para la oveja:'))

            if medicina == 1:
                if self.salud >= 95:
                    self.salud = 100
                    print('Tu oveja tiene buena salud')
                else:
                    self.salud += 5
                    print('Tu oveja recupero salud')

            elif medicina == 2:
                if self.salud >= 80:
                    print('Tu oveja tiene buena salud')
                    self.salud = 100
                else:
                    self.salud += 20
                    print('Tu oveja recupero salud')

            elif medicina == 3:
                if self.salud >= 50:
                    print('Tu oveja tiene muy buena salud')
                    self.salud = 100
                else:
                    print('Tu oveja recupero salud')
                    self.salud += 50

            else:
                print('Opcion no Valida')

    def dormir(self):
        print('1. Una Hora')
        print('2. Dos Horas')
        print('3. Tres Horas a Cinco')
        print('6. Seis Horas a Siete')
        print('8. Ocho Horas')
        print('9. Nueve horas o más')
        hora = int(input('Cuantas Horas va a dormir la oveja aproximadamente: '))

        if hora == 1:
            self.energia += 10
            print('Tu oveja recupero energia')
        elif hora == 2:
            self.energia += 25
            print('Tu oveja recupero energia')
        elif hora == 3:
            self.energia += 40
            print('Tu oveja recupero energia')
        elif hora == 6:
            self.energia += 50
            print('Tu oveja recupero energia')
        elif hora == 8:
            self.energia += 100
            print('Tu oveja recupero energia')
        elif hora == 9:
            self.energia += 100
            self.salud -= 5
            print('Tu oveja recupero energia')
        if self.energia >= 100:
            self.energia = 100
            print('Tu oveja tiene la energia completa')
        else:
            print('Opcion no Valida')
