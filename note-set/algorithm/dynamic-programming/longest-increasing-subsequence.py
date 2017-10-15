# -*- coding: utf-8 -*-

'''
最长递增子序列

## 参考
最长递增子序列问题的求解，http://www.cnblogs.com/lonelycatcher/archive/2011/07/28/2119123.html
最长递增子序列 O(NlogN)算法，https://www.felix021.com/blog/read.php?1587&guid=5

## 变形
最长连续递增子序列

## 应用
'''


def dy_lis(data):
    '''
    动态规划

    L(j) = 1 + max{L(i)}
    '''
    data_len = len(data)
    l = [1] * data_len
    pre = range(data_len)  # 前序节点

    for i in range(1, data_len):
        for j in range(i):
            if data[i] > data[j] and l[i]-1 < l[j]:
                l[i] = 1 + l[j]
                pre[i] = j
    print pre
    return max(l)

if __name__ == '__main__':
    data = [5, 2, 8, 6, 3, 6, 9, 7]
    res = dy_lis(data)
    print res
