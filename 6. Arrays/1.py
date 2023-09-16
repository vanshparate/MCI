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
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def insert(self, index, item):
        self.length += 1
        for i in range(self.length-1, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = item

    def delete(self, index):
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length - 1]
        self.length -= 1


arr = MyArray()
arr.push(6)
# #{'length': 1, 'data': {0: 6}}

arr.push(2)
# #{'length': 2, 'data': {0: 6, 1: 2}}

arr.push(9)
# #{'length': 3, 'data': {0: 6, 1: 2, 2: 9}}

arr.pop()
# #{'length': 2, 'data': {0: 6, 1: 2}}

arr.push(45)
arr.push(12)
arr.push(67)

arr.insert(3,10)

arr.delete(4)


print(arr.get(1))

print(arr)



