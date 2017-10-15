# -*- coding: utf-8 -*-

'''
最小生成树

# 参考

# 变形

# 应用
'''

from Queue import PriorityQueue as PrioQueue

from graph import get_graph, get_al_graph


def kruskal(graph):
    '''
    将各边按权值大小从小到大排列，接着从权值最低的边
    开始建立最小生成树，如果加入的边会造成回路则舍弃
    不用，直到加入了n-1个边为止

    怎么判断回路
    '''
    if graph.node_num == 0:
        return

    node_num = graph.node_num

    # 根据权值整理所有边
    edge_list = []
    for v in range(node_num):
        for e, w in graph.get_w_edges(v):
            edge_list.append((w, v, e))
    edge_list.sort()

    # 初始化各顶点的代表元
    # 用于判断两个端点是否在不同连通分量
    # 两端点间没有路径，即为两个不同的连通分量
    rep_list = [i for i in range(node_num)]

    # 循环取边，构造最小生成树
    mst = []
    for w, vi, vj in edge_list:
        # 判断是否构成回路
        # 判断两端点是否属于不同连通分量
        if rep_list[vi] != rep_list[vj]:
            mst.append(((vi, vj), w))
            if len(mst) == node_num - 1:
                break

            # 更新代表元
            # 两端点间没有路径，即为两个不同的连通分量
            rep, orep = rep_list[vi], rep_list[vj]
            for i in range(node_num):
                if rep_list[i] == orep:
                    rep_list[i] = rep

    return mst


def prim(graph):
    '''
    从一个顶点出发，逐步扩充包含该顶点的部分生成树
    '''
    if graph.node_num == 0:
        return

    node_num = graph.node_num

    mst = [None] * node_num
    edge_list = PrioQueue()  # 候选边优先队列，从小到大排序
    edge_list.put((0, 0, 0))  # 起始顶点
    count = 0
    while count < node_num and not edge_list.empty():
        w, vi, vj = edge_list.get()

        # 判断两端点是否属于不同连通分量
        if mst[vj]:
            continue

        mst[vj] = (vi, vj), w
        count += 1
        # 添加新端点连接的边为候选边
        for e, w in graph.get_w_edges(vj):
            if not mst[e]:
                edge_list.put((w, vj, e))
    return mst

if __name__ == '__main__':
    graph = get_graph()
    graph_al = get_al_graph()

    print kruskal(graph)
    print kruskal(graph_al)

    print prim(graph)
    print prim(graph_al)
