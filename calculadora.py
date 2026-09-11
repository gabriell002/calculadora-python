m = float(input("Digite a média: "))
f = float(input("Digite o percentual de frequencia: "))
if f < 75:
    print(("Reprovado por falta!"))
elif m < 6:
    print("Reprovado por nota!")
else:
    print("Aprovado")
