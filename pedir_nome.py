def calcular_tempo_viagem(distancia, velocidade):
    tempo = distancia / velocidade
    return tempo

# Solicitando o nome do motorista
nome_motorista = input("Digite o nome do motorista: ")

# Recebendo entrada do usuário
distancia = float(input("Digite a distância da viagem em quilômetros: "))
velocidade = float(input("Digite a velocidade de viagem em quilômetros por hora: "))

# Calculando o tempo de viagem
tempo_viagem = calcular_tempo_viagem(distancia, velocidade)

print("O motorista", nome_motorista, "levará aproximadamente", tempo_viagem, "horas para fazer a viagem.")