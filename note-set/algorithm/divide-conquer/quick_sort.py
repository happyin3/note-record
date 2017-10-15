# -*- coding: utf-8 -*-

'''
快速排序

# 参考
快速排序，https://github.com/qiwsir/algorithm/blob/master/quick_sort.md

'''


def quick_sort(seq):
    less, more, pivot_list = [], [], []

    if len(seq) <= 1:
        return seq

    pivot = seq[0]
    for i in seq:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            pivot_list.append(i)

    less = quick_sort(less)
    more = quick_sort(more)

    return less + pivot_list + more

if __name__ == '__main__':
    seq = [4, 65, 2, -31, 0, 99, 83, 782, 1]
    print quick_sort(seq)
