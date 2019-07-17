import math

# obliczamy wynik równania kwadratowego

print("ZAD. 1")


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


while True:
    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c: ")

    if not (check_int(a) and check_int(b) and check_int(c)):
        print("Wrong input. Enter decimals only")
        break
    else:
        a_int = int(a)
        b_int = int(b)
        c_int = int(c)

        if a_int == 0:
            print("It's not a squared equation because a=0. Program stopped")
            break
        else:
            delta = pow(b_int, 2) - 4*a_int*c_int

            if delta < 0:
                print("No possible solution")
                break
            elif delta == 0:
                x1 = (-b_int-math.sqrt(delta))/(2*a_int)
                print("x1 =", x1)
                break
            else:
                x1 = (-b_int - math.sqrt(delta)) / (2 * a_int)
                x2 = (-b_int + math.sqrt(delta)) / (2 * a_int)
                print("x1 =", x1, ", x2=", x2)
                break

