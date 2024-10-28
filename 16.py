def ver_par(numero):
    if numero % 2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")

try:
    numero = int(input("Digite um número: "))
    ver_par(numero)
except ValueError:
    print("Erro: Insira um número inteiro válido")
