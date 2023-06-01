import grafo
import dijstra
import time

def opcoes():
    while True:
        print("-"*50)
        print("Menu de opções:")
        print("1-Verificar distância entre os pontos com o mesmo grafo gerado:")
        print("2- Verificar distância entre pontos com outro grafo:")
        print("3-Sair")
        print("-"*50)
        try:
            opcao = int(input("Digite a opção desejada\n"))
            return opcao
        except ValueError:
            print("Por favor, digite um valor entre 1 e 3")



if __name__ == "__main__":
    opcao = 2
    while True:
        if opcao == 2:
            print("\nCriando novo grafo")
            print("-"*50)
            graph = grafo.criar_grafo()
        grafo.apresentar_grafo(graph)

        ponto_origem = input("Digite o ponto de origem: ")
        ponto_destino = input("Digite o ponto de destino: ")

        if grafo.verificar_pontos_validos(graph, ponto_origem, ponto_destino):
            print("Os pontos informados são válidos.")
            distances = dijstra.dijkstra(graph, ponto_origem)
            shortest_distance = distances[ponto_destino]
            print(f"Calculando a rota entre os pontos {ponto_origem} e {ponto_destino}")
            time.sleep(3)
            print(f"A rota mais curta de {ponto_origem} para {ponto_destino} é: {shortest_distance}\n")
        else:
            print(f"Um ou ambos os pontos informados não estão presentes no grafo.\n")
        
        opcao = opcoes()
        if opcao == 3 :
            print("Encerrando o uso do sistema para verificação de rotas") 
            break