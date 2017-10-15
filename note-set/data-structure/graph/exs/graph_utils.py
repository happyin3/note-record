# -*- coding: utf-8 -*-

'''
图相关算法

@created: 2017.08.29
'''

from collections import deque
from Queue import PriorityQueue as PrioQueue

INF = 99999


def dfs_re_traverse(graph):
    '''
    深度优先搜索，递归
    '''
    if graph.node_num == 0:
        return

    visited_list = [0] * graph.node_num

    def dfs(v):
        print v,
        visited_list[v] = 1
        for e in graph.get_edges(v):
            if not visited_list[e]:
                dfs(e)

    for v in graph.get_nodes():
        if not visited_list[v]:
            dfs(v)


def dfs_traverse(graph):
    '''
    深度优先搜索，非递归
    '''
    if graph.node_num == 0:
        return

    visited_list = [0] * graph.node_num

    def dfs(node_stack):
        while(len(node_stack) > 0):
            v = node_stack.pop()
            if not visited_list[v]:
                print v,
                visited_list[v] = 1
                node_stack.extend(graph.get_edges(v))

    node_stack = []
    for v in graph.get_nodes():
        if not visited_list[v]:
            node_stack.append(v)
            dfs(node_stack)


def bfs_traverse(graph):
    '''
    广度优先搜索，非递归
    '''
    if graph.node_num == 0:
        return

    visited_list = [0] * graph.node_num

    def bfs(node_queue):
        while(node_queue):
            v = node_queue.pop()
            if not visited_list[v]:
                visited_list[v] = 1
                print v,
                for e in graph.get_edges(v):
                    if not visited_list[e]:
                        node_queue.appendleft(e)

    node_queue = deque()
    for v in graph.get_nodes():
        if not visited_list[v]:
            node_queue.appendleft(v)
            bfs(node_queue)


def dfs_re_tree(graph):
    '''
    深度优先生成树，递归
    '''
    if graph.node_num == 0:
        return

    def dfs(v):
        for e in graph.get_edges(v):
            if edge_list[e] is None:
                edge_list[e] = v
                dfs(e)

    edge_list = [None] * graph.node_num
    for v in range(graph.node_num):
        if edge_list[v] is None:
            edge_list[v] = v
            dfs(v)

    print edge_list


def dfs_tree(graph):
    '''
    深度优先生成树，非递归
    '''
    if graph.node_num == 0:
        return

    def dfs(node_stack):
        while(len(node_stack) > 0):
            v, pre = node_stack.pop()
            if edge_list[v] is None:
                edge_list[v] = pre
                for e in graph.get_edges(v):
                    node_stack.append((e, v))

    edge_list = [None] * graph.node_num
    node_stack = []
    for v in range(graph.node_num):
        if edge_list[v] is None:
            node_stack.append((v, 0))
            dfs(node_stack)

    print edge_list


def bfs_tree(graph):
    '''
    宽度优先生成树，非递归
    '''
    if graph.node_num == 0:
        return

    def bfs(node_queue):
        while(len(node_queue) > 0):
            v = node_queue.pop()
            for e in graph.get_edges(v):
                if edge_list[e] is None:
                    edge_list[e] = v
                    node_queue.appendleft(e)

    edge_list = [None] * graph.node_num
    node_queue = deque()
    for v in range(graph.node_num):
        if edge_list[v] is None:
            edge_list[v] = v
            node_queue.appendleft(v)
            bfs(node_queue)

    print edge_list


def kruskal_tree(graph):
    '''
    最小生成树，Kruskal算法
    '''
    if graph.node_num == 0:
        return

    node_num = graph.node_num

    # 初始化所有点的代表元
    reps_list = [i for i in range(node_num)]

    # 根据权值整理所有边
    edge_list = []
    for v in range(node_num):
        for e, w in graph.get_w_edges(v):
            edge_list.append((w, v, e))
    # 边按权值排序
    edge_list.sort()

    # 循环取边，构造最小生成树
    mst = []
    for w, vi, vj in edge_list:
        # 判断两端点是否属于不同连通分量
        if reps_list[vi] != reps_list[vj]:
            mst.append(((vi, vj), w))
            if len(mst) == node_num - 1:
                break

            # 更新代表元
            rep, orep = reps_list[vi], reps_list[vj]
            for i in range(node_num):
                if reps_list[i] == orep:
                    reps_list[i] = rep
    return mst


def prim_tree(graph):
    '''
    最小生成树，Prim算法
    '''
    if graph.node_num == 0:
        return

    node_num = graph.node_num

    mst = [None] * node_num
    edge_list = PrioQueue()
    edge_list.put((0, 0, 0))
    count = 0
    while count < node_num and not edge_list.empty():
        w, vi, vj = edge_list.get()

        if mst[vj]:
            continue

        mst[vj] = (vi, vj), w
        count += 1
        for e, w in graph.get_w_edges(vj):
            if not mst[e]:
                edge_list.put((w, vj, e))
    return mst


def dijkstra_path(graph, v):
    '''
    最短路径，单点，Dijkstra算法
    '''
    if graph.node_num == 0:
        return

    node_num = graph.node_num

    path_list = [None] * node_num
    count = 0
    edge_list = PrioQueue()
    edge_list.put((0, v, v))
    while count < node_num and not edge_list.empty():
        plen, u, vmin = edge_list.get()

        if path_list[vmin]:
            continue

        path_list[vmin] = (u, plen)
        count += 1
        for e, w in graph.get_w_edges(vmin):
            if not path_list[e]:
                edge_list.put((plen+w, vmin, e))

    return path_list


def floyd_path(graph):
    '''
    最短路径，多源，Floyd算法

    基于图的邻接矩阵
    '''
    if graph.node_num == 0:
        return

    node_num = graph.node_num
    maps = graph.maps

    next_v = [[-1 if maps[i][j] == INF else j for j in range(node_num)] for i in range(node_num)]

    for k in range(node_num):
        for i in range(node_num):
            for j in range(node_num):
                if maps[i][j] > maps[i][k] + maps[k][j]:
                    maps[i][j] = maps[i][k] + maps[k][j]
                    next_v[i][j] = next_v[i][k]

    print maps
    print next_v


def topo_sort(graph):
    '''
    拓扑排序
    '''
    if graph.node_num == 0:
        return

    node_num = graph.node_num

    indegree, toposeq = [0]*node_num, []
    zerov = -1

    for v in range(node_num):
        for e, w in graph.get_edges(v):
            indegree[e] += 1
    for v in range(node_num):
        if indegree[v] == 0:
            indegree[v] = zerov
            zerov = v

    for n in range(node_num):
        if zerov == -1:
            return

if __name__ == '__main__':
    from al_graph import GraphAL
    g = GraphAL([
        [(1, 3), (2, 7)],
        [(0, 3), (3, 2), (4, 4)],
        [(0, 7), (4, 6), (5, 9)],
        [(1, 2)],
        [(1, 4), (2, 6)],
        [(2, 9), (6, 8)],
        [(5, 8)]
    ])

    dfs_re_traverse(g)
    print
    dfs_traverse(g)
    print
    bfs_traverse(g)

    print

    print kruskal_tree(g)
    print prim_tree(g)

    from graph import Graph
    g = Graph(7, [
        [1, 2, 3], [1, 3, 7], [2, 1, 3],
        [2, 4, 2], [2, 5, 4], [3, 1, 7],
        [3, 5, 6], [3, 6, 9], [6, 3, 9],
        [6, 7, 8], [7, 6, 8], [4, 2, 2],
        [5, 2, 4], [5, 3, 6]
    ])

    print g
    dfs_re_traverse(g)
    print
    dfs_traverse(g)
    print
    bfs_traverse(g)

    print

    dfs_re_tree(g)
    dfs_tree(g)
    bfs_tree(g)

    print kruskal_tree(g)
    print prim_tree(g)

    print dijkstra_path(g, 0)

    floyd_path(g)
