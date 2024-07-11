import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._grafo=nx.Graph()
        self._idMap={}
        for country in DAO.getCountries():
            self._idMap[country.CCode]=country

    def get_countries(self):
        return self._grafo.nodes()
    def get_grafo(self):
        return self._grafo

    def crea_grafo(self,year):
        self._grafo.clear()
        borders=DAO.getBorders(year)
        for country in borders:
            self._grafo.add_node(self._idMap[country])
            for border in borders[country]:
                if border.conttype==1:
                    if self._idMap[border.state1no] in self._grafo.nodes and self._idMap[border.state2no] in self._grafo.nodes:
                        self._grafo.add_edge(self._idMap[border.state1no],self._idMap[border.state2no])
        return self._grafo

    def getComponentiConnesse(self):
        checked=[]
        count=0
        for node in self._grafo.nodes():
            if node not in checked:
                tree=nx.dfs_tree(self._grafo,node)
                count+=1
                checked.extend(tree.nodes())
        return count




    def numNodes(self):
        return self._grafo.number_of_nodes()

