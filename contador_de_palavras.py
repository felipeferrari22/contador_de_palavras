from unidecode import unidecode

menu = int
while menu != 0:
    print("Olá!")
    print("1 - Abrir arquivo")
    print("2 - Remover acentos")
    print("3 - Contar palavras")
    print("4 - Quantidade de aparições de uma palavra específica")
    print("5 - Exibir a palavra com mais aparições e a com menos aparições.")
    print("0 - Sair")
    menu = int(input("Insira o número que corresponde a qual atividade você deseja realizar: "))


    if menu == 1:
        arq = open("palavras.txt")
        print(arq)
    
    # elif menu == 2:
    #     arq_sem_acento = unidecode(arq)
    #     print(arq_sem_acento)

    # elif menu == 4:
    #     palavra = str(input("Insira a palavra que deseja contar: "))
    #     arq.count(palavra)

print("Obrigado por utilizar o Contador de Palavras!")