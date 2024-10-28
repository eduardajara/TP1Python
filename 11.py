import random

def jogar_dados(quant):
    resultados = []
    for _ in range(quant):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    return resultados

try:
    quant = int(input("Você quer jogar quantos dados? "))
    
    if quant > 0:
        resultados = jogar_dados(quant)
        print("\nResultados:")
        for i, resultado in enumerate(resultados, 1):
            print(f"Dado {i}: {resultado}")
    else:
        print("Erro: Insira um número positivo")

except ValueError:
    print("Erro: Insira um número inteiro")
