import pytest
import random as rnd
import src.task_2 as task_2

TASK_WORD = '<YOUR CODE>'


@pytest.mark.task_2
def test_simple_branch():

    for i in range(100):
        first_value = rnd.randint(0, 100)
        second_value = rnd.randint(0, 100)
        res = task_2.simple_branch(first_value, second_value)
        assert res == "верно" if first_value > second_value else "неверно"


@pytest.mark.task_2
def test_middle_branch():

    for i in range(10):
        first_value = rnd.randint(0, 100)
        res = task_2.middle_branch(first_value)
        if first_value == 10:
            assert res == "равно"
        elif first_value > 10:
            assert res == "больше"
        else:
            assert res == "меньше"


@pytest.mark.task_2
def test_conditional_operation():

    first_value = rnd.randint(0, 100)
    second_value = rnd.randint(0, 100)
    res = task_2.conditional_operation(True, first_value, second_value)
    assert res == first_value + second_value

    first_value = rnd.randint(0, 100)
    second_value = rnd.randint(0, 100)
    res = task_2.conditional_operation(False, first_value, second_value)
    assert res == first_value - second_value


@pytest.mark.task_2
def test_checker():

    test_value = 1
    res = task_2.checker(test_value)
    assert res is True

    test_value = "sad"
    res = task_2.checker(test_value)
    assert res is False

@pytest.mark.task_2
def test_hard_condition():

    first_value = 0
    second_value = 100
    res = task_2.hard_condition(first_value, second_value)
    if (first_value >= 0 and first_value <= 10) and \
            (second_value >= -10 and second_value <= 100):
        assert res is True
    else:
        assert res is False

    for i in range(100):
        first_value = rnd.randint(0, 100)
        second_value = rnd.randint(0, 100)
        res = task_2.hard_condition(first_value, second_value)
        if (first_value >= 0 and first_value <= 10) and \
            (second_value >= -10 and second_value <= 100):
            assert res is True
        else:
            assert res is False