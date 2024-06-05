import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self.albums_map = {}
        self.best_set = None
        self.best_score = None

    def build_graph(self, d):
        self.graph.clear()
        self.graph.add_nodes_from(DAO.get_albums(to_milliseconds(d)))
        self.albums_map = {a.AlbumId: a for a in list(self.graph.nodes)}
        self.graph.add_edges_from(DAO.get_edges(self.albums_map))

    def get_graph_details(self):
        return len(self.graph.nodes), len(self.graph.edges)

    def get_nodes(self):
        return self.graph.nodes

    def get_connessa_details(self, source):
        conn = nx.node_connected_component(self.graph, source)
        durata_tot = 0
        for album in conn:
            durata_tot += to_minutes(album.tot_d)
        return conn, durata_tot

    def get_set_album(self, a1, d_tot):
        self.best_set = None
        self.best_score = 0
        connessa = nx.node_connected_component(self.graph, a1)  #componente connessa di a1
        parziale = {a1}
        connessa.remove(connessa)
        self.ricorsione(parziale, connessa, d_tot)
        return self.best_set

    def ricorsione(self, parziale, connessa, d_tot):
        if self.get_durata_tot(parziale) > d_tot:  # verifico che parziale è ammissibile
            return
        if len(parziale) > self.best_score:  # se ho trovato una soluzione migliore di quella che ho
            self.best_set = copy.deepcopy(parziale)
            self.best_score = len(parziale)
            print(parziale)
        for c in connessa:
            if c not in parziale:
                parziale.add(c)
                self.ricorsione(parziale, connessa, d_tot)
                parziale.remove(c)

    def get_durata_tot(self, album_list):
        d = 0
        for a in album_list:
            d += a.tot_d
        return d


def to_milliseconds(d):
    return d * 1000 * 60


def to_minutes(d):
    return d / 60 / 1000
