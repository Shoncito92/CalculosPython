import bs4
import requests
import paquete_cientifico

a=1
b=9
print("la suma es:")
print(a+b)
print(bs4.__version__)

print("numero pi desde modulo:")
print(paquete_cientifico.PI)
print("velocidad de la luz desde modulo:")
print(paquete_cientifico.C)

#dimensiones cilindro
radio_cilindro=10
altura_cilindro=5
#calculo de area base cilindro
area_base = paquete_cientifico.PI * radio_cilindro * radio_cilindro
#calculo de volumen cilindro
volumen_cilindro = paquete_cientifico.vol_cilindro(altura_cilindro, area_base)
print("volumen cilindro:")
print(volumen_cilindro)

#multiplicacion de a y b 
multiplicacion = paquete_cientifico.multiplica(a, b)
print("la mutiplicacion es:")
print(multiplicacion)
