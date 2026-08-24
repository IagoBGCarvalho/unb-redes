import socket

# Criando socket TCP com "socket.SOCK_STREAM"
socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind do processo na porta 2023
socketTCP.bind(("127.0.0.1", 2023))
# Após fazer o bind é necessário usar "listen()" para preparar o socket para aceitar novas conexões
socketTCP.listen()
print("Servidor TCP esperando novas conexões!")

while True:
    # Servidor bloqueia esperando por novas conexões.
    # O TCP é orientado a conexão, então além de esperar novas conexões, uma vez que o cliente conecta, ele bloqueia a execução e espera as mensagens do cliente.
    # A partir do momento que o servidor estabelece a conexão, o método "accept()" retorna um outro objeto socket exclusivi para enviar e receeber mensagens com o cliente que se conectou
    socketCliente, endereco = socketTCP.accept()
    print(f"Conexão realizada! Endereço do cliente:{endereco}")

    # Conexão feita, esperando requisição do cliente através do objeto exclusivo para a conexão estabelecida
    msg = socketCliente.recv(1024).decode()

    # Mensagem chegou!
    print(msg)

    # Enviando resposta para o cliente através do socket exclusivo
    socketCliente.sendall(str.encode("Resposta do servidor!"))
    # Encerra a conexão com o cliente e finaliza a execução

socketCliente.close()
