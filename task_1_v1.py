# хотел попробовать реализовать через классы, но так не получилось


class Numbers:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __neg__(self):
        return - self.value


if __name__ == '__main__':
    a = Numbers(3)
    b = Numbers(0)


def error_checker():
    try:
        operation_1 = a + b
        operation_2 = a - b
        operation_3 = a * b
        print(operation_1)
        print(operation_2)
        print(operation_3)
    except TypeError:
        print("Value is not a number!")
    try:
        operation_4 = a / b
        print(operation_4)
    except ZeroDivisionError:
        print("Division by zero!")
    except TypeError:
        pass


error_checker()
