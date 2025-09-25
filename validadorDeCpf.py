import random
import concurrent.futures


def th_gerador_numero(index):
    numero_aleatorio = random.randint(10**10, 10**11 - 1)
    if(th_validar_cpf(numero_aleatorio)):
        return numero_aleatorio
    

def th_validar_cpf(cpf) -> bool:
    cpf = str(cpf)
    if cpf == cpf[0] * 11:
        return False
    
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    return digito1 == int(cpf[9]) and digito2 == int(cpf[10])

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        resultado = list(executor.map(th_gerador_numero, range(100000)))
    print("CPFS:", resultado)