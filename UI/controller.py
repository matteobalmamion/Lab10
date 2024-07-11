import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        grafo=self._model.crea_grafo(self._view._txtAnno.value)
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha  {self._model.getComponentiConnesse()} componenti connesse"))
        nodi=list(grafo.nodes)
        nodi.sort(key=lambda x: x.StateAbb)
        for country in nodi:
            self._view._txt_result.controls.append(ft.Text(f"{country} -- {grafo.degree(country)}"))
        self._view.update_page()

