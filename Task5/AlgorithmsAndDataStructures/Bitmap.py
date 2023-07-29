class Bitmap:
    def __init__(self, size):
        self.size = size
        self.bits = [False] * size

    def set_bit(self, index):
        if 0 <= index < self.size:
            self.bits[index] = True
        else:
            raise IndexError("Index out of range")

    def clear_bit(self, index):
        if 0 <= index < self.size:
            self.bits[index] = False
        else:
            raise IndexError("Index out of range")

    def test_bit(self, index):
        if 0 <= index < self.size:
            return self.bits[index]
        else:
            raise IndexError("Index out of range")


bitmap = Bitmap(10)
bitmap.set_bit(2)
bitmap.set_bit(5)

print(bitmap.test_bit(2))
print(bitmap.test_bit(5))
print(bitmap.test_bit(8))

bitmap.clear_bit(5)
print(bitmap.test_bit(5))
