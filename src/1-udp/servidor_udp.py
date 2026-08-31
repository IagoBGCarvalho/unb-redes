# Biblioteca responsável pelas funções do socket, que é a interface que permite às aplicações utilizarem de serviços da camada de transporte
# A camada de transporte é responsável por fazer o mapeamento da informação para uma determinada porta do computador
import socket

# Criando um objeto socket do tipo UDP a partir do parâmetro "socket.SOCK_DGRAM"
socketUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind do processo do servidor na porta 2023 e com o IP definido (localhost)
socketUDP.bind(("127.0.0.1", 2023))
print("Servidor UDP esperando mensagens!")

# A função "socketUDP.recvfrom()" lê e delimita a quantidade de bytes lidos da rede. No caso, irá ler 1024 bytes e atribuirá eles como valor do vetor, colocando a mensagem na primeira posição e o endereço do cliente na segunda. Normalmente travaria o fluxo de execução e só receberia uma mensagem por vez, mas usando um loop é possível receber múltiplas mensagens de múltiplos processos

while True:
    # Thread principal bloqueada enquanto o servidor espera as mensagens da rede chegarem.
    #Assim que um pacote chega, ela lê 1024 bytes e avança
    parMsgEndereco = socketUDP.recvfrom(1024)

    # Mensagem chegou! É necessário decodificar a mensagem de bytes para string
    msg = parMsgEndereco[0].decode()
    endereco = parMsgEndereco[1]

    msgCliente = "Mensagem do cliente:{}".format(msg)
    ipCliente = "Endereço IP do cliente:{}".format(endereco)
    print("\nNova requisição!")
    print(msgCliente)
    print(ipCliente)

    # Enviando uma mensagem de resposta para o cliente
    resposta = "Olá cliente da porta {}, mensagem recebida com sucesso!".format(endereco[1])
    socketUDP.sendto(str.encode("Mensagem para o cliente!"), endereco)
