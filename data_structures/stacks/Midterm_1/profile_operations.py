import sys
import os
from memory_profiler import profile

sys.path.append(os.path.abspath("Estructura-datos-2025/data_structures/stacks"))

from stack_module import Stack

N = 1500000

sizes = [N, 2*N, 3*N, 4*N, 5*N]
results = {}

@profile
def run_operations(stack_size):
    s = Stack(stack_size)
    for i in range(stack_size):
        s.push(str(i))

    search_time = s.search("not_found")

    delete_time = s.pop()

    return search_time, delete_time

for size in sizes:
    results[size] = run_operations(size)

print("Perfilamiento completado.")

profile_data = [(size, res[0], res[1]) for size, res in results.items()]
print(profile_data)
