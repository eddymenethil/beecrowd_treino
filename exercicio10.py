"""Neste problema, deve-se ler o código de uma peça 1, 
o número de peças 1, o valor unitário de cada peça 1, 
o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, 
calcule e mostre o valor a ser pago.

Entrada
O arquivo de entrada contém duas linhas de dados. 
Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.

Saída
A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, 
lembrando de deixar um espaço após os dois pontos e um espaço após o "R$".
O valor deverá ser apresentado com 2 casas após o ponto."""

# Variavel 
cod_peca_1 = int(input())
numero_peca_1 = int(input())
valor_unitario_1 = float(input())

# variavel 2 
cod_peca_2 = int(input())
numero_peca_2 = int(input())
valor_unitario_2 = float(input())


# Calculo vai ser quantidade multiplicado pelo valor , depois soma os dois valores para da resultado final
total = (numero_peca_2 * valor_unitario_2) + (numero_peca_1 * valor_unitario_1 )

# imprimir resultado
print("VALOR A PAGAR: R$ {:.2f}" .format(total))