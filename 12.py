def class_palavras(palavras):
    curtas = []
    longas = []

    for palavra in palavras:
        if len(palavra) < 5:
            curtas.append(palavra)
        else:
            longas.append(palavra)
    
    return curtas, longas

entrada = input("Digite várias palavras separadas por espaço: ")
palavras = entrada.split()

curtas, longas = class_palavras(palavras)

print("\nPalavras curtas (menos de 5 letras):")
print(", ".join(curtas) if curtas else "Nenhuma palavra curta")

print("\nPalavras longas (5 letras ou mais):")
print(", ".join(longas) if longas else "Nenhuma palavra longa")
