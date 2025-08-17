import random

def imprimir_tabuleiro(tabuleiro):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            valor = tabuleiro[i][j]
            print(valor if valor != 0 else ".", end=" ")
        print()

def validar(tabuleiro, linha, coluna, numero):
    for j in range(9):
        if tabuleiro[linha][j] == numero:
            return False
    for i in range(9):
        if tabuleiro[i][coluna] == numero:
            return False
    inicio_linha = (linha // 3) * 3
    inicio_coluna = (coluna // 3) * 3
    for i in range(inicio_linha, inicio_linha + 3):
        for j in range(inicio_coluna, inicio_coluna + 3):
            if tabuleiro[i][j] == numero:
                return False
    return True

def preencher(tabuleiro):
    for i in range(9):
        for j in range(9):
            if tabuleiro[i][j] == 0:
                numeros = list(range(1, 10))
                random.shuffle(numeros)
                for num in numeros:
                    if validar(tabuleiro, i, j, num):
                        tabuleiro[i][j] = num
                        if preencher(tabuleiro):
                            return True
                        tabuleiro[i][j] = 0
                return False
    return True

def gerar_tabuleiro():
    tabuleiro = [[0 for _ in range(9)] for _ in range(9)]
    preencher(tabuleiro)
    return tabuleiro

def remover_numeros(tabuleiro, removidos=40):
    tentativas = removidos
    while tentativas > 0:
        linha = random.randint(0, 8)
        coluna = random.randint(0, 8)
        if tabuleiro[linha][coluna] != 0:
            tabuleiro[linha][coluna] = 0
            tentativas -= 1
    return tabuleiro

def jogar():
    tabuleiro = gerar_tabuleiro()
    remover_numeros(tabuleiro)
    tabuleiro_inicial = [linha[:] for linha in tabuleiro]
    while True:
        imprimir_tabuleiro(tabuleiro)
        entrada = input("Digite linha coluna valor (ex: 1 2 3) ou 'sair': ")
        if entrada.lower() == 'sair':
            print("Saindo do jogo.")
            break
        try:
            linha, coluna, valor = map(int, entrada.split())
            linha -= 1
            coluna -= 1
            if not (0 <= linha < 9 and 0 <= coluna < 9 and 1 <= valor <= 9):
                print("Valores fora do intervalo. Tente novamente.")
                continue
            if tabuleiro_inicial[linha][coluna] != 0:
                print("Você não pode alterar esta posição fixa.")
            elif not validar(tabuleiro, linha, coluna, valor):
                print("Movimento inválido.")
            else:
                tabuleiro[linha][coluna] = valor
        except Exception:
            print("Entrada inválida. Use o formato: linha coluna valor")

while True:
    print("1 - Jogar\n2 - Sair")
    entrada = input("Escolha uma opção: ")
    if entrada == '1':
        jogar()
    elif entrada == '2':
        print('Saindo do jogo...')
        break
    else:
        print('\n***Opção inválida!***\n')
