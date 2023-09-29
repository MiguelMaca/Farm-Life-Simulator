class Animals: #La clase inicia con mayuscula y en singular
    def __init__(self):
        self.edad = 0
        self.salud = 100
        self.entretenimeinto = 100
        self.energia = 100

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
        print("Tu cerdo ha crecido")
        self.edad += 1

    def comer(self):
        print('1. Concentrado')
        print('2. Heno')
        print('3. Vitaminas')
        comida = int(input('Ingrese que va a comer el cerdo: '))

        if comida == 1:
            if self.energia >= 100 or self.salud >= 100:
                print('Tu cerdo no tiene hambre')
            else:
                self.energia += 10
                self.salud += 1
                print('"el cerdo come"')
        elif comida == 2:
            if self.energia or self.salud >= 100:
                print('Tu cerdo no tiene hambre')
            else:
                self.energia += 20
                self.salud += 5
                print('"el cerdo come"')
        elif comida == 3:
            if self.energia or self.salud >= 100:
                print('Tu cerdo no tien hambre')
            else:
                self.energia += 30
                self.salud += 10
                print('"el cerdo come"')
        else:
            print('Opcion no Valida')

    def jugar(self):
        print('-----Acariciar-----')

        if self.entretenimeinto >= 0 or self.entretenimeinto <= 80:
            print('-----¡Acertaste!-----')
            print('Al cerdo le agradas')
            print('Aumentó 25 de entretenimiento')
            self.entretenimeinto += 25
        elif self.entretenimeinto >= 80:
            print('-----Fallaste-----')
            print('El cerdo se molesto')
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
            medicina = int(input('Ingrese el medicamento para el cerdo:'))

            if medicina == 1:
                if self.salud >= 95:
                    self.salud = 100
                    print('Tu cerdo tiene buena salud')
                else:
                    self.salud += 5
                    print('Tu cerdo recupero salud')

            elif medicina == 2:
                if self.salud >= 80:
                    print('Tu cerdo tiene buena salud')
                    self.salud = 100
                else:
                    self.salud += 20
                    print('Tu cerdo recupero salud')

            elif medicina == 3:
                if self.salud >= 50:
                    print('Tu cerdo tiene muy buena salud')
                    self.salud = 100
                else:
                    print('Tu cerdo recupero salud')
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
            print('Tu cerdo recupero energia')
        elif hora == 2:
            self.energia += 25
            print('Tu cerdo recupero energia')
        elif hora == 3:
            self.energia += 40
            print('Tu cerdo recupero energia')
        elif hora == 6:
            self.energia += 50
            print('Tu cerdo recupero energia')
        elif hora == 8:
            self.energia += 100
            print('Tu cerdo recupero energia')
        elif hora == 9:
            self.energia += 100
            self.salud -= 5
            print('Tu cerdo recupero energia')
        if self.energia >= 100:
            self.energia = 100
            print('Tu cerdo tiene la energia completa')
        else:
            print('Opcion no Valida')


class Pollo(Animals):
    def __init__(self):
        super().__init__()
        self.huevos = 0

    def producto(self):
        self.huevos = self.huevos + 1
        print("Tu gallina acaba de producir huevos")


class Vaca(Animals):
    def __init__(self):
        super().__init__()
        self.leche = 0

    def producto(self):
        self.leche = self.leche + 1
        print("Tu vaca acaba de producir Leche")


class Oveja(Animals):
    def __init__(self):
        super().__init__()
        self.lana = 0

    def producto(self):
        self.lana = self.lana + 1
        print("Tu oveja acaba de producir lana")
