import heapq
import grafo

def dijkstra(graph, start):
    # Inicialização
    distances = {node: float('inf') for node in graph}  # Distâncias iniciais como infinito
    distances[start] = 0  # Distância para o nó inicial como 0
    queue = [(0, start)]  # Fila de prioridade para explorar os nós
    visited = set()  # Conjunto de nós visitados

    while queue:
        # Extrai o nó com a menor distância da fila
        current_distance, current_node = heapq.heappop(queue)

        # Verifica se o nó já foi visitado
        if current_node in visited:
            continue

        # Marca o nó como visitado
        visited.add(current_node)

        # Explora os vizinhos do nó atual
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Atualiza a distância se for menor que a distância atualmente conhecida
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Adiciona o vizinho à fila com a nova distância
                heapq.heappush(queue, (distance, neighbor))

    return distances