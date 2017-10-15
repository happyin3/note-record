# -*- coding: utf-8 -*-

'''
二叉树
'''


class Node(object):
    '''
    节点类
    '''
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinTree(object):
    '''
    二叉树
    '''
    def __init__(self):
        self.root = Node()
        self.node_list = []  # 右子树为空的节点

    def add(self, data):
        '''
        添加树节点
        '''
        node = Node(data)
        if self.root.data is None:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.node_list.append(self.root)
        else:
            tree_node = self.node_list[0]
            if tree_node.left is None:
                tree_node.left = node
                self.node_list.append(tree_node.left)
            else:
                tree_node.right = node
                self.node_list.append(tree_node.right)
                self.node_list.pop(0)


def get_tree():
    tree = BinTree()
    for data in range(15):
        tree.add(data)
    return tree

if __name__ == '__main__':
    print get_tree()
