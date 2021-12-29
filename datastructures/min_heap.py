
class MinHeap:

    def __init__(self, heap = []):
        self.heap = heap

    def __repr__(self):
        return f'{self.heap}'

    def insert(self, value):
        self.heap.append(value)
        
        val_index_found = False
        val_index = len(self.heap) - 1        
        i = int(val_index / 2)
        print(i)
        while val_index >= 0 and val_index_found == False:
            if self.heap[val_index] < self.heap[i]:
                self.heap[val_index], self.heap[i] = self.heap[i], self.heap[val_index]
                val_index = i
                i = int(val_index / 2)
            else:
                val_index_found = True

min_heap = MinHeap([18, 23, 76, 98, 35, 22, 64])
print(min_heap)
min_heap.insert(3)
print(min_heap)