# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc  # Certifique-se de retornar 'imc', não 'im'

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "peso adequado"
    elif 25 <= imc <= 29.9:
        return "sobrepeso"
    elif 30 <= imc <= 34.9:
        return "obesidade grau I"
    elif 35 <= imc <= 39.9:
        return "obesidade grau II"
    else:
        return "obesidade grau III"

# Solicitar entrada do usuário
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros (use ponto como separador decimal): "))

# Calcular o IMC
imc = calcular_imc(peso, altura)

# Classificar o IMC
classificacao = classificar_imc(imc)

# Exibir o resultado
print(f"Seu IMC é {imc:.2f}, e sua classificação é: {classificacao}.")