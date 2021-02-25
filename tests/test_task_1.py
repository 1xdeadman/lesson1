import pytest
import subprocess
import src.task_1 as task_1
import random as rnd


@pytest.mark.task_1
def test_shadow_sum():
    try:
        assert 'shadow_sum' in dir(task_1)
    except Exception as ex:
        raise Exception("Модуль не содержит атрибут shadow_sum")
    for i in range(10):
        first_value = rnd.randint(0, 100)
        second_value = rnd.randint(0, 100)
        result = task_1.shadow_sum(first_value, second_value)
        assert result == 100 + first_value + second_value


@pytest.mark.task_1
def test_condition():
    try:
        assert 'condition' in dir(task_1)
    except Exception as ex:
        raise Exception("Модуль не содержит атрибут shadow_sum")
    for i in range(10):
        first_value = rnd.randint(0, 100)
        second_value = rnd.randint(0, 100)
        result = task_1.condition(first_value, second_value)
        assert result == (first_value > second_value)


@pytest.mark.task_1
def test_power():
    try:
        assert 'condition' in dir(task_1)
    except Exception as ex:
        raise Exception("Модуль не содержит атрибут shadow_sum")
    for i in range(10):
        first_value = rnd.randint(0, 100)
        second_value = rnd.randint(0, 100)
        result = task_1.power(first_value, second_value)
        assert result == first_value ** second_value
