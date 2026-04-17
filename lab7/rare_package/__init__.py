"Пакет с лабораторными работами №4-6"

# Импорты из lab4
from .lab4.task1_option1 import unpack_recursive
from .lab4.task1_option2 import unpuck_interative as unpack_iterative
from .lab4.task2_option1 import sequence_recursive
from .lab4.task2_option2 import sequence_iterative

# Импорты из lab5
from .lab5.task1 import get_file_reader
from .lab5.task2 import log_c

# Импорты из lab6
from .lab6.prime_num import generate_primes

# Список того, что будет доступно
__all__ = [
    'unpack_recursive',
    'unpack_iterative',
    'sequence_recursive',
    'sequence_iterative',
    'get_file_reader',
    'log_c',
    'generate_primes'
]
