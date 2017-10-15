# -*- coding: utf-8 -*-

'''
图的邻接表表示

@created: 2017.08.28
'''


class GraphAL(object):

    def __init__(self, maps):
        self.maps = maps
        self.node_num = len(maps)

    def __repr__(self):
        return str(self.maps)

    def __str__(self):
        return self.__repr__()

    def get_nodes(self):
        return list(range(self.node_num))

    def get_edges(self, v):
        return [e for e, w in self.maps[v]]

    def get_w_edges(self, v):
        return self.maps[v]

if __name__ == '__main__':
    maps = [[(1, 1), (2, 1)], [(0, 1), (2, 1)], [(0, 1), (1, 1)]]

    g = GraphAL(maps)
    print g
