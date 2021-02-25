import pytest
import src.task_0_0 as task_0_0


@pytest.mark.task_1_1
def test_text():
    assert type(task_0_0.text) == str
    assert task_0_0.text == "Это моя переменная. Таких переменных много, но эта - моя"


@pytest.mark.task_1_1
def test_symbol_count():
    assert type(task_0_0.symbol_count) == int
    assert task_0_0.symbol_count == 56

