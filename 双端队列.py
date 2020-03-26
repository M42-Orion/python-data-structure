#! /structrue/Scripts/python
# -*- encoding: utf-8 -*-
'''
@File    :   双端队列.py
@Time    :   2020/03/26 15:21:34
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
 什么是双端队列？双端队列是在普通队列的基础上，既可以在前端弹出元素也可以在前端插入元素，既可以在后端插入元素也可以在后端弹出元素，下面来实现这一基本模型。
'''
class Deque(object):
    """双端队列"""
    def __init__(self):
        self._items = []

    @property
    def is_empty(self):
        """
        判断队列是否为空
        :return:
        """
        return self._items == []

    @property
    def size(self):
        """
        返回队列大小
        :return:
        """
        return len(self._items)

    def add_front(self, item):
        """
        在队头添加元素
        :param item:
        :return:
        """
        self._items.insert(0, item)

    def add_rear(self, item):
        """
        在队尾添加元素
        :param item:
        :return:
        """
        self._items.append(item)

    def remove_front(self):
        """
        从队头删除元素
        :return:
        """
        return self._items.pop(0)

    def remove_rear(self):
        """
        从队尾删除元素
        :return:
        """
        return self._items.pop()

'''
 双端队列分类：

输出受限的双端队列：允许在一端进行插入和删除，但在另一端只允许插入的双端队列称为输出受限的双端队列。



输入受限的双端队列：允许在一端进行插入和删除，但在另一端只允许删除的双端队列称为输入受限的双端队列，而如果限定双端队列从某个端点插入的元素只能从该端点删除，则该双端队列就蜕变为两个栈底相邻接的栈了。
'''