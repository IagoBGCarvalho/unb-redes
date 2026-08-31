# Funcionamento semelhante ao servidor TCP apresentado anteriormente, 
# com a principal diferença sendo o uso de threads!

# Após o método accept() retornar uma nova conexão, o servidor cria uma thread que
# executa a função tratar_cliente

# Enquanto a thread criada trata a comunicação om o cliente, 
# o processo principal do servidor retorna imediatamente ao laço de repetição e
# permanece disponível para aceitar novas conexões!

# Dessa forma, múltiplos clientes podem ser atendidos simultaneamente, cada um em uma thread!

# É possível usar o cliente_tcp.py para testar!

import socket
import threading

def tratar_cliente(conn, endereco):
    print(f"Conexão estabelecida com {endereco}")

    while True:
        dados = conn.recv(1024)

        if not dados:
            break

        mensagem = dados.decode()
        print(f"Mensagem de {endereco}: {mensagem}")

        resposta = f"Servidor recebeu: {mensagem}"
        conn.sendall(resposta.encode())

    print(f"Conexao encerrada com {endereco}")
    conn.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", 2023))
servidor.listen()

print("Servidor TCP concorrente aguardando conexoes...")

while True:
    conn, endereco = servidor.accept()

    thread_cliente = threading.Thread(
        target=tratar_cliente,
        args=(conn, endereco)
    )

    thread_cliente.start()
