# _*_ coding=utf-8 _*_


import random


"""
归并排序（Merge sort）是建立在归并操作上的一种有效的排序算法。
    该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
算法步骤
1.申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
2.设定两个指针，最初位置分别为两个已经
排序序列的起始位置；
3.比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
4.重复步骤 3 直到某一指针达到序列尾；
5.将另一序列剩下的所有元素直接复制到合并序列尾。
"""


def merge(left: [], right: []):
    """
    :param left: 列表左边区域
    :param right:列表右边区域
    :return:排序后的列表
    """
    result = []
    while left and right:               # 列表至少存在2个元素
        if left[0] <= right[0]:
            result.append(left.pop(0))  # 将较小的元素从删除后添加进新的列表
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def merge_sort(li):
    """
    使用递归的方法先将列表两部分分解成单个元素，再调用merge()进行排序
    :param li:列表
    :return:merge()
    """
    if len(li) < 2:
        return li
    mid = len(li) // 2
    left, right = li[0:mid], li[mid:]
    return merge(merge_sort(left), merge_sort(right))


data = [i for i in range(20)]
random.shuffle(data)


if __name__ == '__main__':
    print(merge_sort(data))