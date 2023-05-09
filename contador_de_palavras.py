from unidecode import unidecode
from collections import Counter

with open('palavras.txt', 'r') as arq:
    texto = arq.read()

def abrir_arquivo(arquivo):
    with open(arquivo, 'r') as arq:
        texto = arq.read()
    return texto

def remover_acentos(texto):
    return unidecode(texto)

def contar_palavras(texto):
    palavras = texto.lower().split()
    contador = Counter(palavras)
    ranking = contador.most_common()
    for palavra, frequencia in ranking:
        print(f"{palavra}: {frequencia}")

def procurar_palavras(texto):
    palavras = texto.lower().split()
    contador = Counter(palavras)
    palavras_procuradas = input('Insira as palavras que deseja procurar (separadas por vírgula): ').split(',')
    for palavra in palavras_procuradas:
        frequencia = contador.get(palavra.strip(), 0)
        print("A palavra",palavra.strip(),"aparece",frequencia,"vez/vezes no arquivo.")

def maiscomum_menoscomum(texto):
    palavras = texto.lower().split()
    contador = Counter(palavras)
    mais_comum = contador.most_common(1)[0][0]
    n_mais_comum = contador.most_common(1)[0][1]
    menos_comum = contador.most_common()[-1][0]
    n_menos_comum = contador.most_common()[-1][1]
    print("A palavra com mais aparições é", mais_comum, "com", n_mais_comum, "aparição/aparições.")
    print("A palavra com menos aparições é", menos_comum, "com", n_menos_comum, "aparição/aparições.")

menu = int
while menu != 0:
    print("\nOlá!")
    print("1 - Abrir arquivo")
    print("2 - Remover acentos")
    print("3 - Contar palavras")
    print("4 - Quantidade de aparições de uma palavra específica")
    print("5 - Exibir a palavra com mais aparições e a com menos aparições.")
    print("0 - Sair")
    menu = int(input("Insira o número que corresponde a qual atividade você deseja realizar: "))

    if menu == 1:
        arquivo = input('Insira o nome do arquivo: ')
        texto = abrir_arquivo(arquivo)
        print(texto)
    
    elif menu == 2:
        print(remover_acentos(texto))

    elif menu == 3:
            contar_palavras(texto)
    
    elif menu == 4:
        print(procurar_palavras(texto))

    elif menu == 5:
            maiscomum_menoscomum(texto)
    
    elif menu == 0:
        print()
    
    else:
        print("\nNúmero inválido.")

print("Obrigado por utilizar o Contador de Palavras!")