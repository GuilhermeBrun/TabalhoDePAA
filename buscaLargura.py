import pdb

dicionarioEstados = {
0: 'AC',
1: 'AM',
2: 'RO',
3: 'PA',
4: 'RR',
5: 'AP',
6: 'MA',
7: 'TO',
8: 'PI',
9: 'CE',
10: 'RN',
11: 'PB',
12: 'PE',
13: 'AL',
14: 'SE',
15: 'BA',
16: 'MG',
17: 'ES',
18: 'RJ',
19: 'GO',
20: 'MT',
21: 'MS',
22: 'SP',
23: 'PR',
24: 'SC',
25: 'RS'}

grafo = [ [1, 2], #vizinhos do no 0
        [0, 2, 3, 4, 20], #vizinhos do no 1
        [0, 1, 20], #vizinhos do no 2
        [1, 4, 5, 6, 7, 20], #vizinhos do no 3
        [1, 3], #vizinhos do no 4
        [3], #vizinhos do no 5
        [3, 7, 8], #vizinhos do no 6
        [3, 6, 8, 15, 19, 20], #vizinhos do no 7
        [6, 7, 9, 12, 15], #vizinhos do no 8
        [8, 10, 11, 12], #vizinhos do no 9
        [9, 11], #vizinhos do no 10
        [9, 10, 12], #vizinhos do no 11
        [8, 9, 11, 13, 15], #vizinhos do no 12
        [12, 14, 15], #vizinhos do no 13
        [13, 15], #vizinhos do no 14
        [7, 8, 12, 13, 14, 16, 17, 19], #vizinhos do no 15
        [15, 17, 18, 19, 21, 22], #vizinhos do no 16
        [15, 16, 18], #vizinhos do no 17
        [16, 17, 22], #vizinhos do no 18
        [7, 15, 16, 20, 21], #vizinhos do no 19
        [1, 2, 3, 7, 19, 21], #vizinhos do no 20
        [16, 19, 20, 22, 23], #vizinhos do no 21
        [16, 18, 21, 23], #vizinhos do no 22
        [21, 22, 24], #vizinhos do no 23
        [23, 25], #vizinhos do no 24
        [24]] #vizinhos do no 25

def buscaLargura(noPartida, noChegada):
    fila = []
    fila.append(noPartida)
    while len(fila) > 0:
        no = fila.pop(0)
        nosVisitados[no] = 1
        print(dicionarioEstados[no])
     
        if no == noChegada:
            print("Chegou ao destino")
            break
        for i in grafo[no]:
            if nosVisitados[i] == 0:
                nosVisitados[i] = 1
                fila.append(i)

nosVisitados = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
noPartida = 0
noChegada = 25

buscaLargura(noPartida, noChegada)