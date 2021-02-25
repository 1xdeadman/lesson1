import pytest
import random as rnd
import src.task_3 as task_3

TASK_WORD = '<YOUR CODE>'


@pytest.mark.task_3
def test_repeat_please():

    for i in range(10):
        repeat_count = rnd.randint(0, 100)
        count = 0
        for res in task_3.repeat_please(repeat_count):
            assert res == 'TASK 3.0'
            count += 1
        assert count == repeat_count


@pytest.mark.task_3
def test_remove_by_iteration():
    for i in range(100):
        data = [x for x in range(rnd.randint(5, 100))]
        rnd.shuffle(data)
        reserved_data = data.copy()
        size = rnd.randint(1, len(data) - 3)

        print(data)
        print(size)
        print(len(reserved_data))
        task_3.remove_by_iteration(data, size)
        print(len(data))
        assert len(data) == size
        assert reserved_data[len(reserved_data) - size] == data[0]
