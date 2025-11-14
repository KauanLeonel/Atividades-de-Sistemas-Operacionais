import subprocess
import shutil

# result = subprocess.run(["netstat", "-a"], shell = True, capture_output= True, text = True)

# print(result)

#subprocess.run(["Comando que pode falhar"], shell = True)

#shutil.copy('arquivo.txt', 'C:/Users/cg3033775/Documents/Códigos/Atividades-de-Sistemas-Operacionais/arquivoteste.txt')

# info = shutil.disk_usage('C:/Users')
# print ("Espaço total: ", info.total / (1024 ** 3))
# print ("Espaço livre: ", info.free  / (1024 ** 3)) 
# print ("Espaço usado: ", info.used  / (1024 ** 3))


# copia diretorio sem perder metadados
# shutil.copytree('diretorio_origem', 'caminho/para/destino')


# #move um arquivo
# shutil.move('arquivo.txt', 'novo_diretorio/arquivo_movido.txt')


# #remove um diretorio
# shutil.rmtree('diretorio_para_excluir')


# info = shutil.disk_usage('/caminho/do/diretorio')
# print("Espaço Total:", info.total)
# print("Espaço Usado:", info.used)
# print("Espaço Livre:", info.free)


# ##########################################################


# #cria um arquivo compactado de um diretorio
# shutil.make_archive('arquivo_zip', 'zip', 'diretorio_a_zipar')


# #descompacta um arquivo
# shutil.unpack_archive('arquivo_zip.zip', 'diretorio_destino')


# import os


# # Exemplo de uso: listar o conteúdo do diretório atual
# print(os.listdir())


# print(os.name)


# username = os.environ.get('USERNAME')
# print(f"Username: {username}")


# diretorio_atual = os.getcwd()
# print(f"Diretório atual: {diretorio_atual}")


# os.chdir('caminho/para/diretorio')
# os.mkdir('novo_diretorio')


# os.system('ls')


# with open("arquivo.txt", "r") as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)
#     arquivo.close()


# # Lendo todas as linhas em uma lista
# with open("arquivo.txt", "r", encoding="utf-8") as arquivo:
#     linhas = arquivo.readlines()
#     print(f"O arquivo tem {len(linhas)} linhas")
#     for i, linha in enumerate(linhas):
#         print(f"Linha {i+1}: {linha.strip()}")


# with open("arquivo.txt", "a", encoding="utf-8") as arquivo:
#         arquivo.write("So if gotta let me now\n")
#         arquivo.write("Should i stay?\n")
#         arquivo.write("Or should i go?\n")


#         # Lendo com cabeçalhos
# with open("dados.csv", "r", encoding="utf-8", newline="") as arquivo:
#     leitor = csv.DictReader(arquivo)  # Usa a primeira linha como chaves
#     for linha in leitor:
#         print(linha)  # linha é um dicionário
#         print(f"Nome: {linha['nome']}, Idade: {linha['idade']}")

# # Especificando delimitador
# with open("dados.tsv", "r", encoding="utf-8", newline="") as arquivo:
#     leitor = csv.reader(arquivo, delimiter="\t")  # Tabulação como delimitador
#     for linha in leitor:
#         print(linha)


import json

# Criando um dicionário
pessoa = {
    "nome": "João Silva",
    "idade": 30,
    "cidade": "São Paulo",
    "habilidades": ["Python", "JavaScript", "SQL"],
    "ativo": True,
    "contatos": {
        "email": "joao@exemplo.com",
        "telefone": "123-456-789"
    }
}

# # # Salvando como JSON
# # with open("pessoa.json", "w", encoding="utf-8") as arquivo:
# #     json.dump(pessoa, arquivo, indent=4, ensure_ascii=False)
# #     # indent: formata o JSON para fácil leitura
# #     # ensure_ascii=False: preserva caracteres não-ASCII (acentos, etc.)

# # # Convertendo para string JSON
# # json_str = json.dumps(pessoa, indent=4, ensure_ascii=False)
# # print(json_str)

# # # Salvando uma lista de objetos
# # pessoas = [
# #     {"nome": "João", "idade": 30},
# #     {"nome": "Maria", "idade": 25},
# #     {"nome": "Pedro", "idade": 40}
# # ]

# # with open("pessoas.json", "w", encoding="utf-8") as arquivo:
# #     json.dump(pessoas, arquivo, indent=4, ensure_ascii=False)

# import json

# # Lendo um arquivo JSON
# with open("pessoas.json", "r", encoding="utf-8") as arquivo:
#     dados = json.load(arquivo)

# print(type(dados))  # <class 'dict'> ou <class 'list'> dependendo do JSON

# # Acessando dados
# if isinstance(dados, dict):
#     print(f"Nome: {dados.get('nome')}")
#     print(f"Idade: {dados.get('idade')}")
# elif isinstance(dados, list):
#     for item in dados:
#         print(f"Item: {item}")

# # Lendo arquivo binário
# with open("kid.jpg", "rb") as arquivo:
#     dados = arquivo.read()
#     print(f"Tamanho: {len(dados)} bytes")
#     print(f"Primeiros bytes: {dados[:10].hex()}")

# # Escrevendo arquivo binário
# dados_binarios = bytes([0x48, 0x65, 0x6C, 0x6C, 0x6F])  # "Hello" em ASCII
# with open("dados.bin", "wb") as arquivo:
#     arquivo.write(dados_binarios)

# Precisa instalar: pip install Pillow
from PIL import Image

# Abrir uma imagem
imagem = Image.open("kid.jpg")
print(f"Formato: {imagem.format}")
print(f"Tamanho: {imagem.size}")
print(f"Modo: {imagem.mode}")

# Redimensionar
imagem_redimensionada = imagem.resize((800, 600))
imagem_redimensionada.save("foto_redimensionada.jpg")

# Converter para escala de cinza
imagem_pb = imagem.convert("L")
imagem_pb.save("foto_pb.jpg")

# Recortar
area = (100, 100, 400, 400)  # (left, upper, right, lower)
imagem_recortada = imagem.crop(area)
imagem_recortada.save("foto_recortada.jpg")