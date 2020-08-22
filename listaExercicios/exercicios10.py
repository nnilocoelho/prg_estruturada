print("Teste de Formatação de Strings")

myInt = 12345
myFloat = 3.14159
myString = "Curso de Python"

print("Integer: ", myInt)
print("Decimal %d e um integer %d" %(myInt, myInt))
print("Integer Hexadecimal %x" %myInt)
print("Float", myFloat)
print("Default %f", myFloat)
print("Exponencial %e" %myFloat)
print("Justificar Direita (%10d)" % myFloat)
print("Justify Esquerda (%-10d)" %myFloat)
print("Forma 9 digitos %.9d" %myInt)
print("Forma 3 digitos depois do decimal %.3f" % myFloat)
print("Dez e cinco caracteres permitidos na string:")
print("(%.10s) (%.5s)" % (myString, myString))
