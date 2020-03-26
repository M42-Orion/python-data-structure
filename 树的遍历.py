#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   树的遍历.py
@Time    :   2020/03/26 15:39:11
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
深度遍历和广度遍历是相对的概念，深度遍历是沿着树的深度遍历树的节点，尽可能深的搜索树的分支；广度遍历是从树的根层级开始一层一层的遍历，遍历完上一层再遍历下一层；

但对于深度遍历而言还有三种方式：先序遍历/中序遍历/后序遍历；
先序遍历的顺序为：根节点->左子树->右子树；
中序遍历为：左子树->根节点->右子树；
后序遍历是：左子树->右子树->根节点；
其中的序指的是根节点相对于左右节点的遍历位置。
'''
#深度遍历
class Node:
    """节点类"""
    def __init__(self, elem, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """树类"""
    def __init__(self, root=None):
        self._root = root

    def add(self, item):
        node = Node(item)
        if not self._root:
            self._root = node
            return
        queue = [self._root]
        while queue:
            cur = queue.pop(0)
            if not cur.lchild:
                cur.lchild = node
                return
            elif not cur.rchild:
                cur.rchild = node
                return
            else:
                queue.append(cur.rchild)
                queue.append(cur.lchild)

    def preorder(self, root):
        """
        先序遍历-递归实现
        :param root:
        :return:
        """
        if not root:
            raise ValueError("ROOT ERROR")
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """
        中序遍历-递归实现
        :param root:
        :return:
        """
        if not root:
            raise ValueError("ROOT ERROR")
        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)

    def postorder(self, root):
        """
        后序遍历-递归实现
        :param root: 
        :return: 
        """
        if not root:
            raise ValueError("ROOT ERROR")
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)

#广度遍历
class Node:
    """节点类"""
    def __init__(self, elem, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """树类"""
    def __init__(self, root=None):
        self._root = root

    def breadth_travel(self, root):
        """
        广度优先-队列实现
        :param root:
        :return:
        """
        if not root:
            raise ValueError("ROOT ERROR")
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild:
                queue.append(node.lchild)
            elif node.rchild:
                queue.append(node.rchild)