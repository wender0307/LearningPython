vcarro = float(input("você passou no radar a quantos kms?"))
if vcarro >= 80:
    print("Você foi multado em {:.2f} R$!".format((vcarro-80)*7))
else:
    print("Você não foi multado!")