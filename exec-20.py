inicio = int(input("Qual é a hora do inicio do jogo: "))

fim = int(input("Qual é a hora do fim do jogo: "))

if fim >= inicio:
    duracao = fim - inicio
else:
    duracao = (24 - inicio) + fim

if duracao >= 24:
    print("O tempo excedeu o limite")
else:
    print(f"A duração do jogo foi de {duracao} horas")
