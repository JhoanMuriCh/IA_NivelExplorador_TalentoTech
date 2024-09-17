distancia, velocidad, tiempo = input().split()
distancia = float(distancia)
velocidad = float(velocidad)
tiempo = float(tiempo)  
velocidad_media = (distancia/1000) / (tiempo/3600)
if distancia < 0 or velocidad < 0 or tiempo < 0:
    print("ERROR")
elif velocidad_media <= velocidad:
    print("OK")
elif velocidad_media > velocidad and velocidad_media < velocidad*1.2:
    print("MULTA")
else:
    print("CURSO SENSIBILIZACION")



