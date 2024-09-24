"""Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno.
A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5.
Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 3 valores com uma casa decimal, de dupla precisão (double).

Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo,
com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade. 
Assim como todos os problemas, 
não esqueça de imprimir o fim de linha após o resultado,
caso contrário, você receberá "Presentation Error"."""

# Variavel 
a = float(input())
b = float(input())
c = float(input())

# Variavel do peso
peso_a = 2
peso_b = 3
peso_c = 5

#Caculo das notas

media = ((a * peso_a) + (b * peso_b) + (c * peso_c)) / (peso_a + peso_b + peso_c) 

#imprimir
print("MEDIA = {:.1f}".format(media))