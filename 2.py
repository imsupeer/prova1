#O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem
# do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual
#do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de
#fábrica de um carro, calcular e escrever o custo final ao consumidor.

custo_de_fabrica = float(input("Insira o valor do custo de fabricação: "))
porcetagem_distribuidor = custo_de_fabrica * 0.28
imposto= custo_de_fabrica * 0.45
carro_novo = custo_de_fabrica + porcetagem_distribuidor +imposto

print(f"O valor do carro novo é: R${carro_novo}")
