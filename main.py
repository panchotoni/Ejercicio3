import math

peso = int(input("Digite su peso: "))
altura= float(input("Digite su altura: "))

masa = peso / (math.pow(altura, 2))
masa2 = round(masa, 2)
print(f"Tu masa corporal es de: {masa2}")