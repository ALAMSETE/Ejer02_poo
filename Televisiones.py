from Electrodomesticos import Electrodomesticos


class Television(Electrodomesticos):
    def __init__(self, precioB=100, color="blanco", consumo='F', peso=5, resolucion=20, cuatroK=False):

        # Para introducir los valores por parametro(si no queremos que lo valores sean por defecto)
        Electrodomesticos.__init__(self, precioB=precioB, color=color, consumo=consumo, peso=peso)
        self.resolucion = resolucion
        self.fourK = cuatroK

    # Se le añade el precio segun la resolucion y si es 4k
    def precioFinal(self):
        Electrodomesticos.precioFinal(self)
        if self.resolucion > 40:
            self.precioB = self.precioBase * 1.3
        if self.fourK == True:
            self.precioB = self.precioB+50