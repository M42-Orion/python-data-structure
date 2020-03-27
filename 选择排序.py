#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   选择排序.py
@Time    :   2020/03/27 12:54:49
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
选择排序，简单而直观，其原理是把序列中的最小值或者最大值找出来放在起始位置，然后再从剩下的序列中找出极值放到起始位置之后，以此类推最后就完成排序。

完成这个过程大致思想：首先需要一个记录器，记录排序排到第几个位置了，然后在剩余的序列中找到极值下标，最后将记录器位置和极值位置元素交换，完成本次选择排序。
'''
def select_sort(items):
    n = len(items)
    for cur in range(n-1):
       item_max = cur
       for i in range(cur+1, n):
           if items[i] > items[item_max]:
               items[i], items[item_max] = items[item_max], items[i]
       if item_max != cur:
           items[cur], items[item_max] = items[item_max], items[cur]
    return items