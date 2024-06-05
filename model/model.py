import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self.albums_map = {}

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


def to_milliseconds(d):
    return d * 1000 * 60


def to_minutes(d):
    return d / 60 / 1000
