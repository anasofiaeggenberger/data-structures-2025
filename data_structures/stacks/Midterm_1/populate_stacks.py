import sys
import os

sys.path.append(os.path.abspath("Estructura-datos-2025/data_structures/stacks"))

from stack_module import Stack

N = 13010000  

sizes = [N, 2*N, 3*N, 4*N, 5*N]
stacks = {}

for size in sizes:
    s = Stack(size)
    for i in range(size):
        s.push(str(i))
    stacks[size] = s
    print(f"Stack de tamaño {size} poblado completamente.")

print("Stacks creados y llenos.")
