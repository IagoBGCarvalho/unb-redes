import socket

socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Cliente TCP iniciado.")

# Estabelece uma conexão com o servidor passando como parâmetro o endereço IP e a porta que identifica o processo do servidor na máquina onde o servidor TCP está executando
socketTCP.connect(("127.0.0.1", 2023))

while True:
    mensagem_usuario = input("\nDigite a mensagem (ou 'sair'): ")

    if mensagem_usuario.lower() == "sair":
        break

    # Envia uma mensagem pelo socket para o servidor no qual a conexão foi estabelecida Utilizando .encode() para transformar a string em um objeto bytes-like
    socketTCP.sendall(mensagem_usuario.encode())

    # Bloqueia a execução do processo esperando a resposta do servidor
    msg = socketTCP.recv(1024).decode()
    print(f"Resposta do servidor: {msg!r}")

# Fecha a conexão com o servidor
socketTCP.close()

# O problema aqui é se um cliente se conectar e não mandar nada, o servidor ficará preso no laço interno daquele cliente e ignorará totalmente outras conexões que tentem chegar na porta 2023
