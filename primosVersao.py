#Gerador de números primos com 18 algarismos
import threading
import random
import concurrent.futures

#Gerar um número aleatório com 18 algarismo
#Validar se é primo
#Rodar o código no thread main

maximo = 10
primos = 0
array = []
lock = threading.Lock

def th_gerador_numero(index): #Como se fosse um deamon, rondar em segundo plano, sem mostrar
    global primos
    print("Thread", index)
    lista = list()
    for i in range(maximo):
        numero_aleatorio = random.randint(10**15, 10**16 - 1)
        if eh_primo(numero_aleatorio):
            lista.append(numero_aleatorio)
            #print(numero_aleatorio)
            primos = primos + 1           
    array.append(lista)
    
def eh_primo(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(th_gerador_numero, range(10))
    print(array)
    contador = 0
    for sublista in array:
        for _ in sublista:
            contador = contador + 1
    print(primos)
    print (contador)
    print("Quando se olha demais para o abismo, ele te olha te volta")

    #diferença entre start e run, run ele organiza e o start inicia, usar o start