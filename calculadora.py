total_leituras = 0
normal = 0
alerta = 0
critico = 0
criticos_consecutivos = 0

while True:
    bpm = int(input("Digite a frequência cardíaca (bpm): "))

    total_leituras += 1

    if 60 <= bpm <= 100:
        print("Classificação: Normal")
        normal += 1
        criticos_consecutivos = 0  # zera sequência

    elif 101 <= bpm <= 120:
        print("Classificação: Alerta")
        alerta += 1
        criticos_consecutivos = 0  # zera sequência

    elif bpm > 120:
        print("Classificação: Crítico")
        critico += 1
        criticos_consecutivos += 1  # soma na sequência

    else:
        print("Valor fora do padrão")
        criticos_consecutivos = 0

    # condição de parada
    if criticos_consecutivos == 3:
        print("\n Três estados críticos consecutivos detectados!")
        break

     # relatório final
    print("\n===== RELATÓRIO =====")
    print("Total de leituras:", total_leituras)
    print("Normal:", normal)
    print("Alerta:", alerta)
    print("Crítico:", critico)
