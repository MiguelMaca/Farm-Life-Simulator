#Plantas

class Trigo:
    def sembrar(self):
        print('¡El cultivo (Trigo) ha sido sembrado con exito!')

    def regar(self):
        print('¡El cultivo (Trigo) ha sido regado con exito!')

    def cosechar(self):
        print('¡El cultivo (Trigo) ha sido cosechado con exito!')


class Regar(Trigo):
  def nivel():
    riego = 0
    contador = 0
    while contador < 10:
      reg = input('¿Desea regar el cultivo?: '
      if reg == 'Si' or reg == 'si':
        contador +=1
        riego = riego + 5
        if riego == 25:
          print('¡Felicidades! Ha aumentado de nivel la cosecha')
          print('Nivel actual de planta: ', riego)
          riego = 0
        else:
          print('¡Planta regada exitosamente!')
    print('No se puede seguir regando la planta; ¡Es hora de cultivar!')


class Arroz:
    def sembrar(self):
        print('¡El cultivo (Arroz) ha sido sembrado con exito!')

    def regar(self):
        print('¡El cultivo (Arroz) ha sido regado con exito!')

    def cosechar(self):
        print('¡El cultivo (Arroz) ha sido cosechado con exito!')


class Maiz:
    def sembrar(self):
        print('¡El cultivo (Maiz) ha sido sembrado con exito!')

    def regar(self):
        print('¡El cultivo (Maiz) ha sido regado con exito!')

    def cosechar(self):
        print('¡El cultivo (Maiz) ha sido cosechado con exito!')


class Avena:
    def sembrar(self):
        print('¡El cultivo (Avena) ha sido sembrado con exito!')

    def regar(self):
        print('¡El cultivo (Avena) ha sido regado con exito!')

    def cosechar(self):
        print('¡El cultivo (Avena) ha sido cosechado con exito!')


cultivo_uno = Trigo()
cultivo_dos = Arroz()
cultivo_tres = Maiz()
cultivo_cuatro = Avena()
while True:
    opci = int(input('¡Bievenido! \n 1. Sembrar \n 2. Regar \n 3. Cosechar \n Por favor, elija alguna de estas opciones: '))

    match(opci):
        case 1:
            cultivo = int(input('De entre estas 5 opciones: \n 1. trigo \n 2. arroz \n 3. maiz \n 4. avena \n 5. \n ¿cual desea '
                                    'cultivar?: '))
            if cultivo == 1:
                cultivo_uno.sembrar()
            elif cultivo == 2:
                cultivo_dos.sembrar()
            elif cultivo == 3:
                cultivo_tres.sembrar()
            elif cultivo == 4:
                cultivo_cuatro.sembrar()


