nota1 = float(input("Digite a primeira nota :"))
nota2 = float(input("Digite a segunda nota :"))
media = (nota1 + nota2) / 2
print("Você atingiu a média de {} pontos!".format(media))
if media >= 7:
    print("Parabéns você foi aprovado!")
elif media <= 6.9 and media >= 5.0:
    print("Você está de recuperação!")
else:
    print("Você foi reprovado!")
