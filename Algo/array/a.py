
class ArrayList:
    def __init__(self, length):
        self.array = []
        self.length = length

    def __getitem__(self, position):
        if position >= self.length:
            return False, ""
        return True, self.array[position]

    def __setitem__(self, key, value):
        if 0 <= key < self.length:
            self.array[key] = value

    def __len__(self):
        return len(self.array)

    def __delete__(self, index):
        if index >= self.length:
            return False
        self.array.pop(index)
        return True

    def insert(self, index, value):
        if 0 <= index < self.length:
            self.array.insert(index, value)
            return True
        return False

    def print(self):
        for item in self:
            print(item)

if __name__ == '__main__':
    array = ArrayList(10)
    array.insert(0, 1)
    array.insert(1, 2)
    array.insert(2, 3)
    array.print()
    """
    (True, 1)
    (True, 2)
    (True, 3)
    """
    print(array.__getitem__(2))  # (True, 3)