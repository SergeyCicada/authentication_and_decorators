"""Декоратор - это функция, которая позволяет обернуть другую функцию для расширения её функциональности
без непосредственного изменения её кода
Код декоратора:"""

"""Простой декоратор"""
#
#
# def decorator_name(func):
#     def wrapper():
#         print('До выполнения функции')
#         func()
#         print('После выполнения функции')
#
#     return wrapper
#
#
# @decorator_name
# def my_func():  # по факту мы заменяем функцию my_func() на decorator_name(func) с помощью @decorator_name
#     print('Ok')
#
#
# my_func()

"""Декоратор для работы с результатом"""


# def decorator_name(func):
#     def wrapper():
#         result = func()
#         print(f"Результат - {result}")
#
#         return result
#
#     return wrapper
#
#
# @decorator_name
# def my_func():  # по факту мы заменяем функцию my_func() на decorator_name(func) с помощью @decorator_name
#     return 'Ok'
#
#
# print(my_func())

"""Декоратор для работы с пользователем"""


def decorator_name(func):
    def wrapper(*args, **kwargs):
        print(f"До выполнения функции")
        result = func(*args, **kwargs)
        print("После выполнения функции")

        return f"Decorator - {result}"

    return wrapper

@decorator_name
def my_func(user_name, year):
    return [user_name, year]


print(my_func("Joan", 21))
