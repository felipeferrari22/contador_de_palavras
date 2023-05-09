# Contador de Palavras

<img src="https://builtin.com/sites/www.builtin.com/files/styles/og/public/hero-python-data-science-courses.jpg" width="750px" height="300px">

**Este Repositório trata-se de um projeto em Python, desenvolvido para a disciplina de Arquiteturas Cloud do curso de Big Data no Agronegócio.**

Inicialmente, criei um arquivo .txt, chamado de 'palavras.txt', e criei a seguinte função para abrí-lo no script em Python:

    def abrir_arquivo(arquivo):
      with open(arquivo, 'r') as arq:
          texto = arq.read()
      return texto
Após a primeira função ter sido criada, parti para a segunda, criando a função para remover os acentos do arquivo .txt:

    def remover_acentos(texto):
      return unidecode(texto)
A terceira função, que realiza a contagem das palavras e as exibe de forma decrescente foi desenvolvida da seguinte maneira:

    def contar_palavras(texto):
    palavras = texto.lower().split()
    contador = Counter(palavras)
    ranking = contador.most_common()
    for palavra, frequencia in ranking:
        print(f"{palavra}: {frequencia}")
Já a função para contar a quantidade de vezes que uma palavra específica aparece no texto, funciona desta forma:

    def procurar_palavras(texto):
      palavras = texto.lower().split()
    contador = Counter(palavras)
    palavras_procuradas = input('Insira as palavras que deseja procurar (separadas por vírgula): ').split(',')
    for palavra in palavras_procuradas:
        frequencia = contador.get(palavra.strip(), 0)
        print("A palavra",palavra.strip(),"aparece",frequencia,"vez/vezes no arquivo.")
E, por último, a função que exibe as palavras com mais e com menos aparições no texto, é a seguinte:

    def maiscomum_menoscomum(texto):
      palavras = texto.lower().split()
      contador = Counter(palavras)
      mais_comum = contador.most_common(1)[0][0]
      n_mais_comum = contador.most_common(1)[0][1]
      menos_comum = contador.most_common()[-1][0]
      n_menos_comum = contador.most_common()[-1][1]
      print("A palavra com mais aparições é", mais_comum, "com", n_mais_comum, "aparição/aparições.")
      print("A palavra com menos aparições é", menos_comum, "com", n_menos_comum, "aparição/aparições.")
