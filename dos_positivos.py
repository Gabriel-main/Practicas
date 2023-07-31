def two_are_positive(a, b, c):
    numeros = [a,b,c]
    dos_true = 0

  #Aqui hace la comparacion si hay numeros positivos
    for i in range(len(numeros)):
        if numeros[i] > 0:
            dos_true += 1

  #Aqui comprueba solo dos numeros positivos sale True, si sale mas de dos o menos sale False   
    if dos_true == 2:
        return True
    else:
        return False
