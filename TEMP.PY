temperatura = []
for n in range (0,23):
    t = int(input("ingrese la temperatura"))
    temperatura.append(t)
    print (temperatura)

import random 
import tabulate

def generarTemperaturas():
    return round(random.uniform(0, 23) , 1)
salones = []
periodos=[mañana , tarde , noche]

for salon in range (10):
    tempraturas_salon = []
    for _ in range (3):
        