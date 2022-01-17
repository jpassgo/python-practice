


class Heap:

    def __init__(self):
        self.array = []

    def insert(self, val):
        self.array.append(val)
        self.bubble_up(len(self.array) - 1)

    def bubble_up(self, index):            
        parent_index = int((index - 2)/2) if index % 2 == 0 else int((index - 1)/2)
        while parent_index >= 0:            
            if self.array[index] < self.array[parent_index]:
                self.array[index], self.array[parent_index] = self.array[parent_index], self.array[index]
                self.bubble_up(parent_index)
            else:
                break


min_heap = Heap()
print(min_heap.array)
min_heap.insert(32)
min_heap.insert(43)
min_heap.insert(12)
min_heap.insert(22)
min_heap.insert(16)
min_heap.insert(3)
print(min_heap.array)