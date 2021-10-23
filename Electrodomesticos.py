class Electrodomesticos:
    def __init__(self, precioB=100,color="blanco",consumo='F',peso=5):
        if color in ("blanco", "negro", "gris", "rojo", "azul"):
            self.color=color
        self.precioBase = precioB
        self.comprobarConsumoEnergetico(consumo)
        self.peso = peso

    # Se le suma el precio segun el consumo
    def precioFinal(self):
        if self.consumo == 'A':
            self.precioBase = self.precioBase + 100
        elif self.consumo == 'B':
            self.precioBase = self.precioBase + 80
        elif self.consumo == 'C':
            self.precioBase = self.precioBase + 60
        elif self.consumo == 'D':
            self.precioBase = self.precioBase + 50
        elif self.consumo == 'E':
            self.precioBase = self.precioBase + 30
        elif self.consumo == 'F':
            self.precioBase = self.precioBase + 10

        # Se le añade el precio segun su peso
        if 0 < self.peso < 20:
            self.precioBase = self.precioBase + 10
        elif 20 < self.peso < 49:
            self.precioBase = self.precioBase + 50
        elif 50 < self.peso < 79:
            self.precioBase = self.precioBase + 80
        elif self.peso < 80:
            self.precioBase = self.precioBase + 100

    # Si la letra se encuentra comprendida entre las de la lista se le asigna al consumo
    def comprobarConsumoEnergetico(self, letra):
        if letra in ("A","B","C","D","E","F"):
            self.consumo=letra