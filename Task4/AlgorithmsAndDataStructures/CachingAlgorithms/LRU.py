from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            # Move the accessed item to the end
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def put(self, key, value):
        if key in self.cache:
            # If the key exists, update its value and move it to the end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the first item (least recently used) if the cache is full
                self.cache.popitem(last=False)
            self.cache[key] = value


lru_cache = LRUCache(3)

lru_cache.put(1, "A")
lru_cache.put(2, "B")
lru_cache.put(3, "C")
print(lru_cache.cache)
lru_cache.put(3, "C1")

print(lru_cache.get(2))  # Output: B (Most recently used)
print(lru_cache.get(1))  # Output: A (Recently used)
print(lru_cache.get(4))  # Output: None (Not in the cache)
print()
print(lru_cache.cache)
print("Cache is full!")
lru_cache.put(4, "D")
print("Adding new item")
print(lru_cache.cache)
