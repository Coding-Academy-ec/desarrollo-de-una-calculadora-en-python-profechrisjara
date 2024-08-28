def sumar(a, b):
    # aqui se realiza la suma de dos numeros
    return a + b
a = 5
b = 3

resultado = sumar(a, b)
print("El resultado de la suma de", a, "y", b, "es:", resultado)

def restar(a, b):
        # aqui se realiza la resta de dos numeros
    return a - b
a = 5
b = 3

resultado = restar(a, b)
print("El resultado de la resta de", a, "y", b, "es:", resultado)


def multiplicar(a, b):

    # aqui se realiza la multiplicacion de dos numeros
    return a * b
a = 5
b = 3

resultado = multiplicar(a, b)
print("El resultado de la multiplicación de", a, "y", b, "es:", resultado)

def dividir(a, b):
    # aqui se realiza la division de dos numeros
    return a / b
a = 10
b = 2

resultado = dividir(a, b)
print("El resultado de la dicivión de", a, "entre", b, "es:", resultado)

def main():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    print("Suma:", sumar(num1, num2))
    print("Resta:", restar(num1, num2))
    print("Multiplicación:", multiplicar(num1, num2))
    print("División:", dividir(num1, num2))

if __name__ == "__main__":
    main()
