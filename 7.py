def calc_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def obter_fb(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Normal."
    elif 25 <= imc < 29.9:
        return "Sobrepeso."
    else:
        return "Obesidade."
    
peso = float(input("Digite o seu pelo em Kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = calc_imc(peso,altura)

feedback = obter_fb(imc)

print(f"Seu IMC é {imc:.2f}. {feedback}")
