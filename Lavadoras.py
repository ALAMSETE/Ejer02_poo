from Electrodomesticos import Electrodomesticos


class Lavadora(Electrodomesticos):

    def __init__(self, precioB=100, color="blanco", consumo='F', peso=5, carga=5):

        # Para introducir los valores por parametro(si no queremos que lo valores sean por defecto)
        Electrodomesticos.__init__(self, precioB=precioB, color=color, consumo=consumo, peso=peso)
        self.carga=carga

    # Se le añade el precio segun su carga
    def precioFinal(self):
        Electrodomesticos.precioFinal(self)
        if self.carga > 30:
            self.precioB = self.precioBase + 50