# 
# 146. LRU Cache
# 
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. 
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
# 
# https://leetcode.com/problems/lru-cache/
# 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.entries = {}
        self.operation_stack = []

    def get(self, key: int) -> int:
        if key in self.entries:
            self.operation_stack.remove(key)
            self.operation_stack.insert(0, key)
            return self.entries[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:        
        if len(self.entries) >= self.capacity:
            del self.entries[self.operation_stack.pop()]

        if key in self.operation_stack:
            self.operation_stack.remove(key)
       
        self.operation_stack.insert(0, key)
        self.entries[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


lRUCache = LRUCache(2)
lRUCache.put(1, 1) 
lRUCache.put(2, 2) 
assert lRUCache.get(1) == 1
lRUCache.put(3, 3)
assert lRUCache.get(2) == -1
lRUCache.put(4, 4)
assert lRUCache.get(1) == -1
assert lRUCache.get(3) == 3
assert lRUCache.get(4) == 4

