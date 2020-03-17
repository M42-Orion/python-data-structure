#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   单链表循环链表.py
@Time    :   2020/03/17 15:28:04
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
 在单向链表的基础上，最后一个节点纸箱头部，定义基本节点对象和链条对象。
    ___________________   __________________          ___________________
--->|元素|指向下一个结点|->|元素|指向下一个结点|->.....->|元素|指向下一个结点|
|    ￣￣￣￣￣￣￣￣￣￣   ￣￣￣￣￣￣￣￣￣￣          ￣￣￣￣￣￣￣￣￣￣|
|________________________________________________________________________|
'''

class Node:
    def __init__(self, item):
        self.item = item  # 该节点值
        self.next = None   #  连接一下一个节点


class SinCycLinkedlist:

    def __init__(self):
        self._head = None

    def is_empty(self):
        """
        是否为空链表
        :return:
        """
        return None == self._head

    @property
    def length(self):
        """
        链表长度
        :return:
        """
        if self.is_empty():
            return 0
        n = 1
        cur = self._head
        while cur.next != self._head:
            cur = cur.next
            n += 1
        return n

    def ergodic(self):
        """
        遍历所有节点
        :return:
        """
        if self.is_empty():
            raise ValueError('error null')
        cur = self._head
        print(cur.item)
        while cur.next != self._head:
            cur = cur.next
            print(cur.item)

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            raise ValueError('error null')
        cur = self._head
        if cur.item == item:
            return True
        while cur != self._head:
            if cur.item == item:
                return True
        return False

    def add(self, item):
        """
        头部添加
        :param item:
        :return:
        """
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            self._head = node
            cur.next = node

    def append(self, item):
        """
        尾部添加节点
        :param item:
        :return:
        """
        node = Node(item)
        if self.is_empty():
            self.add(item)
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

    def insert(self, index, item):
        """
        任意位置插入节点
        :param item:
        :return:
        """
        node = Node(item)
        if index+1 >= self.length:
            self.append(item)
        elif index == 0:
            self.add(item)
        else:
            cur = self._head
            n = 1
            while cur.next != self._head:
                pre = cur
                cur = cur.next
                if n == index:
                    break
                n += 1
            pre.next = node
            node.next = cur

    def delete(self, item):
        """
        删除元素
        :param item:
        :return:
        """
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        cur = self._head
        pre = None
        # 若头节点的元素就是要查找的元素item
        if cur.item == item:
            # 如果链表不止一个节点
            if cur.next != self._head:
                while cur.next != self._head:
                    cur = cur.next
                cur.next = self._head.next
                self._head = self._head.next
            else:
                # 链表只有一个节点
                self._head = None
        else:
            pre = self._head
            # 第一个节点不是要删除的
            while cur.next != self._head:
                if cur.item == item:
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            # cur 指向尾节点
            if cur.item == item:
                pre.next = cur.next
