import time

start_tempo = time.time()

soma = 0
for i in range(1,1000001):
    soma += i

stop_tempo = time.time()
execution_time = stop_tempo - start_tempo

print("A soma dos números é:", soma)
print("Tempo de execução:", execution_time, "segundos")
