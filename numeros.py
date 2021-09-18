"""
el codigo permite reconocer los numeros positivos y negativos y de el mismo modo diferenciarlos
18/9/2021
"""
numeros = [56,32,-7,6,-1.45,4,19,45,0,15]
#           0 1  2  3   4   5  6  7  8 9
print (numeros[8])
def numerospositivos (e):
    if e > 0:
        print ("este numero es positivo :)")

numerospositivos(numeros[8])

def numerosnegativos (e):
    if e <0:
        print ("este numero es negativo :3")
        
numerosnegativos(numeros[8])

def numero (e):
    if e == 0:
        print ("es cero")

numero(numeros[8])