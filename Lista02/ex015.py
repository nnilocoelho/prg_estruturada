'''Calculo de média , media de aproveitamento e conceito
APROVADO = A, B, C
REPROVADO = D e E
>= 90 A
>= 75 e < 90 B
>= 60 e < 75 C
>= 40 e < 60 D
< 40 E
'''

id = input("Insira a ID do Aluno: ")
n1 = float(input("Insira a NOTA 1: "))
n2 = float(input("Insira a NOTA 2: "))
n3 = float(input("Insira a NOTA 3: "))

media = (n1+n2+n3)/3
mediaAproveitamento = (n1+n2+n3 * 3 +media)/7

print(f"Aluno da ID: {id}")
print(f'NOTA 1: {n1}\n NOTA2: {n2}\n NOTA 3: {n3}\n')
print(f"Media dos Exercicios: {media:.2f}")

if 0 >= mediaAproveitamento < 4:
    print('Média de aproveitamento: E\nResultado: Reprovado')
elif 4 >= mediaAproveitamento < 6:
    print('Média de aproveitamento: D\nResultado: Reprovado')
elif 6 >= mediaAproveitamento < 7.5:
    print('Média de aproveitamento: C\nResultado: Aprovado')
elif 7.5 >= mediaAproveitamento < 9:
    print('Média de aproveitamento: B\nResultado: Aprovado')
elif 9 >= mediaAproveitamento < 10:
    print('Média de aproveitamento: A\nResultado: Aprovado')
