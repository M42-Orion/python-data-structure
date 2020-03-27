#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   希尔排序.py
@Time    :   2020/03/27 12:57:30
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
希尔排序是插入排序的一种又称“缩小增量排序”，是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定排序算法。

希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。

希尔排序的核心是对步长的理解，步长是进行相对比较的两个元素之间的距离，随着步长的减小，相对元素的大小会逐步区分出来并向两端聚拢，当步长为1的时候，就完成最后一次比较，那么序列顺序就出来了。
'''
def shell_sort(items):
    """
    希尔排序
    :param items: 
    :return: 
    """
    n = len(items)
    step = n // 2
    while step > 0:
        for cur in range(step, n):
            i = cur
            while i >= step and items[i-step] > items[i]:
                items[i - step], items[i] = items[i], items[i-step]
                i -= step
        step = step // 2
    return items
