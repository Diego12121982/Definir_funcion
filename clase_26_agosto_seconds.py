"""
escribir un funcion que permita calcular la duracion en segundos
de un intervalo dado en horas,minutos y segundos
"""

def total(horas, minutos, segundos):

    horas = horas*3600
    minutos = minutos*60
    segundos = segundos
    resul_total = horas+minutos+segundos
    
    return resul_total

horas = int(input("ingrese las horas: "))
minutos = int(input("ingrese los minutos: "))
segundos = int(input("ingrese los segundos: ")) 


print("las horas en segundos son: {} " .format(horas*3600))
print("los minutos en segundos son: {} " .format(minutos*60))
print("los segundos son: {} " .format(segundos))
resul_total = total(horas, minutos, segundos)   

print("el resultado total en segundos es :  " , resul_total) 
    
print("buen trabajo")   