from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq_dict = defaultdict(OrderedDict)
        self.min_freq = 0

    def _update_frequency(self, key):
        freq = self.cache[key][1]
        self.freq_dict[freq].pop(key)
        if not self.freq_dict[freq]:
            # Remove the frequency level if it becomes empty
            del self.freq_dict[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        freq += 1
        self.cache[key][1] = freq
        self.freq_dict[freq][key] = None

    def get(self, key):
        if key in self.cache:
            self._update_frequency(key)
            return self.cache[key][0]
        return None

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self.cache:
            self.cache[key][0] = value
            self._update_frequency(key)
        else:
            if len(self.cache) >= self.capacity:
                # Evict the LFU item (from the minimum frequency level) if the cache is full
                evict_key, _ = self.freq_dict[self.min_freq].popitem(last=False)
                del self.cache[evict_key]
            self.cache[key] = [value, 1]
            self.freq_dict[1][key] = None
            self.min_freq = 1


lfu_cache = LFUCache(3)
lfu_cache.put(1, "A")
lfu_cache.put(2, "B")
lfu_cache.put(3, "C")

print(lfu_cache.get(2))  # Output: B (Frequency of 2 increased to 2)
print(lfu_cache.get(1))  # Output: A (Frequency of 1 increased to 2)
print(lfu_cache.get(4))  # Output: None (Not in the cache)
print()
print(lfu_cache.cache)
