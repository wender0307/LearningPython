nome = input("Sou o vendedor da loja ! Qual é seu nome? ")
precoinicial = float(input("{}, digite o valor do produto ".format(nome)))
meiopagamento = str(input("{}, qual será o meio de pagamento?".format(nome))).upper().strip()
if meiopagamento == "DINHEIRO":
    print("{}, você ganhará um desconto de 10% no pagamento em dinheiro!\nO produto sairá por R${:.2f}!".format(nome, precoinicial-(precoinicial/100*10)))
elif meiopagamento == "cartão" or "cartao":
    vezes = int(input("Em quantas vezes? "))
    if vezes == 1:
        print("{}, você ganhará 5% de desconto pagando a vista no cartão!\nO preço do produto cairá para R${:.2f}!".format(nome, precoinicial-(precoinicial/100*5)))
    elif vezes == 2:
        print("Ok {}! Não iremos cobrar juros, seu produto sairá por : R${:.2f}!".format(nome, precoinicial))
    elif vezes >= 3:
        print("Ok {}, devido ao número de parcelas , o produto terá um acréscimo de 20%.\nO preço final ficará em R${:.2f}!".format(nome, (precoinicial/100*20)+precoinicial))
    print("Muito Obrigado {}, e volte sempre!".format(nome))