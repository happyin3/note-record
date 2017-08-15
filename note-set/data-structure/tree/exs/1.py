# -*- coding: utf-8 -*-

'''
求二叉树的最大深度
'''


from binary_tree import build_tree_by_list


def get_max_depth(tree):
    if not tree:
        return 0

    left = get_max_depth(tree.left)
    right = get_max_depth(tree.right)

    return max(left, right) + 1

if __name__ == '__main__':
    node_list = list(range(7))
    tree = build_tree_by_list(node_list)
    max_depth = get_max_depth(tree)
    print max_depth
