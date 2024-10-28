def eh_pali(texto):
    text_limpo = texto.replace(" ", "").lower()
    return text_limpo == text_limpo[::-1]

entrada = input("Digite uma palavra ou frase: ")

if eh_pali(entrada):
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
