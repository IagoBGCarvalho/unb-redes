import socket

# Criando socket UDP
socketUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

print("Cliente UDP iniciado. Digite 'sair' para encerrar.")

while True:
    mensagem_usuario = input("\nDigite a mensagem: ")

    if mensagem_usuario.lower() == "sair":
        break

    # Enviando requisição para o servidor.
    # O cliente não precisa fazer o bind em alguma porta pois ele apenas envia requisições e recebe respostas a partir de suas requisições
    socketUDP.sendto(str.encode(mensagem_usuario), ("127.0.0.1", 2023))

    # Lendo resposta do servidor. Thread será bloqueada até receber uma mensagem de volta da requisição
    resposta = socketUDP.recvfrom(1024)

    # Imprimindo mensagem do servidor na tela
    msg = "Mensagem do servidor:{}".format(resposta[0].decode())
    print(msg)

socketUDP.close()
