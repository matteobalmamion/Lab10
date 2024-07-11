import datetime

import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._country=None

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        try:
            year=int(self._view._txtAnno.value)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Errore nel formato del testo inserito"))
            self._view.update_page()
            return
        if year<1816 or year>2016:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append("Anno inserito fuori dal range")
            self._view.update_page()
            return
        grafo=self._model.crea_grafo(year)
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha  {self._model.getComponentiConnesse()} componenti connesse"))
        nodi=list(grafo.nodes)
        nodi.sort(key=lambda x: x.StateAbb)
        for country in nodi:
            self._view._txt_result.controls.append(ft.Text(f"{country} -- {grafo.degree(country)}"))
        self._view._ddStato.disabled=False
        self._view._btnStatiRaggiungibili.disabled=False
        self._fillDD()
        self._view.update_page()

    def handleStatiRaggiungibili(self,e):
        self._view._txt_result.controls.clear()
        self.tree_dfs()
        self.tree_bfs()
        self.tree_ricorsivo()
        self.tree_iterativo()

    def tree_dfs(self):
        start=datetime.datetime.now()
        self._view._txt_result.controls.append(ft.Text(f"Metodo 1: DFS"))
        grafo=self._model.get_grafo()
        start = datetime.datetime.now()
        tree=nx.dfs_tree(grafo,self._country)
        tree.remove_node(self._country)
        end = datetime.datetime.now()
        print(end-start)
        print(len(tree))
        for node in tree:
            self._view._txt_result.controls.append(ft.Text(f"{node}"))

        self._view.update_page()

    def tree_bfs(self):
        self._view._txt_result.controls.append(ft.Text(f"Metodo 2: BFS"))
        grafo=self._model.get_grafo()
        start = datetime.datetime.now()
        tree=nx.bfs_tree(grafo,self._country)
        tree.remove_node(self._country)
        end = datetime.datetime.now()
        print(end-start)
        print(len(tree))
        for node in tree:
            self._view._txt_result.controls.append(ft.Text(f"{node}"))

        self._view.update_page()

    def tree_iterativo(self):
        self._view._txt_result.controls.append(ft.Text(f"Metodo 4: Iterativo"))
        grafo=self._model.get_grafo()
        visitati=[]
        daVisitare=[self._country]
        start = datetime.datetime.now()
        while daVisitare:
            country= daVisitare.pop(0)
            visitati.append(country)
            neighbors=list(grafo.neighbors(country))
            for neighbor in neighbors:
                if neighbor not in visitati and neighbor not in daVisitare:
                    daVisitare.append(neighbor)
        visitati.remove(self._country)
        end = datetime.datetime.now()
        print(end-start)
        print(len(visitati))
        for node in visitati:
            self._view._txt_result.controls.append(ft.Text(f"{node}"))

        self._view.update_page()

    def tree_ricorsivo(self):
        self._view._txt_result.controls.append(ft.Text(f"Metodo 3: Algoritmo ricorsivo"))
        grafo=self._model.get_grafo()
        start = datetime.datetime.now()
        visited = []
        n = self._country
        self._recursive_visit(n, visited,grafo)
        visited.remove(n)
        end = datetime.datetime.now()
        print(end - start)
        print(len(visited))
        for node in visited:
            self._view._txt_result.controls.append(ft.Text(f"{node}"))
        self._view.update_page()

    def _recursive_visit(self, n, visited,grafo):
        visited.append(n)
        # Iterate through all neighbors of n
        for c in grafo.neighbors(n):
            # Filter: visit c only if it hasn't been visited yet
            if c not in visited:
                self._recursive_visit(c, visited,grafo)

    def _fillDD(self):
        countries=self._model.get_countries()
        for country in countries:
            self._view._ddStato.options.append(ft.dropdown.Option(data=country,text=country.StateNme,on_click=self.readCountry))

    def readCountry(self,e):
        if e.control.data is None:
            self._country=None
        else:
            self._country=e.control.data
