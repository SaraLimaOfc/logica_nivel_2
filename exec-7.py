votos_brancos = int(input("Digite a quantidade de votos brancos:"))

votos_nulos = int(input("Digite a quantidade de votos nulos:"))

votos_validos = int(input("Digite a quantidade de votos validos:"))

total_eleitores = votos_brancos + votos_nulos + votos_validos

percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100

print(f"O total de votos válidos é: {percentual_validos:.2f}%")
print(f"O total de votos brancos é: {percentual_brancos:.2f}%")
print(f"O total de votos nulos é: {percentual_nulos:.2f}%")
