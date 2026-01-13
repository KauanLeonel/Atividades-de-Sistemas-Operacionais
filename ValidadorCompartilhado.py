import random
import concurrent.futures
from queue import Queue
import threading    

fila = Queue()
contador = 0
cpf_validos = Queue()  # PARÊNTESES!!!
lock = threading.Lock()

def th_contador(index):
    global contador
    # gera 10 CPFs e coloca na fila
    for _ in range(10):
        fila.put(th_gerador_numero())

    # valida cada CPF da fila
    while not fila.empty():
        cpf = fila.get()
        if th_validar_cpf(cpf):
            cpf_validos.put(cpf)
        else:
            with lock:
                contador += 1

def th_gerador_numero():
    # sempre retorna uma string de 11 dígitos
    return str(random.randint(10**10, 10**11 - 1))

def th_validar_cpf(cpf) -> bool:
    cpf = str(cpf)
    if cpf == cpf[0] * 11:
        return False
    try:
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        digito1 = (soma * 10 % 11) % 10
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        digito2 = (soma * 10 % 11) % 10
        return digito1 == int(cpf[9]) and digito2 == int(cpf[10])
    except ValueError:
        return False  # caso algum caractere não seja numérico

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        list(executor.map(th_contador, range(5000)))

    print("CPFs válidos:", list(cpf_validos.queue))
    print("CPFs inválidos:", contador)
