#二叉堆
class Heap(object):

    list = [0]
    k = 0
    def __init__(self, list):


    def delMax(self):
        max = self.list[1]
        return self.list[0]

    def insert(self, value):
        #放到堆末尾然后执行有序化
        self.k += 1
        self.list[self.k] = value
        self.__swim(self.k)
        return

    #自顶向下的有序化
    def __sink(self, k):

        return

    #自下往上的有序化
    def __swim(self, k):

        return


testlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
Heap = Heap(testlist)
max = Heap.delMax()
print(max)
