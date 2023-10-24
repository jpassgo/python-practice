class MinHeap:
    def __init__(self, heap=[]):
        self.heap = heap

    def __repr__(self):
        return f"{self.heap}"

    def insert(self, value):
        self.heap.append(value)

        val_index_found = False
        val_index = len(self.heap) - 1
        i = int(val_index / 2)
        while val_index >= 0 and val_index_found == False:
            if self.heap[val_index] < self.heap[i]:
                self.heap[val_index], self.heap[i] = self.heap[i], self.heap[val_index]
                val_index = i
                i = int(val_index / 2)
            else:
                val_index_found = True

    def remove(self):
        min_element = self.heap[0]
        last_element = self.heap[len(self.heap) - 1]
        self.heap[0] = last_element


min_heap = MinHeap()
print(min_heap)
min_heap.insert(32)
min_heap.insert(43)
min_heap.insert(12)
min_heap.insert(22)
min_heap.insert(16)
min_heap.insert(3)
print(min_heap)
