import pytest
import random as rnd
import src.task_4 as task_4



@pytest.mark.task_4
def test_capitalize():
    text = 'текст теКст тЕкст\nтекст теКст тЕкст. текст теКст тЕкст'
    for i in range(10):
        text = ''.join(rnd.sample(text, len(text)))
        res = task_4.capitalize(text)
        assert res == text.capitalize()


@pytest.mark.task_4
def test_process_text():
    text = 'текст текст текст текст текст текст. текст текст текст  '
    delim = [
        ' ',
        'a',
        'те',
        " е",
        "к "
    ]
    for i in range(5):
        text = ''.join(rnd.sample(text, len(text)))
        text = '      asd' + text + '   qwe   '
        res = task_4.process_text(text, delim[i])
        assert res == text.strip().split(delim[i])