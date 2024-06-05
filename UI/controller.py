import warnings

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.chosen_album = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_crea_grafo(self, e):
        try:
            tot_d_int = int(self._view.txt_in_durata.value)
        except ValueError:
            self._view.create_alert("Inserire un numero intero")
            '''warnings.warn_explicit(message="Inserire un intero",
                                   category=TypeError,
                                   filename="controller.py",
                                   lineno=15)'''
            return
        self._model.build_graph(tot_d_int)
        nodes = self._model.get_nodes()
        self._view.dd_album.options.clear()
        for n in nodes:
            try:
                self._view.dd_album.options.append(ft.dropdown.Option(data=n,
                                                                      text=n.Title))
            except AttributeError:
                print("******")
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        n_nodi, n_archi = self._model.get_graph_details()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {n_nodi} e {n_archi} archi."))
        self._view.update_page()

    def get_selected_album(self, e):
        if e.control.data is None:
            self.chosen_album = None
        else:
            self.chosen_album = e.control.data

    def handle_analisi_componente(self):
        if self.chosen_album is None:
            self._view.create_alert("Selezionare un album")
            return
        size_c, tot_d = self._model.get_connessa_details(self.chosen_album)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"La componente connessa che contiene {self.chosen_album} "
                                                      f"contiene {size_c} album e ha una durata di {tot_d} minuti."))


    def handle_set_album(self):
        pass
