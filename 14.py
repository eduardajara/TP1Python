def votar(opcao, votos):
    if opcao == 1:
        votos['Lana'] += 1
    elif opcao == 2:
        votos['Billie'] += 1
    elif opcao == 3:
        votos['Lady Gaga'] += 1
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

votos = {'Lana': 0, 'Billie': 0, 'Lady Gaga': 0}

print("Vote em uma das opções abaixo:")
print("1 - Lana")
print("2 - Billie")
print("3 - Lady Gaga")
print("Digite 0 para encerrar a votação.\n")

while True:
    try:
        opcao = int(input("Digite o número da sua opção: "))
        if opcao == 0:
            break
        votar(opcao, votos)
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

print("\nResultados da votação:")
for opcao, quantidade in votos.items():
    print(f"{opcao}: {quantidade} votos")