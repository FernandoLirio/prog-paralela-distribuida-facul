import threading
from time import time

def soma_range(inicio, fim):
    total = 0
    for i in range(inicio, fim + 1):
        total += i
    return total

def paralelo_soma():
    t1 = threading.Thread(target=soma_range, args=(1, 5000000))
    t2 = threading.Thread(target=soma_range, args=(5000001, 10000000))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

def sequencia_soma():
    soma_range(1, 10000000)

inicio = time()
paralelo_soma()
fim = time()
print(f"Execução paralela: {fim - inicio}")

start = time()
sequencia_soma()
end = time()
print(f"Execução sequencial: {fim - inicio}")

