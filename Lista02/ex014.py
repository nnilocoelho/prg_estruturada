'''Calcular a média do aluno com 3 notas inseridas e a média de aproveitamento com a formula abaixo
MA := (nota1 + nota2 ∗ 2 + nota3 ∗ 3 + ME)/7'''

n1 = float(input("Insira a NOTA 1: "))
n2 = float(input("Insira a NOTA 2: "))
n3 = float(input("Insira a NOTA 3: "))

media = (n1+n2+n3)/3
mediaAproveitamento = (n1+n2+n3 * 3 +media)/7

print(f"Media {media:.2f}")
print(f"Media de Aproveitamento {mediaAproveitamento:.2f}")

