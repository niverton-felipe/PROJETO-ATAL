import random

def criar_grafo():
    graph = {}

    # Definir os pontos do grafo
    pontos = ['A', 'B', 'C', 'D', 'E', 'F']

    # Criar as conexões com distâncias aleatórias
    for i in range(len(pontos)):
        for j in range(i + 1, len(pontos)):
            ponto_origem = pontos[i]
            ponto_destino = pontos[j]
            distancia = random.randint(1, 20)  # Definir uma distância aleatória entre 1 e 20
            if ponto_origem not in graph:
                graph[ponto_origem] = {}
            if ponto_destino not in graph:
                graph[ponto_destino] = {}
            graph[ponto_origem][ponto_destino] = distancia
            graph[ponto_destino][ponto_origem] = distancia

    return graph

def apresentar_grafo(graph):
    print("Grafo:")
    for ponto_origem, conexoes in graph.items():
        print(f"{ponto_origem}:")
        for ponto_destino, distancia in conexoes.items():
            print(f"  -> {ponto_destino} (Distância: {distancia})")

def verificar_pontos_validos(graph, ponto_origem, ponto_destino):
    if ponto_origem not in graph or ponto_destino not in graph:
        return False
    return True

# Exemplo de uso
#graph = criar_grafo()
#apresentar_grafo(graph)

