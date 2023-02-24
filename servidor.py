# Grupo:
# Wedson Cândido da Silva
# Maria Clara Luna Alves
# João Paulo Pereira de Lima
import threading
import socket


clientes = []


def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 1234))
        server.listen(2)
        print('Servidor inicializado!')
    except:
        return print('\nNão foi posível se conectar ao servidor!\n')
    while True:
        cliente, addr = server.accept()
        clientes.append(cliente)
        thread = threading.Thread(target=tratamentoMensagem, args=[cliente])
        thread.start()


def tratamentoMensagem(cliente):
    while True:
        try:
            msg = cliente.recv(2048)
            broadcast(msg, cliente)
        except:
            break


def broadcast(msg, cliente):
    for clientesItem in clientes:
        if clientesItem != cliente:
            try:
                clientesItem.send(msg)
            except:
                pass


main()
