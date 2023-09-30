from animals import Pollo, Vaca, Oveja

class Jugador_monedas:
    def __init__(self):
        self.monedas=350
        self.concentrado=0
        self.heno=0
        self.vacunas=0
        self.vitaminas=0
        self.jarabe=0
    def compra(self):
        que_desea=int(input("Productos para:\n1. Animales\n2. Plantas\nQue desea comprar: "))
        while que_desea>2 or que_desea<1:
            que_desea = int(input("Opcion invalida\nProductos para:\n1. Animales\n2. Plantas\nQue desea comprar: "))
        if que_desea==1:
            que_desea_animales=int(input("1. Comida\n2. Medicamento\nQue desea obtener: "))
            while que_desea_animales>2 or que_desea_animales<1:
                que_desea_animales= int(input("Opcion invalida\n1. Comida\n2. Medicamento\nQue desea obtener: "))
            if que_desea_animales==1:
                comida=int(input("1. Concentrado\n2. Heno\nQue comida desea: "))
                while comida>2 or comida<1:
                    comida = int(input("Opcion invalida\n1. Concentrado\n2. Heno\nQue comida desea: "))
                if comida==1:
                    if self.monedas>50:
                        self.monedas=self.monedas-50
                        self.concentrado=self.concentrado+1
                elif comida==2:
                    if self.monedas>100:
                        self.monedas=self.monedas-50
                        self.heno=self.heno+1
            elif que_desea_animales==2:
                medicamentos=int(input("1. Vacunas\n2. Vitaminas\3. Jarabe para la tos\nQue medicamento quiere: "))
                while medicamentos>3 or medicamentos<1:
                    medicamentos = int(input("Opcion invalida\n1. Vacunas\n2. Vitaminas\3. Jarabe para la tos\nQue medicamento quiere: "))
                if medicamentos==1:
                    if self.monedas > 100:
                        self.monedas = self.monedas - 100
                        self.vacunas = self.vacunas + 1
                elif medicamentos==2:
                    if self.monedas > 75:
                        self.monedas = self.monedas - 75
                        self.vitaminas = self.vitaminas + 1
                elif medicamentos==3:
                    if self.monedas > 50:
                        self.monedas = self.monedas - 50
                        self.jarabe = self.jarabe + 1
        elif que_desea==2:
            print("Plantas no hay")
    def venda(self):
        pollo=Pollo()
        vaca=Vaca()
        oveja=Oveja()
        que_deseav=int(input(""))

    def Mejora(self):
        print("Mejora")




