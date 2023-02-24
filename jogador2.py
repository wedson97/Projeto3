# Grupo:
# Wedson Cândido da Silva
# Maria Clara Luna Alves
# João Paulo Pereira de Lima
import os
import threading
import socket


def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect(('localhost', 1234))
        print('cliente conectado')
    except:
        return print('erro')
    while True:
        tela()
        jogador1(cliente)
        vit = verificarVitoria()
        if (vit != 'n') or (jogadas >= maxJogadas):
            break
        jogador2(cliente)
        vit = verificarVitoria()
        if (vit != 'n') or (jogadas >= maxJogadas):
            break

    print('FIM DE JOGO')
    if (vit == 'X' or vit == 'O'):
        print('Resultado: Jogador ' + vit + ' Venceu')
    else:
        print('Reultado: Empate')
    jogarNovamente = input('Jogar novamente [s/n]:')
    if jogarNovamente.lower() == 's':
        redefinir()
    else:
        cliente.close()


jogarNovamente = 's'
jogadas = 0
quemJoga = 1
maxJogadas = 9
vit = 'n'
velha = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def tela():
    global velha
    global jogadas
    os.system('cls')
    print('    0   1   2')
    print('0:  '+velha[0][0] + ' | '+velha[0][1]+' | ' + velha[0][2])
    print('   -----------')
    print('1:  '+velha[1][0] + ' | '+velha[1][1]+' | ' + velha[1][2])
    print('   -----------')
    print('2:  '+velha[2][0] + ' | '+velha[2][1]+' | ' + velha[2][2])
    print('Jogadas: ' + str(jogadas))

# daqui pra baixo eu acho que vai pra o socket


def jogador1(cliente):
    print('Vez de jogar: Jogador 1')
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        try:
            linha = int(cliente.recv(2048).decode('utf-8'))
            coluna = int(cliente.recv(2048).decode('utf-8'))
            velha[linha][coluna] = 'X'
            quemJoga = 2
            jogadas += 1
        except:
            print('Linha e/ou coluna são invalidos')
            os.system("pause")
    tela()


def jogador2(cliente):
    print('Vez de jogar: Jogador 2')
    global jogadas
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            while velha[linha][coluna] != ' ':
                linha = int(input('Linha: '))
                coluna = int(input('Coluna: '))
            velha[linha][coluna] = 'O'
            quemJoga = 1
            jogadas += 1
        except:
            return
    tela()
    linha = str(linha).encode()
    coluna = str(coluna).encode()
    cliente.send(linha)
    cliente.send(coluna)


def verificarVitoria():
    global velha
    vitoria = 'n'
    simbolos = ['X', 'O']
    for s in simbolos:
        vitoria = 'n'

        # Verifica linhas

        il = ic = 0
        while il < 3:
            soma = 0
            ic = 0
            while ic < 3:
                if (velha[il][ic] == s):
                    soma += 1
                ic += 1
            if (soma == 3):
                vitoria = s
                break
            il += 1
        if (vitoria != 'n'):
            break

        # Verifica colunas

        il = ic = 0
        while ic < 3:
            soma = 0
            il = 0
            while il < 3:
                if (velha[il][ic] == s):
                    soma += 1
                il += 1
            if (soma == 3):
                vitoria = s
                break
            ic += 1
        if (vitoria != 'n'):
            break

        # Verifica diagonal 1

        soma = 0
        indiag = 0
        while indiag < 3:
            if (velha[indiag][indiag] == s):
                soma += 1
            indiag += 1
        if (soma == 3):
            vitoria = s
            break

        # Verifica diagonal 1
        soma = 0
        indiagl = 0
        indiagc = 2
        while indiagc >= 0:
            if (velha[indiagl][indiagc] == s):
                soma += 1
            indiagl += 1
            indiagc -= 1
        if (soma == 3):
            vitoria = s
            break
    return vitoria


def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogadas
    global vit
    jogadas = 0
    quemJoga = 1
    maxJogadas = 9
    vit = 'n'
    velha = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]


while (jogarNovamente != 'n'):
    main()
