class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem

    def insert(self, index, item):
        self.length += 1
        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = item

    def delete(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1


newArray = MyArray()

newArray.push('hi')
newArray.push('you')
newArray.insert(2, 'are')
print(newArray.get(0))
newArray.pop()
newArray.push('are')
newArray.push('nice')
newArray.delete(1)
print(newArray)
