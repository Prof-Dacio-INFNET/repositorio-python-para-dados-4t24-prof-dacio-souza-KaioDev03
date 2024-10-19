""" Desafio

Crie uma função que recebe uma matriz (lista de listas) e retorna transposta dessa matriz. """

matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
# print(matriz,"-"*40, sep="\n\n")

for linha, _ in enumerate(matriz):
    for coluna, _ in enumerate(matriz[linha]):
        print(matriz[coluna][linha], end=" ") #Invertendo o padrão da matriz(linha,coluna) podemos inverter e fazer retornar uma matriz transposta.
    print("")