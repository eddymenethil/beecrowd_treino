"""Leia 2 valores de ponto flutuante de dupla precisão A e B,
que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, 
sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). 
Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

Entrada
O arquivo de entrada contém 2 valores com uma casa decimal cada um.

Saída
Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, 
com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade. 
Utilize variáveis de dupla precisão (double) e como todos os problemas, 
não esqueça de imprimir o fim de linha após o resultado, caso contrário, 
você receberá "Presentation Error".
"""

#Variavel

a = float(input())
b = float(input())

#peso da notas
peso_a = 3.5
peso_b = 7.5

#Calculo da média
media = ((a * peso_a) + (b * peso_b)) / (peso_a + peso_b)

#imprimir 
print('MEDIA = {:.5f}'.format(media))