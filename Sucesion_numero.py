import time

print("Sucesion de numero naturales.")

conteo = 1
suma = 0

# Inicio del bucle.
while True:
    
    # Variable para el numero.
    n = (int(input("Ingrese un numero:")))
    time.sleep(1) #Pausa un momento, para que tenga estilo xDDDD
    
    if(n <= -1): # Condicion para salir del bucle.
        print("-----------")
        conteo -= 1
        break
    else: 
        print("--------------\n"+"Sucesion "+str(conteo)+ # Muestra cuanta veces vas el numero
              "\nIngresate el numero:"+str(n)+
              "\n---------------")
        conteo += 1 # Aumenta el contador
        suma = suma + n #Almacena los valores y suma de una vez.
        
promedio = suma / conteo # saca el promedio.
    

print("Suma total de los valores: "+str(suma)+
      "\nEl promedio es:"+str(promedio)+"\n------------")

print("Total de numero ingresado: "+str(conteo))
