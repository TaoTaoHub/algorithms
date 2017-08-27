#二叉堆
class Heap(object):

    list = [0]
    length = 0
    def __init__(self, list):
        for x in list:
            self.insert(x)


    def delMax(self):
        if not self.length:
            return
        max = self.list[1]
        self.list[1] = self.list[self.length]   #
        del self.list[self.length]              #
        self.length -= 1                        #减小堆
        self.__sink(1)                          #重建堆
        return max

    def insert(self, value):
        #放到堆末尾然后执行有序化
        self.length += 1
        self.list.insert(self.length, value)
        self.__swim(self.length)
        return self.list

    #自顶向下的有序化
    def __sink(self, k):
        while k < self.length:
            if self.list[k] < self.list[2*k]:
                self.list[k], self.list[2*k] = self.list[2*k], self.list[k]
                k = 2*k
            elif self.list[k] < self.list[2*k+1]:
                self.list[k], self.list[2*k+1] = self.list[2*k+1], self.list[k]
                k = 2*k+1
            else:
                break
        return 1

    #自下往上的有序化
    def __swim(self, k):
        if k <= 1:
            return 1
        while self.list[k] > self.list[k//2] and k > 1:
            self.list[k], self.list[k//2] = self.list[k//2], self.list[k]
            k = k//2
        return 1

testlist = [9, 17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
Heap = Heap(testlist)#生成堆
print(Heap.list)

print(Heap.delMax())
print(Heap.list)

print(Heap.delMax())
print(Heap.list)

print(Heap.delMax())
print(Heap.list)

