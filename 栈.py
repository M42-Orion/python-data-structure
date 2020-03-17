#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   栈.py
@Time    :   2020/03/17 17:12:25
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
 栈（stack）又名堆栈，它是一种运算受限的线性表。其限制是仅允许在表的一端进行插入和删除运算。这一端被称为栈顶，相对地，把另一端称为栈底。向一个栈插入新元素又称作进栈、入栈或压栈，它是把新元素放到栈顶元素的上面，使之成为新的栈顶元素；从一个栈删除元素又称作出栈或退栈，它是把栈顶元素删除掉，使其相邻的元素成为新的栈顶元素。
 在python中已经有实现栈的数据结构，在queue库中的LifoQueue就是一种堆栈，堆栈的实现也是线性表，在Python的queue中是通过列表这一线性顺序表实现的。
 栈可以通过列表实现，不过从某种意义上来说安全系数不高。
'''


class Stack:
    """堆栈结构类"""

    def __init__(self):
        self._item = []

    def push(self, item):
        """
        添加新元素
        :param item:
        :return:
        """
        self._item.append(item)

    @property
    def size(self):
        """
        返回堆栈大小
        :return:
        """
        return len(self._item)

    @property
    def is_empty(self):
        """
        判断是否为空
        :return:
        """
        return not self._item

    def pop(self):
        """
        弹出栈顶元素
        :return:
        """
        return self._item.pop()

    def peek(self):
        """
        返回栈顶元素
        :return:
        """
        return self._item[-1]
