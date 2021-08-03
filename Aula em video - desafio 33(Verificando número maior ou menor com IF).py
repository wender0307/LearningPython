a = int(input("Número 1 :"))
b = int(input("Número 2 :"))
c = int(input("Número 3 :"))
#Verificando qual o número menor...
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print("O número menor é {}.".format(menor))
#Verificando qual o número maior...
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print("O número maior é {}.".format(maior))