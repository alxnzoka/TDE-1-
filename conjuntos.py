#Alan Filipe
#Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
#linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
#operações que serão realizadas entre dois conjuntos de dados.
#O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
#contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
#em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
#segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
#operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
#seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
#operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
#terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
#das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
#4
#U
#3, 5, 67, 7
#1, 2, 3, 4
#I
#1, 2, 3, 4, 5
#4, 5
#D
#1, A, C, 34
#A, C, D, 23
#C
#3, 4, 5, 5, A, B, R
#1, B, C, D, 1
def realizar_operacoes(arquivo):
    with open("teste1.txt", 'r') as f:
        linhas = f.readlines()

    num_operacoes = int(linhas[0].strip())
    resultados = []
    linha_atual = 1

    for _ in range(num_operacoes):
        operacao = linhas[linha_atual].strip()
        conjunto1 = set(linhas[linha_atual + 1].strip().split(", "))
        conjunto2 = set(linhas[linha_atual + 2].strip().split(", "))

        if operacao == 'U':
            resultado = conjunto1.union(conjunto2)
            descricao = f"União: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"

        elif operacao == 'I':
            resultado = conjunto1.intersection(conjunto2)
            descricao = f"Interseção: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"

        elif operacao == 'D':
            resultado = conjunto1.difference(conjunto2)
            descricao = f"Diferença: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"

        elif operacao == 'C':
            resultado = {(x, y) for x in conjunto1 for y in conjunto2}
            descricao = f"Produto Cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"

        resultados.append(descricao)
        linha_atual += 3

    return resultados


# Função principal que lê o arquivo e exibe os resultados
def main():
    arquivo_teste = "teste1.txt"
    resultados = realizar_operacoes("teste1.txt")

    for resultado in resultados:
        print(resultado)


# Chamar a função principal
if __name__ == "__main__":
    main()
