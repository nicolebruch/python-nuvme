#5. Tempo de jogo: (futebol)

tempo_jogo = int(input("Quantos minutos passou: "))

if (tempo_jogo <= 45):
    print("É o primeiro tempo")

elif (tempo_jogo >= 90):
    print("É o segundo tempo")

else:
    print("Acabou")
