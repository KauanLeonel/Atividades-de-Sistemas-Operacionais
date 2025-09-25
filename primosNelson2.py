#Gerador de números primos com 18 algarismos
import threading
import random
import concurrent.futures

#Gerar um número aleatório com 18 algarismo
#Validar se é primo
#Rodar o código no thread main

maximo = 10

def th_gerador_numero(index): #Como se fosse um deamon, rondar em segundo plano, sem mostrar
    print("Thread", index)
    for i in range(maximo):
        numero_aleatorio = random.randint(10**17, 10**18 - 1)
        if eh_primo(numero_aleatorio):
            print(numero_aleatorio)
    
def eh_primo(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(th_gerador_numero, range(10))
    print("Quando se olha demais para o abismo, ele te olha te volta")

    #diferença entre start e run, run ele organiza e o start inicia, usar o start