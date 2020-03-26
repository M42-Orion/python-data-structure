#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   二叉树.py
@Time    :   2020/03/26 15:28:52
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
什么是二叉树：每个节点最多有两个子树的树结构，通常子树被称作“左子树”（left subtree）和“右子树”（right subtree）。

二叉树具备以下数学性质：

    在二叉树的第i层上至多有2^(i-1)个结点（i>0）

    深度为k的二叉树至多有2^k - 1个结点（k>0）

    对于任意一棵二叉树，如果其叶结点数为N0，而度数为2的结点总数为N2，则N0=N2+1;

    具有n个结点的完全二叉树的深度必为 log2(n+1)

    对完全二叉树，若从上至下、从左至右编号，则编号为i 的结点，其左孩子编号必为2i，其右孩子编号必为2i＋1；其双亲的编号必为i/2（i＝1 时为根,除外）

除此之外二叉树分为满二叉树跟完全二叉树
满二叉树:除最后一层无任何子节点外，每一层上的所有结点都有两个子结点二叉树
                    1
                   / \
                  2   3
                 / \ / \
                4  56   7
完全二叉树:设二叉树的深度为h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。
                    1
                   / \
                  2   3
                 / \ / \
                4  56   7
               / \
              8   9
'''
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