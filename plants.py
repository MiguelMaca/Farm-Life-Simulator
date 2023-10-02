#Plantas
from repeat_timer import RepeatTimer


class Trigo:
    def __init__(self):
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

    def fertilizar(self, cantidad_fert):
        if cantidad_fert == 0:
            print('No tiene fertilizante')
        else:
            self.contadort += cantidad_fert
            if self.contadort > 15:
                self.contadort = 15

    def plaga(self):
        print('¡PLAGA ENCONTRADA!, el trigo bajo de nivel :( ')
        self.contadort = self.contadort - 2


class Arroz:
    def __init__(self):
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

    def fertilizar(self, cantidad_fert):
        if cantidad_fert == 0:
            print('No tiene fertilizante')
        else:
            self.contadora += cantidad_fert
            if self.contadora > 15:
                self.contadora = 15

    def plaga(self):
        print('¡PLAGA ENCONTRADA!, el arroz bajo de nivel :( ')
        self.contadora = self.contadora - 2


class Maiz:
    def __init__(self):
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

    def fertilizar(self, cantidad_fert):
        if cantidad_fert == 0:
            print('No tiene fertilizante')
        else:
            self.contadorm += cantidad_fert
            if self.contadorm > 15:
                self.contadorm = 15


class Avena:
    def __init__(self):
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

    def fertilizar(self, cantidad_fert):
        if cantidad_fert == 0:
            print('No tiene fertilizante')
        else:
            self.contadorav += cantidad_fert
            if self.contadorav > 15:
                self.contadorav = 15


class Tomate:
    def __init__(self):
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

    def fertilizar(self, cantidad_fert):
        if cantidad_fert == 0:
            print('No tiene fertilizante')
        else:
            self.contadorto += cantidad_fert
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
timer = RepeatTimer(30,cultivo_uno.plaga)
timer.start()


class InicioP:

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

                print('Cultivos actuales para fertilizar: ', lista)
                fert = input('¿Desea fertilizar algun cultivo: ?')
                if fert == 'Si' or 'si':
                    fert_c = input('A continuacion, elija el cultivo que desea fertilizar: ')
                    if fert_c == 'trigo':
                        cultivo_uno.fertilizar()
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