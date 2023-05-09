from unidecode import unidecode
from collections import Counter

with open('palavras.txt', 'r') as arq:
    texto = arq.read()

def carregar_arquivo(arquivo):
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
        print(f'{palavra}: {frequencia}')

def procurar_palavras(texto):
    palavras = texto.lower().split()
    contador = Counter(palavras)
    palavras_procuradas = input('Digite as palavras que deseja procurar (separadas por vírgula): ').split(',')
    for palavra in palavras_procuradas:
        frequencia = contador.get(palavra.strip(), 0)
        print("A palavra",palavra.strip(),"aparece",frequencia,"vez/vezes no arquivo.")

def exibir_extremos(texto):
    palavras = texto.lower().split()
    contador = Counter(palavras)
    palavra_mais_frequente = contador.most_common(1)[0][0]
    frequencia_mais_frequente = contador.most_common(1)[0][1]
    palavra_menos_frequente = contador.most_common()[-1][0]
    frequencia_menos_frequente = contador.most_common()[-1][1]
    print(f'A palavra com mais aparições é "{palavra_mais_frequente}" com {frequencia_mais_frequente} aparições.')
    print(f'A palavra com menos aparições é "{palavra_menos_frequente}" com {frequencia_menos_frequente} aparições.')

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
        arquivo = input('Digite o nome do arquivo: ')
        texto = carregar_arquivo(arquivo)
        print(texto)
    
    elif menu == 2:
        print(remover_acentos(texto))

    elif menu == 3:
        if not 'texto' in locals():
            print('É necessário carregar um arquivo antes de contar as palavras.')
        else:
            contar_palavras(texto)
    
    elif menu == 4:
        print(procurar_palavras(texto))

    elif menu == 5:
            exibir_extremos(texto)
    
    elif menu == 0:
        print()
    
    else:
        print("\nNúmero inválido.")

print("Obrigado por utilizar o Contador de Palavras!")