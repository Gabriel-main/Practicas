def sum_mul(n, m):
    sumaFinal = 0

  #aqui hacemos una verificacion solo entren numeros positivos
    if n <= 0 or m <= 0:
        return 'INVALID'
    
    else:
      #Aqui hace la suma hasta que llegue al limite de m
        for i in range(m):
            if i % n == 0:
                sumaFinal += i
    
    return sumaFinal
