from collections import OrderedDict


class MRUCache:
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
                # Remove the last item (most recently used) if the cache is full
                self.cache.popitem(last=True)
            self.cache[key] = value


mru_cache = MRUCache(3)
mru_cache.put(1, "A")
mru_cache.put(2, "B")
mru_cache.put(3, "C")
print(mru_cache.cache)
mru_cache.put(3, "C1")

print(mru_cache.get(2))  # Output: B (Most recently used)
print(mru_cache.get(1))  # Output: A (Recently used)
print(mru_cache.get(4))  # Output: None (Not in the cache)
print()
print(mru_cache.cache)
print("Cache is full!")
mru_cache.put(4, "D")
print("Adding new item")
print(mru_cache.cache)
