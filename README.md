1 - Rodar Desafio da Mochila: basta ir no terminal e escrever: python Mochila.py

2 - Rodar Desafio de Encontrar o X: 1º Passo: Para isso você precisa instalar o módulo numpy. Vá no terminal e faça o seguinte comando: pip install numpy
                                    2º Passo: Escrever no terminal: python ValorX.py






Enunciado dos Desafios: 

O Problema da Mochila

Descrição
 ● Consiste em dado uma lista com pesos e valores, o algoritmo deve retornar 
uma lista com o a média dos pesos dos itens da lista para serem colocados 
na mochila de forma que maximize o valor, mas não ultrapassem um peso 
máximo e a lista do melhor indivíduo de cada geração. 
● Este algoritmo deve ser implementado com um algoritmo genético que 
também recebe o número de cromossomos/indivíduos e gerações que serão 
investigadas.

Exemplo de Entrada e Saída
 ● Entrada: pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], 
[12, 50], [25, 75], [50, 100], [100, 400] ]; peso_maximo = 100; 
numero_de_cromossomos = 150; geracoes = 50 
● Saída: [ [691.63, [1, 1, 1, 0, 0, 1, 0, 1, 1, 0]], [659.47, [1, 1, 1, 1, 1, 1, 1, 0, 1, 
0]], [616.23, [0, 1, 1, 0, 1, 1, 1, 0, 1, 0]], [541.4, [0, 0, 1, 0, 1, 1, 0, 1, 1, 0]], 
[468.23, [1, 1, 1, 1, 0, 1, 1, 0, 1, 0]] ]
 



 O Valor de X na Função

Descrição
 ● Desenvolva um algoritmo genético para encontrar o valor de x para o qual a função 
f(x) = x³ - 6x + 14 assuma o valor mínimo.
 ● Considerações:
 ○ Assumir que x seja um número real na seguinte faixa: [-10, +10].
 ○ Codificar x como vetor binário. 
○ Criar uma população inicial com 10 indivíduos (deixar configurável). 
○ Aplicar mutação com taxa de 1% (deixar configurável). 
○ Aplicar Crossover de 1 ou 2 pontos de corte (deixar configurável). 
○ Usar seleção por torneio ou roleta viciada. 
○ Implementar elitismo. Deixar configurável para utilizar ou não. 
○ Quando utilizado, possibilitar a configuração do percentual de indivíduos. 
○ Critério de parada: quantidade máxima de gerações (deixar configurável).