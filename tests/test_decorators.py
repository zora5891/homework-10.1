import pytest

from src.decorators import log


def test_log_success_to_console_exact_format(capsys):
    """Успешная запись в консоль"""

    @log()
    def test_function(a, b):
        return a + b

    result = test_function(1, 2)
    assert result == 3

    captured = capsys.readouterr()
    assert captured.out == "test_function ok\n"


def test_log_error_to_console_exact_format(capsys):
    """Формат ошибки в консоль"""

    @log()
    def error_function(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        error_function(10, 0)

    captured = capsys.readouterr()
    expected_output = "error_function error: ZeroDivisionError. Inputs: (10, 0), {}\n"
    assert captured.out == expected_output


def test_log_preserves_function_behavior():
    """Поведение функции"""

    @log()
    def original_function(a, b):
        return a**b

    assert original_function(2, 3) == 8
    assert original_function(5, 2) == 25

    assert original_function.__name__ == "original_function"


@pytest.mark.parametrize(
    "input_args,expected_result",
    [
        ((1, 1), 2),
        ((0, 5), 5),
        ((-1, 1), 0),
        ((100, 200), 300),
    ],
)
def test_log_with_various_inputs(capsys, input_args, expected_result):
    """Параметризация с различными входными данными"""

    @log()
    def parametrized_add(x, y):
        return x + y

    result = parametrized_add(*input_args)

    assert result == expected_result

    captured = capsys.readouterr()
    assert captured.out == "parametrized_add ok\n"


def test_log_empty_arguments_success(capsys):
    """Функция без аргументов"""

    @log()
    def no_args_function():
        return "success"

    result = no_args_function()

    assert result == "success"
    captured = capsys.readouterr()
    assert captured.out == "no_args_function ok\n"
