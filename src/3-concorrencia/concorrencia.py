# Concorrência é a técnica que permite que múltiplas partes de um programa sejam executadas sobrepostas no tempo.

# No Python uma das formas mais simples de introduzir concorrência é por meio do uso de threads.

# Uma thread pode ser entendida como uma linha de execução dentro de um processo
# Um programa pode possuir várias threads executando simultaneamente
# Cada uma é responsável por uma tarefa específica!

import threading # Biblioteca para concorrência
import time # Biblioteca que serve para monitorar tempo para poder pausar a thread por 1 segundo

def tarefa(nome):
    for i in range(3):
        print(f"{nome} executando passo {i}")
        time.sleep(1)

# As duas threads executam a mesma função, cada ume imprimindo mensagens na tela ao longo do tempo
t1 = threading.Thread(target=tarefa, args=("Thread 1"))
t2 = threading.Thread(target=tarefa, args=("Thread 2"))

# Start() ativa o gatilho da thread e faz ela ser executada, mas sem parar o fluxo principal do código
t1.start()
t2.start()

# Join() pausa a execução principal até que a thread seja executada
t1.join()
t2.join()

print("Execução finalizada!")
