# Tendencias e Innovacion en Tecnologias Agricolas (TEA)
from unicodedata import numeric


minutos_srt = input ("minutos jugados? ")
print(minutos_srt)
print(type(minutos_srt))
valorPorMinutos_srt = input ("valor por minuto")
print(valorPorMinutos_srt)
print(type(valorPorMinutos_srt))

# se utiliza la conversion de tipo a int
# sino se hace la conversion existira error porque trata de multiplicar strings
# calculando el valor total de las minutos jugados
numeric = [int(minutos_srt)*int(valorPorMinutos_srt)]
print(numeric)