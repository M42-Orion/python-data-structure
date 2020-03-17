#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   非原始数据结构.py
@Time    :   2020/03/16 22:48:14
@Author  :   望 
@Version :   1.0
@Contact :   2521664384@qq.com
@Desc    :   None
'''

# here put the import lib
'''
 非原始数据之列表于数组
'''

# array
# ###################################################
import array as arr
a = arr.array("I",[3,6,9])
print(type(a))
# array.array
# ###################################################

# lists
# ###################################################
x = []
print(type(x))
# list
x1 = [1,2,3]
print(type(x1))
# list
x2 = list([1,'apple',3])
print(type(x2))
# list
print(x2[1])
# apple
x2[1] = 'orange'
print(x2)
# [1, 'orange', 3]

# list 内置方法
# append 添加
list_num = [1,2,45,6,7,2,90,23,435]
list_char = ['c','o','o','k','i','e']
list_num.append(11) 
print(list_num)
# [1, 2, 45, 6, 7, 2, 90, 23, 435, 11]

# 插入
list_num.insert(0, 11)
print(list_num)
# [11, 1, 2, 45, 6, 7, 2, 90, 23, 435, 11]

# 删除
list_char.remove('o') 
print(list_char)
# ['c', 'o', 'k', 'i', 'e']

# 索引
list_char.pop(-2) # Removes the item at the specified position
print(list_char)
# ['c', 'o', 'k', 'e']

# 排序
list_num.sort()
print(list_num)
# [1, 2, 2, 6, 7, 11, 11, 23, 45, 90, 435]
list.reverse(list_num)
print(list_num)
# [435, 90, 45, 23, 11, 11, 7, 6, 2, 2, 1]
# ###################################################


#列表比数组更强大同时意味着占用更多的内存空间，当我们处理相同数据类型的时候，拥有更快的反应速度，更强的处理能力。
# 处理数字推荐 numpy
'''
 numpy
'''
# ##################################################
import numpy as np

arr_a = np.array([3, 6, 9])
arr_b = arr_a/3 # Performing vectorized (element-wise) operations 
print(arr_b)
# [ 1.  2.  3.]
arr_ones = np.ones(4)
print(arr_ones)
# [ 1.  1.  1.  1.]
multi_arr_ones = np.ones((3,4)) 
print(multi_arr_ones)
# [[ 1.  1.  1.  1.]
#  [ 1.  1.  1.  1.]
#  [ 1.  1.  1.  1.]]
# ##################################################

# Stack:堆栈是根据Last-In-First-Out（LIFO）概念插入和移除的对象的容器。 想象一下这样一种场景，即在一个有一堆盘子的晚宴上，总是在堆顶部添加或移除盘子。 在计算机科学中，这个概念用于评估表达式和语法分析，调度算法/例程等。可以使用Python中的列表来实现堆栈。 将元素添加到堆栈时，它被称为推送操作，而当您删除或删除元素时，它被称为弹出操作。 

# python提供了专门处理堆的库
# ###################################################
import heapq
import random


'''
python 堆
'''
data = list(range(10))
random.shuffle(data)
heap = []
print(data,'原始数据')
for i in data:
    heapq.heappush(heap,i)

print(heap,'建立堆')#建堆

heapq.heappush(heap,0.5)
print(heap,'新数据入堆')#入堆

heapq.heappop(heap)
print(heap,'出堆')

myheap = [1,2,3,5,7,8,9,4,10,333]
heapq.heapify(myheap)
print(myheap,'建立堆')
heapq.heapreplace(myheap,6)
print(myheap,'弹出最小元素，同时插入新元素')
heapq.nlargest(3,myheap)
print(myheap,'返回前三个最大的元素')
heapq.nsmallest(3,myheap)
print(myheap,'返回前三个最小的元素')
# ###################################################

# Queue
# 队列是根据先进先出（FIFO）原则插入和移除的对象的容器。 在现实世界中排队的一个很好的例子是售票柜台的线路，根据他们的到达顺序上车，因此首先到达的人也是第一个离开的人。队列可以有许多不同的类型，但在本教程中仅讨论最基本的类型。 列表实现队列效率不高，因为列表末尾的append（）和pop（）速度很快， 但是，最后插入和从列表开头删除不是那么快，因为它需要元素位置的移动。

# Graphs
# ###################################################
graph = { "a" : ["c", "d"],
          "b" : ["d", "e"],
          "c" : ["a", "e"],
          "d" : ["a", "b"],
          "e" : ["b", "c"]
        }

def define_edges(graph):
    edges = []
    for vertices in graph:
        for neighbour in graph[vertices]:
            edges.append((vertices, neighbour))
    return edges

print(define_edges(graph))
# ###################################################
# Tree
# ###################################################
class Tree:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left  = left
        self.right = right

    def __str__(self):
        return (str(self.info) + ', Left child: ' + str(self.left) + ', Right child: ' + str(self.right))

tree = Tree(1, Tree(2, 2.1, 2.2), Tree(3, 3.1))
print(tree)

# ###################################################

# Tuples元组是另一种标准序列数据类型。 元组和列表之间的区别在于元组是不可变的，这意味着一旦定义，您就无法删除，添加或编辑其中的任何值。 这可能在您可能将控件传递给其他人但您不希望它们操纵集合中的数据但可能只是在数据副本中看到它们或单独执行操作的情况下有用。
# ###################################################
x_tuple = 1,2,3,4,5
y_tuple = ('c','a','k','e')
x_tuple[0]

1

y_tuple[3]

# x_tuple[0] = 0 # Cannot change values inside a tuple

# ###################################################

# Dictionary
# 想实现类似于电话簿的东西，字典是要使用的数据结构。 您之前看到的所有数据结构都不适用于电话簿。
# ###################################################
x_dict = {'Edward':1, 'Jorge':2, 'Prem':3, 'Elisa':4}

del x_dict['Elisa']

print(x_dict)
# {'Edward': 1, 'Jorge': 2, 'Prem': 3}
print(x_dict['Edward']) # Prints the value stored with the key 'Kevin'.
# 1
len(x_dict)
# 3
x_dict.keys()

dict_keys(['Prem', 'Edward', 'Jorge'])

x_dict.values()
dict_values([3, 1, 2])
# ###################################################
# Sets集合是唯一对象的集合。 这些对于创建仅在数据集中包含唯一值的列表很有用。 它是一个无序的集合，但是一个可变的集合。
# ###################################################
x_set = set('CAKE&COKE')
y_set = set('COOKIE')

print(x_set)

# {'A', '&', 'O', 'E', 'C', 'K'}

print(y_set) # Single unique 'o'

# {'I', 'O', 'E', 'C', 'K'}

print(x_set - y_set) # All the elements in x_set but not in y_set
# ###################################################
