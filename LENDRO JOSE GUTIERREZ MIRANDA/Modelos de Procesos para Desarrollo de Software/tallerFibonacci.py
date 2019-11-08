#NO RECURSIVO
numInicial=0
numFinal=1
var =0
posicion = 1;

ValorIngresado =int(input("Favor ingresar el valor maximo"))

while (posicion < ValorIngresado):        
            var = numInicial+numFinal
            numInicial=numFinal
            numFinal = var
            posicion = posicion +1         
print("en la posicion",posicion,"el valor es :",var)


#recursivo

def vFibonacci (valor):
    if (valor==0):
        return valor
    elif (valor==1):
        return valor
    else:
        return vFibonacci(valor-2) + vFibonacci(valor-1)    
valor = int(input("Favor ingresar valor="))
vFibonacci(valor)