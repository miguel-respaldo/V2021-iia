
def suma(numero1, numero2):
    res = numero1 + numero2
    return res


def resta(numero1, numero2):
    return numero1 - numero2


def principal():
    num1 = eval(input("Ingresa un número: "))
    num2 = eval(input("Ingresa otro número: "))
    resultado = suma(num1, num2)
    print("La suma es: ", resultado)
    print("La resta es:", resta(num1, num2))


if __name__ == "__main__":
    principal()
