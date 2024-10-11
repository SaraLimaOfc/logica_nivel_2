salario_atual = float(input("Digite o salário mensal atual:"))

percentual_reajuste = float(input("Digite o valor do reajuste:"))

novo_salario = salario_atual + (salario_atual * percentual_reajuste / 100)

print(f"O novo salário será: R${novo_salario:.2f}")
