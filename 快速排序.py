#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   快速排序.py
@Time    :   2020/03/27 12:49:17
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
从序列中找出一个基准元素，然后大于该元素的放到一边，小于该元素的放到另一边形成分区；然后在分别冲大小分区中再找基准再分别分出相对大小分区，这样递归的完成快速排序。
'''
def quick_sort(data):    
    """快速排序"""    
    if len(data) >= 2:  # 递归入口及出口        
        mid = data[len(data)//2]  # 选取基准值，也可以选取第一个或最后一个元素        
        left, right = [], []  # 定义基准值左右两侧的列表        
        data.remove(mid)  # 从原始数组中移除基准值        
        for num in data:            
            if num >= mid:                
                right.append(num)            
            else:                
                left.append(num)        
        return quick_sort(left) + [mid] + quick_sort(right)    
    else:        
        return data

print(quick_sort([2,3,1,4,6,3,4,8,6,3]))
