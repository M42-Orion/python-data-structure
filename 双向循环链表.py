#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   双向循环链表.py
@Time    :   2020/03/17 16:21:32
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
向循环链表是在双向链表的基础上发展的，双向链表的最后一个节点指向起始节点，起始节点的上一个节点指向最后一个节点，就得到双向循环链表。
双向循环链表比双向链表具有更多的优势，节点的增加和删除有很多优化的地方，从起点开始不必循环完整个链表就可以增加或删除节点。
'''


class Node:
    def __init__(self, item):
        self.item = item  # 该节点值
        self.next = None   # 连接一下一个节点
        self.prev = None  # 上一个节点值


class DoubleCircularLinkedList:
    """双向循环列表类"""

    def __init__(self):
        self._head = None

    @property
    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return not self._head

    @property
    def length(self):
        """
        链表长度
        :return:
        """
        if self.is_empty:
            return 0
        else:
            cur = self._head.next
            n = 1
            while cur != self._head:
                cur = cur.next
                n += 1
            return n

    @property
    def ergodic(self):
        """
        遍历链表
        :return:
        """
        if self.is_empty:
            raise ValueError("ERROR NULL")
        else:
            cur = self._head.next
            print(self._head.item)
            while cur != self._head:
                print(cur.item)
                cur = cur.next

    def add(self, item):
        """
        头部添加节点
        :return:
        """
        node = Node(item)
        if self.is_empty:
            node.next = node
            node.prev = node
            self._head = node
        else:
            node.next = self._head
            node.prev = self._head.prev
            self._head.prev.next = node
            self._head.prev = node
            self._head = node

    def append(self, item):
        """
        尾部添加节点
        :param item:
        :return:
        """
        if self.is_empty:
            self.add(item)
        else:
            node = Node(item)
            cur = self._head.next
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.prev = cur
            node.next = self._head
            self._head.prev = node

    def insert(self, index, item):
        """
        任意位置插入节点
        :param item:
        :return:
        """
        if index == 0:
            self.add(item)
        elif index+1 >= self.length:
            self.append(item)
        else:
            cur = self._head.next
            n = 1
            while cur.next != self._head:
                if n == index:
                    break
                cur = cur.next
                n += 1
            node = Node(item)
            node.prev = cur.prev
            cur.prev.next = node
            node.next = cur
            cur.prev = node

    def search(self, item):
        """
        查找节点是否存在
        :return:
        """
        if self.is_empty:
            return False
        else:
            cur = self._head.next
            if self._head.item == item:
                return True
            else:
                while cur != self._head:
                    if cur.item == item:
                        return True
                    else:
                        cur = cur.next
                return False

    def delete(self, item):
        """
        删除指定值的节点
        :param item:
        :return:
        """
        if self.is_empty:
            raise ValueError("ERROR NULL")
        else:
            if self._head.item == item:
                if self.length == 1:
                    self._head = Node
                else:
                    self._head.prev.next = self._head.next
                    self._head.next.prev = self._head.prev
                    self._head = self._head.next
            cur = self._head.next
            while cur != self._head:
                if cur.item == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                cur = cur.next
