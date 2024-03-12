import timeit
import psutil
from array import array

# Criando uma tupla de ponto flutuante
b_memory_info = psutil.virtual_memory().used
tupla_float = tuple(1.0 for _ in range(10**7))
t_memory_info = psutil.virtual_memory().used
total_tupla = t_memory_info - b_memory_info

# Criando um array de ponto flutuante
b_memory_info = psutil.virtual_memory().used
array_float = array('d', (1.0 for _ in range(10**7)))
t_memory_info = psutil.virtual_memory().used
total_array = t_memory_info - b_memory_info

tupleismoreeffitient = total_tupla - total_array

# Teste de velocidade de criação
tempo_tupla = timeit.timeit(lambda: tupla_float)
tempo_array = timeit.timeit(lambda: array_float)

tempo_tupla_acesso_1 = timeit.timeit(lambda: tupla_float[0])
tempo_array_acesso_1 = timeit.timeit(lambda: array_float[0])

tempo_tupla_acesso = timeit.timeit(lambda: tupla_float[500000])
tempo_array_acesso = timeit.timeit(lambda: array_float[500000])


pass