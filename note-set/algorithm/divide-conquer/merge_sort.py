# -*- coding: utf-8 -*-

'''
归并排序

是创建在归并操作上的一种有效的排序算法，效率为O(n log n)。1945年由约翰·冯·诺伊曼首次提出。

# 参考
分治算法，http://chenqx.github.io/2015/03/16/Introduction-to-Divide-and-Conquer-Algorithm/
python归并排序--递归实现，http://www.jianshu.com/p/3ad5373465fd

# 变形

# 应用
'''


def merge_sort(seq):
    '''
    归并排序
    '''
    if len(seq) <= 1:
        return seq

    mid = len(seq) / 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])

    return merge(left, right)


def merge(left, right):
    '''
    合并两个列表
    '''
    i, j = 0, 0
    res = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])

    return res

if __name__ == '__main__':
    seq = [5, 3, 0, 6, 1, 4]
    print merge_sort(seq)
