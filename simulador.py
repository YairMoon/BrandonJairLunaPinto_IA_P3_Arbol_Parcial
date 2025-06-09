import heapq
import matplotlib.pyplot as plt
import networkx as nx

def prim_mst(grafo, inicio):
    visitado = set()
    mst = []
    total = 0
    heap = [(0, inicio, None)]  # (costo, nodo_actual, nodo_origen)

    print("Paso a paso del algoritmo de Prim:")
    while heap:
        costo, actual, origen = heapq.heappop(heap)
        if actual in visitado:
            continue
        visitado.add(actual)
        if origen is not None:
            mst.append((origen, actual, costo))
            total += costo
            print(f"Seleccionado: {origen} --({costo})--> {actual}")

        for vecino, peso in grafo[actual].items():
            if vecino not in visitado:
                heapq.heappush(heap, (peso, vecino, actual))
    print(f"\nCosto total del árbol de expansión mínima: {total}")
    return mst

# Grafo de ejemplo (adyacencia con pesos)
grafo = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 15, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 15, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}

# Ejecutar el algoritmo desde el nodo A
mst = prim_mst(grafo, 'A')

# --- Visualización gráfica ---
def dibujar_mst(grafo, mst):
    G = nx.Graph()
    for nodo, vecinos in grafo.items():
        for vecino, peso in vecinos.items():
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)
    pesos = nx.get_edge_attributes(G, 'weight')
    mst_edges = [(u, v) for u, v, _ in mst]

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=800, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos)
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color='r', width=2)

    plt.title("Árbol de Expansión Mínima - Algoritmo de Prim")
    plt.show()

dibujar_mst(grafo, mst)
