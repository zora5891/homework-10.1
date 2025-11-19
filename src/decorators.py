import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования начала и конца выполнения функции."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                # Логируем успешное выполнение
                log_message = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")

                return result

            except Exception as e:
                # Формируем строку с входными параметрами
                args_str = ", ".join(repr(arg) for arg in args)
                kwargs_str = ", ".join(f"{key}={repr(value)}" for key, value in kwargs.items())
                inputs_str = f"({args_str}), {{{kwargs_str}}}"
                # Логируем ошибку
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {inputs_str}\n"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message)
                else:
                    print(error_message, end="")
                raise

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


print("1. Успешное выполнение (mylog.txt):")
result1 = my_function(1, 2)
print(f"   Результат: {result1}")


@log()
def console_log_function(a, b):
    return a * b


print("\n2. Успешное выполнение (консоль):")
result2 = console_log_function(3, 4)
print(f"   Результат: {result2}")


@log(filename="error_example.txt")
def error_function(x, y):
    """Функция, которая может вызвать ошибку"""
    return x / y


print("\n3. Ошибка выполнения (файл error_example.txt):")
try:
    error_function(10, 0)
except ZeroDivisionError:
    print("   Ошибка перехвачена: ZeroDivisionError")
