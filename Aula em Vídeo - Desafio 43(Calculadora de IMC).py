peso = float(input("Qual é o seu peso?  :"))
altura = float(input("Qual é a sua altura?"))
imc = peso / (altura*altura)
if imc < 18.5 :
    print("Seu imc é {:.2f} , e você está abaixo do peso!".format(imc))
elif imc >= 18.5 and imc < 25:
    print("Seu imc é {:.2f}, parabéns você está no peso ideal!".format(imc))
elif imc >= 25 and imc < 30:
    print("Seu imc é {:.2f}, tome cuidado você está acima do peso!".format(imc))
elif imc >= 30 and imc < 40:
    print("Seu imc é {:.2f},procure uma dieta, você está obeso!".format(imc))
else:
    print("Seu imc é {:.2f},faça uma dieta urgente, você está com obesidade mórbida!".format(imc))