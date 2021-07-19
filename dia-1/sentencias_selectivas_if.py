# Salida es print()
# Entrada es input()

print("Este es una calculadora simple")
print("División")
num1 = eval(input("Escribe el primer número: "))
num2 = eval(input("Escribe el segundo numero: "))
# >  >=  <  <=  ==(igual)  !=(diferente, o no igual)  !(no)
if num2 == 0:
    print("Error: división entre cero")
else:
    resultado = num1 / num2
    print("El resultado es: ", resultado)
