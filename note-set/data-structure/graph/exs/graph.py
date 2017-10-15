# -*- coding: utf-8 -*-

'''
图的邻接矩阵表示

1. 初始化
2. 创建图

@created: 2017.08.26
'''

INF = 99999


class Graph(object):

    def __init__(self, node_num=0, edge_list=None):
        if node_num == 0:
            # 空图，没什么意义
            raise ValueError('The node nums of graph do not none')
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
        return [index for index, e in enumerate(self.maps[v]) if e]

    def get_w_edges(self, v):
        return [(index, e) for index, e in enumerate(self.maps[v]) if e]

if __name__ == '__main__':
    node_num = 3
    edge_list = [(1, 2, 1), (1, 3, 1), (2, 1, 1), (2, 3, 1), (3, 1, 1), (3, 2, 1)]

    g = Graph(node_num, edge_list)
    print g
