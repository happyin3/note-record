# -*- coding: utf-8 -*-

'''
编辑距离

又称Levenshtein距离，是指两个字串之间，由一个转成另一个所需的最少编辑操作次数。
俄罗斯科学家Vladimir Levenshtein在1965年提出这个概念。

## 参考
编辑距离（Levenshtein距离）详解（附python实现），http://blog.csdn.net/luo123n/article/details/9999481
Levenshtein距离及其python实现，http://blog.csdn.net/Sinsa110/article/details/54176145

## 变形
另类编辑距离，传统的编辑距离里面有3中操作，即插入、删除、替换。假定现在编辑距离只允许任意两种操作。

## 应用
DNA分析、拼音纠错、命名实体抽取、实体共指、机器翻译等方面有广泛应用。
'''


def levenshtein(first, second):
    '''
    编辑距离
    '''
    if len(first) == 0 or len(second) == 0:
        return len(first) + len(second)

    first_len = len(first) + 1
    second_len = len(second) + 1
    distance_matrix = [range(second_len) for i in range(first_len)]

    for i in range(1, first_len):
        for j in range(1, second_len):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(deletion, insertion, substitution)

    return distance_matrix[first_len-1][second_len-1]

if __name__ == '__main__':
    first = '123'
    second = '321'
    print(levenshtein(first, second))
