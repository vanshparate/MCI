class HashTable():
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[
                                   i]) * i) % self.size  # The ord() function returns an integer representing the Unicode code point of the character.
        return hash

    def get(self, key):
        hash = self._hash(key)
        if self.data[hash]:
            for i in range(len(self.data[hash])):
                if self.data[hash][i][0] == key:
                    return self.data[hash][i][1]
        return None

    def set(self, key, value):
        hash = self._hash(key)
        if not self.data[hash]:
            self.data[hash] = [[key, value]]
        else:
            self.data[hash].append([key, value])
        print(self.data)

    def keys(self):
        keys_array = []
        for i in range(self.size):
            if self.data[i]:
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])):
                        keys_array.append(self.data[i][j][0])
                else:
                    keys_array.append(self.data[i][0][0])
        return keys_array

    def values(self):
        values_array = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values_array.append(self.data[i][j][1])
        return values_array


new_hash = HashTable(2)
# print(new_hash)
# {'size': 2, 'data': [None, None]}


new_hash.set('one', 1)
new_hash.set('two', 2)
new_hash.set('three', 3)
new_hash.set('four', 4)
new_hash.set('five', 5)
print(new_hash)
# {'size': 2, 'data': [[['one', 1], ['five', 5]], [['two', 2], ['three', 3], ['four', 4]]]}

print(new_hash.get('one'))
# 1

print(new_hash.keys())
# ['one', 'five', 'two', 'three', 'four']

print(new_hash.values())
# [1, 5, 2, 3, 4]
