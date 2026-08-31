import socket

# Criando socket TCP com "socket.SOCK_STREAM"
socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind do processo na porta 2023
socketTCP.bind(("127.0.0.1", 2023))

# Após fazer o bind é necessário usar "listen()" para preparar o socket para aceitar novas conexões
socketTCP.listen()
print("Servidor TCP esperando novas conexões!")

# Laço externo: responsável por manter o servidor vivo para aceitar novas conexões
while True:
    # Servidor bloqueia esperando até um novo cliente se conectar

    # A partir do momento que o servidor estabelece a conexão, o método "accept()" retorna um outro objeto socket exclusivo para enviar e receber mensagens com o cliente que se conectou
    socketCliente, endereco = socketTCP.accept()
    print(f"\n[+] Conexão realizada! Endereço do cliente:{endereco}")

    # Laço interno: responsável por receber múltiplas mensagens do mesmo cliente
    while True:
        # Conexão feita, esperando requisição do cliente através do objeto exclusivo para a conexão estabelecida
        msg = socketCliente.recv(1024).decode()

        # Se o cliente fechar a conexão, recv() retorna vazio. Precisamos tratar isso para não entrar em loop infinito.
        if not msg:
            print(f"[-] Cliente {endereco} encerrou a conexão.")
            break

        # Mensagem chegou!
        print(msg)

        # Enviando resposta para o cliente através do socket exclusivo[cite: 2]
        resposta = f"Servidor recebeu sua mensagem: {msg}"
        socketCliente.sendall(resposta.encode()) # Convertendo para bytes

    # Encerra a conexão com o cliente atual apenas após o laço interno quebrar
    socketCliente.close()
    print("Aguardando próximo cliente...")
