#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   单链表.py
@Time    :   2020/03/17 14:43:32
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
 单链表
 链表是一个个节点连接而成，节点由两部分构成：元素域、链接域；链接域链接下一个节点，从而构成一条链条，而python主要实现单个节点对象，从而构成链条。
___________________   ___________________
|元素|指向下一个结点|->|元素|指向下一个结点|->.....
￣￣￣￣￣￣￣￣￣￣    ￣￣￣￣￣￣￣￣￣￣
链表是一个个节点连接而成，节点由两部分构成：元素域、链接域；链接域链接下一个节点，从而构成一条链条，而python主要实现单个节点对象，从而构成链条。
'''

# 节点对象


class Node:
    def __init__(self, item):
        self.item = item  # 该节点值
        self.next = None  # 连接一下一个节点

    def look(self):
        print(self.item)

# 链条对象


class SinglyLinkedList:
    """链表对象"""

    def __init__(self):
        self._head = None

    def add(self, item):
        """
        头部添加节点
        :param item: 节点值
        :return:
        """
        node = Node(item)  # 实例化一个头节点
        node.next = self._head  # 下一个指向暂时为None
        self._head = node  # 自己将作为下一个结点的next指向

    def append(self, item):
        """
        尾部添加节点
        :param items:
        :return:
        """
        cur = self._head
        if not cur:  # 判断是否为空链表
            self.add(item)
        else:
            node = Node(item)
            while cur.next:
                cur = cur.next
            cur.next = node

    def ergodic(self):
        """
        遍历链表
        :return:
        """
        cur = self._head
        if not cur:
            print('None')
        else:
            while cur.next:
                print(cur.item, end=' ')
                cur = cur.next
            print(cur.item)

    @property
    def is_empty(self):
        """
        判断链表是否为空，只需要看头部是否有节点
        :return:
        """
        if self._head:
            return False
        else:
            return True

    @property
    def length(self):
        """
        获取链表长度
        :return:
        """
        cur = self._head
        n = 0
        if not cur:
            return n
        else:
            while cur.next:
                cur = cur.next
                n += 1
            return n+1

    def insert(self, index, item):
        """
        在指定位置插入节点(设置索引从0开始)
        :param item:
        :return:
        """
        if index == 0:  # 当索为0则头部插入
            self.add(item)
        elif index >= self.length:  # 当索引超范围则尾部插入
            self.append(item)
        else:  # 找到插入位置的上一个节点，修改上一个节点的next属性
            cur = self._head
            n = 1
            while cur.next:
                if n == index:
                    break
                cur = cur.next
                n += 1
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def deltel(self, item):
        """
        删除节点
        :param item:
        :return:
        """
        if self.is_empty:  # 节点为空的情况
            raise ValueError("null")
        cur = self._head
        pre = None  # 记录删除节点的上一个节点
        if cur.item == item:  # 当删除节点为第一个的情况
            self._head = cur.next
        while cur.next:
            pre = cur
            cur = cur.next
            if cur.item == item:
                pre.next = cur.next

    def search(self, item):
        """
        查找节点是否存在
        :param item:
        :return:
        """
        cur = self._head
        while None != cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False


test = SinglyLinkedList()
test.add(3)
test.add(4)
test.add(5)
test.add(6)
test.add(7)
# test.append(8)
test.ergodic()
