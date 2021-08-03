distancia = float(input("Qual é a distância da viajem?"))
if distancia < 200:
    print("O valor da sua viagem é {:.2f} R$, visto que serão cobrados 0,50 R$ por KM!".format((distancia*0.5)))
else:
    print("Ovalor da sua viajem é {:.2f} R$, visto que serão cobrados 0,45 R$ por KM!".format((distancia*0.45)))