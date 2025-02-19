import time
import sys
import os

sys.path.append(os.path.abspath("Estructura-datos-2025/data_structures/stacks"))

from stack_module import Stack

def find_n():
    n = 10000
    while True:
        s = Stack(n)  
        start_time = time.time()

        for i in range(n):
            s.push(str(i))

        elapsed_time = time.time() - start_time
        print(f"N={n} | Tiempo: {elapsed_time:.4f} segundos")

        if elapsed_time >= 5:
            break
        n += 1000000 

    return n

n = find_n()
print(f"Valor de N encontrado: {n}")
