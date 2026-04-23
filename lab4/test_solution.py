import pytest
from task1_option1 import unpack_recursive
from task1_option2 import unpack_iterative
from task2_option1 import sequence_recursive
from task2_option2 import sequence_iterative

def test_unpack_recursive_basic():
    #Проверка с примером из задания для рекурсивной версии
    data = [None, [1, ({2, 3}, {'foo': 'bar'})]]
    result = unpack_recursive(data)
    assert result == [None, 1, 2, 3, 'foo', 'bar']

def test_unpack_recursive_empty():
    #Поведение на пустом списке
    assert unpack_recursive([]) == []

def test_unpack_recursive_nested():
    #Глубокая вложенность (5 уровней)
    data = [[[1, 2], [3, [4]]], 5]
    result = unpack_recursive(data)
    assert result == [1, 2, 3, 4, 5]

def test_unpack_recursive_with_dict():
    #Словарь с разными типами ключей/значений
    data = [{'a': 1, 'b': 2}, {'c': 3}]
    result = unpack_recursive(data)
    #Порядок ключей словаря не гарантирован!
    #Поэтому лучше не проверять точный порядок, а проверять множество
    assert set(result) == {'a', 'b', 'c', 1, 2, 3}

#То же самое для итеративной версии
def test_unpack_iterative_basic():
    data = [None, [1, ({2, 3}, {'foo': 'bar'})]]
    result = unpack_iterative(data)
    assert result == [None, 1, 2, 3, 'foo', 'bar']

def test_unpack_iterative_empty():
    assert unpack_iterative([]) == []


#Тесты для последовательности
def test_sequence_recursive_base1():
    #Начальное условие w_1 = 0.3
    assert sequence_recursive(1) == 0.3

def test_sequence_recursive_base2():
    #Начальное условие w_2 = -1.5
    assert sequence_recursive(2) == -1.5

def test_sequence_recursive_w3():
    #w3 = w2 * w1 * ((3-1)^2 / (3+1)^3)
    #w3 = (-1.5) * 0.3 * (4 / 64) = -0.45 * 0.0625 = -0.028125
    expected = -1.5 * 0.3 * (4 / 64)
    assert sequence_recursive(3) == pytest.approx(expected, rel=1e-9)

def test_sequence_recursive_w4():
    #w4 = w3 * w2 * ((4-1)^2 / (4+1)^3)
    w3 = -1.5 * 0.3 * (4 / 64)  # -0.028125
    expected = w3 * (-1.5) * (9 / 125)
    assert sequence_recursive(4) == pytest.approx(expected, rel=1e-9)

#Итеративная версия должна давать те же результаты
def test_sequence_iterative_w3():
    # Вычисление w_3 через итеративную версию
    expected = -1.5 * 0.3 * (4 / 64)
    assert sequence_iterative(3) == pytest.approx(expected, rel=1e-9)

def test_sequence_iterative_consistency():
    #Рекурсивная и итеративная версии должны совпадать для первых 10 членов
    for i in range(1, 11):
        assert sequence_recursive(i) == pytest.approx(sequence_iterative(i), rel=1e-9)
