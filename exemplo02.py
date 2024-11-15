from operator import truediv

from TipoVariavel import salario


codigo = int(input("Digite o código do funcionário:"))
nome = input("Digite o nome do funcionário:")
salario = float (input("Informe o slaário:"))
ativo = True #aqui você precisa se lembrar de que Python é uma linguagem tipada

print ("Código: %d" % codigo )
print ("Nome: %s " % nome)
print ("Salario: %.2f" % salario)
print ("Ativo: %r" % ativo)