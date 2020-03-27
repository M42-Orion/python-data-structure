#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   插入排序.py
@Time    :   2020/03/27 12:55:48
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
 插入排序，其原理是通过构建一个初始的有序序列，然后从无需序列中抽取元素，插入到有序序列的相对排序位置，就像将一堆编号混乱的书，一本一本的放到书架上，找到上下编号之间的位置插入，最后完成整理。
'''
def insert_sort(items):
    for i in range(1, len(items)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if items[j] < items[j-1]:
                items[j], items[j-1] = items[j-1], items[j]
    return items