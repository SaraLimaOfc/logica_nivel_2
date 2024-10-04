nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))

media = (nota1 + nota2) / 2

if media >=6:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

print(f"O aluno foi {resultado} com a media de {media}")
