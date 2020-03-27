#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   冒泡排序.py
@Time    :   2020/03/27 12:53:38
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
 太简单，不解释了
'''
def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums