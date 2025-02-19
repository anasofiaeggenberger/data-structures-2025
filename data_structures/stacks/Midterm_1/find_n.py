import time
import sys
import os

sys.path.append(os.path.abspath("Estructura-datos-2025/data_structures/stacks"))

from stack_module import Stack

def find_n():
    n = 100000
    while True:
        s = Stack(n)  
        start_time = time.time()

        for i in range(n):
            s.push(str(i))

        elapsed_time = time.time() - start_time
        print(f"N={n} | Tiempo: {elapsed_time:.4f} segundos")

        if elapsed_time >= 1:
            break
        n += 100000

    return n

n = find_n()
print(f"Valor de N encontrado: {n}")
