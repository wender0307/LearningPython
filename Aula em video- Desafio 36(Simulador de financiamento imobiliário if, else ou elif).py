nome = str(input("Olá qual é o seu nome?")).upper()
print("{} muito prazer em conhece-lo, sou o consultor do banco,\ne vou fazer a analise do seu finaciamento imobiliário ok?".format(nome))
imovel = float(input("{} primeiro precisamos saber qual é o valor do ímovel que você deseja? : ".format(nome)))
tempo = float(input("{} você quer pagar o seu ímovel em quantos anos? :".format(nome)))
salario = int(input("Qual é a sua renda mensal? :"))
parcelas = imovel / (tempo*12)
print("O valor da parcela mensal do ficanciamento vai ficar em R${:.2f}!".format(parcelas))
if parcelas <= (salario/100)*30:
    print("Parabens seu ficanciamento foi aprovado!")
#Com a condição elif também dedu certo!
else:
    print("Sinto muito mais precisamos de uma parcela mensal de até 30% da sua renda mensal!")