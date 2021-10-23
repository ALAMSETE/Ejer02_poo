from Electrodomesticos import Electrodomesticos
from Lavadoras import Lavadora
from Televisiones import Television

# Creamos la lista donde se guardaran los electrodomesticos
electrodomestico = ()
electrodomesticos = list(electrodomestico)
# Insertamos los electrodomesticos en la lista
electrodomesticos.insert(-1, Electrodomesticos(consumo="A", peso=15))
electrodomesticos.insert(-1, Electrodomesticos(consumo="A", peso=30))
electrodomesticos.insert(-1, Electrodomesticos(consumo="A", peso=60))
electrodomesticos.insert(-1, Electrodomesticos(consumo="A", peso=90))

electrodomesticos.insert(-1,Lavadora(consumo="E", peso=50, carga=30))
electrodomesticos.insert(-1,Lavadora(consumo="A", peso=50, carga=60))

electrodomesticos.insert(-1, Television(peso=20, resolucion=30))
electrodomesticos.insert(-1, Television(peso=20, resolucion=50))

# Ponemos los contadores del precio de los objetos a 0
television = 0
lavadora = 0
electro = 0
i = 0

# Recorremos la lista para ver los el precio total que hay de cada tipo
for electrodomestico in electrodomesticos:
    i += 1
    electrodomestico.precioFinal()
    # Este if nos indica a la clase que pertenece el objeto para crearlo en esa misma clase y no en otra diferente
    # el primero nos indica si es un objeto de tipo televisor nos lo almacene en la variable television
    if isinstance(electrodomestico,Television):
        television += electrodomestico.precioBase
    # este nos coge solo los objetos lavadora y los mete en la variable lavadora
    elif isinstance(electrodomestico,Lavadora):
        lavadora += electrodomestico.precioBase
    # y por ultimo si no pertenece a ninguna de las anteriores nos lo almacena en la variable electro quedando el
    # precio de todos los electrodomesticos en total
    else:
        electro=electrodomestico.precioBase

# Mostramos el precio total de cada tipo por pantalla
print("Total de televisores: " + str(television))
print("Total de lavadoras: " + str(lavadora))
print("Total de electrodomésticos: " + str(electrodomestico)) # No da error pero no termina de funcionar correctamente (no se el porque)

print("Total: " + str(television+lavadora+electro))