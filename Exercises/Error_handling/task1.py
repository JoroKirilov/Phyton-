while True:
    try:
        number = input()
        number1 = input()
        a = int(number) / int(number1)
        break
    except ValueError:
        print("Need only digits")
    except ZeroDivisionError:
        print("second digit can not be zero")
    else:
        print(a)

