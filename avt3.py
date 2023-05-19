import multiprocessing
import threading
import time

def calcular_soma_parcial(inicio, fim, resultado):
    soma = 0
    for num in range(inicio, fim + 1):
        soma += num
    resultado.append(soma)

def programa_paralelo():
    resultado = multiprocessing.Manager().list()
    inicio1, fim1 = 1, 5000000
    inicio2, fim2 = 5000001, 10000000

    processo1 = multiprocessing.Process(target=calcular_soma_parcial, args=(inicio1, fim1, resultado))
    processo2 = multiprocessing.Process(target=calcular_soma_parcial, args=(inicio2, fim2, resultado))

    processo1.start()
    processo2.start()

    processo1.join()
    processo2.join()

    soma_total = sum(resultado)

    return soma_total

def programa_sequencial():
    soma_total = 0
    inicio, fim = 1, 10000000

    for num in range(inicio, fim + 1):
        soma_total += num

    return soma_total


start_time = time.time()
soma_paralela = programa_paralelo()
paralelo_execution_time = time.time() - start_time

start_time = time.time()
soma_sequencial = programa_sequencial()
sequencial_execution_time = time.time() - start_time

print("Soma paralela:", soma_paralela)
print("Tempo de execução paralela:", paralelo_execution_time)
print("Soma sequencial:", soma_sequencial)
print("Tempo de execução sequencial:", sequencial_execution_time)
