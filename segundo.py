print()
n = int(input("Quantos termos você quer mostrar?"))
numero_verificar = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

i = 0
j = 1

print("{}, {}".format(i, j), end='')

cont = 3
pertence = (numero_verificar == 0 or numero_verificar == 1)

while cont <= n:
    k = i + j
    print(", {}".format(k), end='')

    if k == numero_verificar:
        pertence = True

    i = j
    j = k
    cont += 1

if pertence:
    print(f"\n0 número {numero_verificar} pertence à sequência de Fibonacci")
else:
    print(f"\n0 número {numero_verificar} NÃO pertence à sequência de Fibonacci")

print('~' * 30)
print('Fim')
