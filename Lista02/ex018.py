'''Inserir salario bruto e valor da prestação, informar se emprestimo pode ser concedido ou não. A prestação não pode
ultrapassar 30% do salario bruto'''


salarioBruto = float (input ("Insira o valor do salario bruto - R$ "))
valorPrestacao = float (input ("Insira o valor da prestação - R$ "))

calculoEmprestimo = salarioBruto - (salarioBruto * 3 / 100)

if valorPrestacao > calculoEmprestimo:
   print (f'Valor da prestação acima dos 30% do salario bruto, emprestimo negado')

else:
    print(f'Emprestimo concedido')