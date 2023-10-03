from repeat_timer import RepeatTimer


class Animals: #La clase inicia con mayuscula y en singular
    def __init__(self):
        self.edad = 0
        self.salud = 100
        self.entretenimeinto = 100
        self.energia = 100
        self.vacunas = 1
        self.vitaminas = 1
        self.jarabe = 1
        self.heno = 1
        self.concentrado = 1
        self.monedas = 350
        self.fertilizante = 0
        self.productop = 45
        self.productov = 60
        self.productoo = 75
        self.huevos = 0
        self.leche = 0
        self.lana = 0

    def henos(self):
        self.heno += 25
        print("Se compro 25 de heno")

    def vita(self):
        self.vitaminas += 5
        print("Se compro 5 de vitaminas")

    def jarabe(self):
        self.jarabe += 5
        print("Se compro 5 jarabes")

    def vacun(self):
        self.vacunas += 5
        print("Se compro 5 vacunas")

    def ganancia_pollo(self):
        self.monedas += 5
        print("Gano 5 monedas")
        print("Tu dinero total: ", self.monedas)

    def ganancia_vaca(self):
        self.monedas += 10
        print("Gano 10 monedas")
        print("Tu dinero total: ", self.monedas)

    def ganancia_oveja(self):
        self.monedas += 25
        print("Gano 25 monedas")
        print("Tu dinero total: ", self.monedas)

    def mejora(self):
        print("1. Nivel 1 (Costo 100 monedas)")
        print("2. Nivel 2 (Costo 200 monedas)")
        print("3. Nivel 3 (Costo 300 monedas)")
        opcion = int(input("Que mejora desea realizar a la granja"))

        if opcion == 1:
            if self.monedas < 100:
                print("No tienes suficientes monedas!!!")
            else:
                self.productop = 40
                self.productoo = 70
                self.productov = 55
                print("Tu granja es de Nivel 1 !!!")
                self.monedas -= 100
        elif opcion == 2:
            if self.monedas < 200:
                print("No tienes suficientes monedas!!!")
            else:
                self.productop = 35
                self.productoo = 65
                self.productov = 50
                print("Tu granja es de Nivel 2 !!!")
                self.monedas -= 200
        elif opcion == 3:
            if self.monedas < 300:
                print("No tienes suficientes monedas!!!")
            else:
                self.productop = 30
                self.productoo = 60
                self.productov = 45
                print("Tu granja es de Nivel 3 !!!")
                self.monedas -= 300
        else:
            print("Regresando al menu")


class Pollo(Animals):
    
    def __init__(self):
        super().__init__()

    def producto(self):
        self.huevos += 1
        print("Tu gallina acaba de producir huevos")

    def venta(self):
        print("Vendio 1 huevo")
        self.huevos -= 1

    def concentra(self):
        self.concentrado += 50
        print("Se compro 50 de concentrado")

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
        print('1. Concentrado -Cantidad de Concentrado: ', self.concentrado)
        print('2. Heno -Cantidad de Heno: ', self.heno)
        comida = int(input('Ingrese que va a comer la gallina: '))

        if comida == 1:
            if self.concentrado == 0:
                print("No tienes suficiente concentrado para tu gallina")
            elif self.energia >= 100 or self.salud >= 100:
                print('Tu gallina no tiene hambre')
            else:
                self.energia += 10
                self.salud += 1
                self.concentrado -= 5
                print('"la gallina come 5 de concentrado"')
        elif comida == 2:
            if self.heno == 0:
                print("No tienes suficiente heno para tu gallina")
            elif self.energia or self.salud >= 100:
                print('Tu gallina no tiene hambre')
            else:
                self.energia += 20
                self.salud += 5
                self.heno -= 1
                print('"la gallina come 1 de heno"')
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

    def producto(self):
        self.leche += 1
        print("Tu vaca acaba de producir Leche")

    def venta(self):
        print("Vendio 1 leche")
        self.leche -= 1

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

    def producto(self):
        self.lana += 1
        print("Tu oveja acaba de producir lana")

    def venta(self):
        print("Vendio 1 lana")
        self.lana -= 1

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

timer = RepeatTimer(45, pollo1.crecer)
timer.start()
timer = RepeatTimer(75, vaca1.crecer)
timer.start()
timer = RepeatTimer(60, oveja1.crecer)
timer.start()


class Inicio:

    def menuan(self):
        while True:
            print("Que animal desea ver?")
            print("1. Gallina")
            print("2. Vaca")
            print("3. Oveja")
            print("4. Menu Principal")
            opcionan = int(input("Ingrese una opcion: "))

            while True:

                if opcionan == 1:
                    print('-----Opciones Gallina-----')
                    print('0. Estadisticas de Gallina')
                    print('1. Jugar')
                    print('2. Alimentar Animales')
                    print('3. Animales Descansen')
                    print('4. Llevar al Veterinario')
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
                    elif opcion == 10:
                        print('Adios')
                        break

                elif opcionan == 4:
                    print("Regresando al menu principal")
                    break

            break


class Trigo(Animals):
    def __init__(self):
        super().__init__()
        self.contadort = 0

    def sembrar(self):
        print('¡El cultivo (Trigo) ha sido sembrado con exito!')

    def regar(self):
        while self.contadort <= 15:
            self.contadort += 1
            reg = input('¿Desea regar el cultivo?: ')
            if reg == 'Si' or reg == 'si':

                if self.contadort < 5:
                    print('¡Planta regada exitosamente!')
                elif self.contadort == 5:
                    print('¡Felicidades! Ha aumentado de nivel la cosecha')
                    print('Nivel actual de planta: Brote', self.contadort)
                elif self.contadort > 5 and self.contadort < 10:
                    print('¡Planta regada exitosamente!')
                elif self.contadort == 10:
                    print('¡Felicidades! Ha aumentado de nivel la cosecha')
                    print('Nivel actual de planta: Crecimiento', self.contadort)
                elif self.contadort > 10 and self.contadort <= 15:
                    print('¡Planta regada exitosamente!')
            else:
                return InicioP


        print('No se puede seguir regando la planta, estado: Maduracion; ¡Es hora de cosechar!')
        c1 = 'trigo'
        cosechar_c.append(c1)
        elimt = 'trigo'
        if elimt in lista:
            lista.remove(elimt)
        self.contadort = 0
        return InicioP

    def cosechar(self):
        print('¡El cultivo (Trigo) ha sido cosechado con exito!')
        prod1 = 'trigo'
        productos_g.append(prod1)
        cosecht = 'trigo'
        if cosecht in cosechar_c:
            cosechar_c.remove(cosecht)

    def compra_fert(self):
        self.fertilizante += 5
        print("Se agrego Fertilizante")

    def fertilizar(self):
        self.contadort += 2
        self.fertilizante -= 2
        if self.contadort > 15:
            self.contadort = 15

    def plaga(self):
        print('¡PLAGA ENCONTRADA!, el trigo bajo de nivel :( ')
        self.contadort = self.contadort - 2


class Arroz(Animals):
    def __init__(self):
        super().__init__()
        self.contadora = 0

    def sembrar(self):
        print('¡El cultivo (Arroz) ha sido sembrado con exito!')

    def regar(self):
        while self.contadora <= 15:
            self.contadora += 1
            reg = input('¿Desea regar el cultivo?: ')
            if reg == 'Si' or reg == 'si':

                if self.contadora < 5:
                    print('¡Planta regada exitosamente!')
                elif self.contadora == 5:
                    print('¡Felicidades! Ha aumentado de nivel la cosecha')
                    print('Nivel actual de planta: Brote', self.contadora)
                elif self.contadora > 5 and self.contadora < 10:
                    print('¡Planta regada exitosamente!')
                elif self.contadora == 10:
                    print('¡Felicidades! Ha aumentado de nivel la cosecha')
                    print('Nivel actual de planta: Crecimiento', self.contadora)
                elif self.contadora > 10 and self.contadora <= 15:
                    print('¡Planta regada exitosamente!')
            else:
                return InicioP

        print('No se puede seguir regando la planta, estado: Maduracion; ¡Es hora de cosechar!')
        c2 = 'arroz'
        cosechar_c.append(c2)
        elima = 'arroz'
        if elima in lista:
            lista.remove(elima)
        self.contadora = 0
        return InicioP

    def cosechar(self):
        print('¡El cultivo (Arroz) ha sido cosechado con exito!')
        prod2 = 'arroz'
        productos_g.append(prod2)

    def compra_fert(self):
        self.fertilizante += 5

    def fertilizar(self):
        self.contadora += 2
        self.fertilizante -= 2
        if self.contadora > 15:
            self.contadora = 15

    def plaga(self):
        print('¡PLAGA ENCONTRADA!, el arroz bajo de nivel :( ')
        self.contadora = self.contadora - 2


class Maiz(Animals):
    def __init__(self):
        super().__init__()
        self.contadorm = 0

    def sembrar(self):
        print('¡El cultivo (Maiz) ha sido sembrado con exito!')

    def regar(self):
        while self.contadorm <= 15:
            self.contadorm += 1
            reg = input('¿Desea regar el cultivo?: ')
            if reg == 'Si' or reg == 'si':

                if self.contadorm < 5:
                    print('¡Planta regada exitosamente!')
                elif self.contadorm == 5:
                    print('¡Felicidades! Ha aumentado de nivel la cosecha')
                    print('Nivel actual de planta: Brote', self.contadorm)
                elif self.contadorm > 5 and self.contadorm < 10:
                    print('¡Planta regada exitosamente!')
                elif self.contadorm == 10:
                    print('¡Felicidades! Ha aumentado de nivel la cosecha')
                    print('Nivel actual de planta: Crecimiento', self.contadorm)
                elif self.contadorm > 10 and self.contadorm <= 15:
                    print('¡Planta regada exitosamente!')
            else:
                return InicioP

        print('No se puede seguir regando la planta, estado: Maduracion; ¡Es hora de cosechar!')
        c3 = 'maiz'
        cosechar_c.append(c3)
        elimm = 'maiz'
        if elimm in lista:
            lista.remove(elimm)
        self.contadorm = 0
        return InicioP

    def cosechar(self):
        print('¡El cultivo (Maiz) ha sido cosechado con exito!')
        prod3 = 'maiz'
        productos_g.append(prod3)

    def compra_fert(self):
        self.fertilizante += 5

    def fertilizar(self):
        self.contadorm += 2
        self.fertilizante -= 2
        if self.contadorm > 15:
            self.contadorm = 15


class Avena(Animals):
    def __init__(self):
        super().__init__()
        self.contadorav = 0

    def sembrar(self):
        print('¡El cultivo (Avena) ha sido sembrado con exito!')

    def regar(self):
        while self.contadorav <= 15:
            self.contadorav += 1
            reg = input('¿Desea regar el cultivo?: ')
            if reg == 'Si' or reg == 'si':

                if self.contadorav < 5:
                    print('¡Planta regada exitosamente!')
                elif self.contadorav == 5:
                    print('¡Felicidades! Ha aumentado de nivel la cosecha')
                    print('Nivel actual de planta: Brote', self.contadorav)
                elif self.contadorav > 5 and self.contadorav < 10:
                    print('¡Planta regada exitosamente!')
                elif self.contadorav == 10:
                    print('¡Felicidades! Ha aumentado de nivel la cosecha')
                    print('Nivel actual de planta: Crecimiento', self.contadorav)
                elif self.contadorav > 10 and self.contadorav <= 15:
                    print('¡Planta regada exitosamente!')
            else:
                return InicioP

        print('No se puede seguir regando la planta, estado: Maduracion; ¡Es hora de cosechar!')
        c4 = 'avena'
        cosechar_c.append(c4)
        elimav = 'avena'
        if elimav in lista:
            lista.remove(elimav)
        self.contadorav = 0
        return InicioP

    def cosechar(self):
        print('¡El cultivo (Avena) ha sido cosechado con exito!')
        prod4 = 'avena'
        productos_g.append(prod4)

    def compra_fert(self):
        self.fertilizante += 5

    def fertilizar(self):
        self.contadorav += 2
        self.fertilizante -= 2
        if self.contadorav > 15:
            self.contadorav = 15


class Tomate(Animals):
    def __init__(self):
        super().__init__()
        self.contadorto = 0

    def sembrar(self):
        print('¡El cultivo (Tomate) ha sido sembrado con exito!')

    def regar(self):
        while self.contadorto <= 15:
            self.contadorto += 1
            reg = input('¿Desea regar el cultivo?: ')
            if reg == 'Si' or reg == 'si':

                if self.contadorto < 5:
                    print('¡Planta regada exitosamente!')
                elif self.contadorto == 5:
                    print('¡Felicidades! Ha aumentado de nivel la cosecha')
                    print('Nivel actual de planta: Brote', self.contadorto)
                elif self.contadorto > 5 and self.contadorto < 10:
                    print('¡Planta regada exitosamente!')
                elif self.contadorto == 10:
                    print('¡Felicidades! Ha aumentado de nivel la cosecha')
                    print('Nivel actual de planta: Crecimiento', self.contadorto)
                elif self.contadorto > 10 and self.contadorto <= 15:
                    print('¡Planta regada exitosamente!')
            else:
                return InicioP

        print('No se puede seguir regando la planta, estado: Maduracion; ¡Es hora de cosechar!')
        c5 = 'tomate'
        cosechar_c.append(c5)
        elimto = 'tomate'
        if elimto in lista:
            lista.remove(elimto)
        self.contadorto = 0
        return InicioP

    def cosechar(self):
        print('¡El cultivo (Tomate) ha sido cosechado con exito!')
        prod5 = 'tomate'
        productos_g.append(prod5)

    def compra_fert(self):
        self.fertilizante += 5

    def fertilizar(self):
        self.contadorto += 2
        self.fertilizante -= 2
        if self.contadorto > 15:
            self.contadorto = 15


comprados = []
productos_g = []
cosechar_c = []
lista = []
cultivo_uno = Trigo()
cultivo_dos = Arroz()
cultivo_tres = Maiz()
cultivo_cuatro = Avena()
cultivo_cinco = Tomate()
timer = RepeatTimer(50, cultivo_uno.plaga)
timer.start()


class InicioP(Trigo, Arroz, Maiz, Avena, Tomate, Animals):

    def __init__(self):
        Trigo.__init__(self)
        Arroz.__init__(self)
        Maiz.__init__(self)
        Avena.__init__(self)
        Tomate.__init__(self)
        Animals.__init__(self)

    def menuplan(self):
        while True:
            opci = int(input('¡Bievenido! \n 1.- Sembrar \n 2.- Regar \n 3.- Cosechar \n 4.- Fertilizar '
                             '\n 5.- Salir \n Por favor, elija alguna de estas opciones: '))

            if opci == 1:

                cultivo = int(input('De entre estas 5 opciones: \n 1. trigo \n 2. arroz \n 3. maiz \n 4. avena \n 5. tomate '
                                        '\n ¿cual desea cultivar?: '))
                if cultivo == 1:
                    cultivo_uno.sembrar()
                    p1 = 'trigo'
                    lista.append(p1)
                elif cultivo == 2:
                    cultivo_dos.sembrar()
                    p2 = 'arroz'
                    lista.append(p2)
                elif cultivo == 3:
                    cultivo_tres.sembrar()
                    p3 = 'maiz'
                    lista.append(p3)
                elif cultivo == 4:
                    cultivo_cuatro.sembrar()
                    p4 = 'avena'
                    lista.append(p4)
                elif cultivo == 5:
                    cultivo_cinco.sembrar()
                    p5 = 'tomate'
                    lista.append(p5)

            elif opci == 2:

                print('Estos son los cultivos actuales: ', lista)
                reg = input('Por favor, elija uno de ellos para regar: ')
                if reg == 'trigo':
                    cultivo_uno.regar()
                elif reg == 'arroz':
                    cultivo_dos.regar()
                elif reg == 'maiz':
                    cultivo_tres.regar()
                elif reg == 'avena':
                    cultivo_cuatro.regar()
                elif reg == 'tomate':
                    cultivo_cinco.regar()

            elif opci == 3:

                print('¡Estos son los cultivos listos para cosechar!', cosechar_c)
                cos = input('Por favor, elija uno de ellos para cosechar: ')
                if cos == 'trigo':
                    cultivo_uno.cosechar()
                elif cos == 'arroz':
                    cultivo_dos.cosechar()
                elif cos == 'maiz':
                    cultivo_tres.cosechar()
                elif cos == 'avena':
                    cultivo_cuatro.cosechar()
                elif cos == 'tomate':
                    cultivo_cinco.cosechar()

            elif opci == 4:
                fert = input('¿Desea fertilizar algun cultivo: ?')
                if fert == 'Si' or 'si':
                    print('Cultivos actuales para fertilizar: ', lista)
                    fert_c = input('A continuacion, elija el cultivo que desea fertilizar: ')
                    if fert_c == 'trigo':
                        if self.fertilizante > 1:
                            cultivo_uno.fertilizar()
                        else:
                            print("No tiene fertilizante")
                    elif fert_c == 'arroz':
                        cultivo_dos.fertilizar()
                    elif fert_c == 'maiz':
                        cultivo_tres.fertilizar()
                    elif fert_c == 'avena':
                        cultivo_cuatro.fertilizar()
                    elif fert_c == 'tomate':
                        cultivo_cinco.fertilizar()

            elif opci == 5:
                break

