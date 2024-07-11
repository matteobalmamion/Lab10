from model.model import Model

model=Model()
grafo=model.crea_grafo(2000)
print(len(grafo.nodes))
print(len(grafo.edges))