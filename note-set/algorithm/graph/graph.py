# -*- coding: utf-8 -*-

'''
图的两种不同表示法
'''

INF = 99999


class Graph(object):
    '''
    图的邻接矩阵表示
    '''

    def __init__(self, node_num=0, edge_list=None):
        if node_num == 0:
            raise ValueError('The node num must be not None')
        maps = []
        for x in range(node_num):
            row = []
            for y in range(node_num):
                if x == y:
                    row.append(0)
                else:
                    row.append(INF)
            maps.append(row)
        for x, y, w in edge_list:
            maps[x-1][y-1] = w
        self.maps = maps
        self.node_num = node_num

    def __repr__(self):
        return str(self.maps)

    def __str__(self):
        return self.__repr__()

    def get_nodes(self):
        return list(range(self.node_num))

    def get_edges(self, v):
        return [index for index, e in enumerate(self.maps[v]) if e and e != INF]

    def get_w_edges(self, v):
        return [(index, e) for index, e in enumerate(self.maps[v]) if e and e != INF]


class GraphAL(object):
    '''
    图的邻接表表示
    '''

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


def get_graph():
    g = Graph(7, [
        [1, 2, 3], [1, 3, 7], [2, 1, 3],
        [2, 4, 2], [2, 5, 4], [3, 1, 7],
        [3, 5, 6], [3, 6, 9], [6, 3, 9],
        [6, 7, 8], [7, 6, 8], [4, 2, 2],
        [5, 2, 4], [5, 3, 6]
    ])
    return g


def get_al_graph():
    g = GraphAL([
        [(1, 3), (2, 7)],
        [(0, 3), (3, 2), (4, 4)],
        [(0, 7), (4, 6), (5, 9)],
        [(1, 2)],
        [(1, 4), (2, 6)],
        [(2, 9), (6, 8)],
        [(5, 8)]
    ])
    return g
