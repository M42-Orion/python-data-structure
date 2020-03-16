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

