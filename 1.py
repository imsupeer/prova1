#A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40
#horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um
#algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total
#do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o
#mês possua 4 semanas exatas).

horas_mensais = int(input("Insira o valor de horas trabalhadas por mês: "))
salario_por_hora = float(input("Insira o valor salarial referente a hora trabalhada: "))

if horas_mensais > 40 and horas_mensais <= 160:
    salario_total = horas_mensais*(salario_por_hora*50/100)
else:
    salario_total = horas_mensais*salario_por_hora

print(f"O salário total é de: R${salario_total}")
