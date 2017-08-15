# -*- coding: utf-8 -*-

'''
二叉树
'''


class BinaryTree(object):

    def __init__(self, node):
        self.node = node
        self.left = None
        self.right = None

    def insert_left(self, node):
        if self.left is None:
            self.left = BinaryTree(node)
        else:
            tree = BinaryTree(node)
            tree.left = self.left
            self.left = tree

    def insert_right(self, node):
        if self.right is None:
            self.right = BinaryTree(node)
        else:
            tree = BinaryTree(node)
            tree.right = self.right
            self.right = tree

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_root_value(self, node):
        self.node = node

    def get_root_value(self):
        return self.node


def build_tree_by_list(node_list):
    if not node_list:
        return None

    tree = BinaryTree(node_list[0])

    for index, node in enumerate(node_list[1:]):
        if index % 2 != 0:
            tree.insert_left(node)
        else:
            tree.insert_right(node)

    return tree
