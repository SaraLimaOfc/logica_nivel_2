salario_fixo = float(input("Digite o salário fixo do vendedor: R$ "))
carros_vendidos = int(input("Digite o número de carros vendidos: "))
total_vendas = float(input("Digite o valor total das vendas: R$ "))

comissao = 700 * carros_vendidos
bonus = total_vendas * 0.05
salario_final = salario_fixo + comissao + bonus

print(f"Salário final: R$ {salario_final:.2f}")
