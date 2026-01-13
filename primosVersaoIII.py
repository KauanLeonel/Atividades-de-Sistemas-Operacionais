#Gerador de números primos com 18 algarismos
import threading
import random
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
    index = 0
    #for index in range(5):
    x = threading.Thread(target = th_gerador_numero, args = (index,)) #Tá rodando o thread
    x.start()
    x.join() #Enquanto os filhotes não terminarem, vai ficar rodando
    print("Quando se olha demais para o abismo, ele te olha te volta")

    #diferença entre start e run, run ele organiza e o start inicia, usar o start