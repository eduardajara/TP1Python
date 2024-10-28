def novo_nome(nome1, nome2):
    n1 = nome1[:len(nome1)//2]
    n2 = nome2[len(nome2)//2:]
    apelido = n1 + n2
    return apelido

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")

apelido = novo_nome(nome1, nome2)

print(f"O apelido criado é: {apelido}")
