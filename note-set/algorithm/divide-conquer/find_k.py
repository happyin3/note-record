# -*- coding: utf-8 -*-

'''
寻找第k个数

# 参考
寻找第K小的数，http://blog.csdn.net/sgbfblog/article/details/7925418

# 变形

# 应用
'''


def quick_sort(data):
    '''
    快速排序
    '''
    left, middle, right = [], [], []

    flag = data[0]

    for value in data:
        if value < flag:
            left.append(value)
        elif value > flag:
            right.append(value)
        else:
            middle.append(value)

    return left, middle, right


def find_k(data, k):
    if len(data) < k or k == 0:
        return -1

    if len(data) == 1:
        return data[0]

    left, middle, right = quick_sort(data)

    llen, mlen = len(left), len(middle)

    if llen >= k:
        return find_k(left, k)
    elif llen+mlen < k:
        return find_k(right, k-llen-mlen)
    else:
        return middle[0]

if __name__ == '__main__':
    data = [2, 0, 1, 3, 4, 5, 6, 7, 8]
    k = 1
    print find_k(data, 8)
