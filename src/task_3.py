"""
Внимательно прочитайте код в этом файле и добавьте свой код везде, где встречается <YOUR CODE>.
Перед каждым <YOUR CODE> вы можете прочитать описание задания, помеченный фразой <TODO>.
для проверки запустите pytest tests/test_task_3.py
"""


def repeat_please(count: int):
    # TODO: добавьте условие итерации для цикла так, чтобы цикл отрабатывал count итераций
    for i in range("<YOUR CODE>"):
        yield "TASK 3.0"


def remove_by_iteration(data: list, size: int):
    current_size = len(data)
    # TODO: добавьте условие итерации для цикла так, чтобы цикл работал до тех пор, пока current_size больше size
    while "<YOUR CODE>":
        data.pop(0)
        current_size = len(data)
