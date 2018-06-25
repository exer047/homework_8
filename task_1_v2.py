# простая и рабочая версия калькулятора через инпуты и принты

def calculate():
    while True:
        try:
            s = input("Операция (+ ,- ,* , /): ")
            x = int(input("x = "))
            y = int(input("y = "))
            if s == "+":
                result = x + y
            elif s == "-":
                result = x - y
            elif s == "*":
                result = x * y
            elif s == "/":
                result = x / y
            print(result)
        except ZeroDivisionError:
            print("Деление на 0 невозможно!")
        except ValueError:
            print("Введеное значение не является числом!")
        except UnboundLocalError:
            print("Вы указали несуществующую операцию")


if __name__ == '__main__':
    calculate()
