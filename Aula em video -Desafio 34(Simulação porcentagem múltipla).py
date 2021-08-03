salario = float(input("Qual é o sálario?"))
if salario >= 1250.00:
    novo = salario + (salario/100*10)
else:
    novo = salario + (salario/100*15)
print("O novo sálario será de {:.2f}!".format(novo))