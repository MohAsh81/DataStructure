def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)

    return h % 100


class HashTable:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)

        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if len(self.arr[h]) == 0:
            self.arr[h].append([key, value])
        else:
            for i in range(len(self.arr[h])):
                if self.arr[h][i][0] == key:
                    self.arr[h][i].append(value)
                else:
                    pass

    def __getitem__(self, key):
        h = self.get_hash(key)
        if len(self.arr[h]) == 0:
            raise Exception("Key not found")
        else:
            for i in self.arr[h]:
                for j in range(1, len(i)):
                    if i[0] != key:
                        pass
                    else:
                        print((i[0], i[j]))
        return ""

    def __delitem__(self, key):
        h = self.get_hash(key)
        if len(self.arr[h]) == 0:
            raise Exception("Key not found")
        elif len(self.arr[h]) == 1:
            self.arr[h].pop()
        else:
            for i in self.arr[h]:
                for j in range(1, len(i)):
                    if i[0] != key:
                        pass
                    else:
                        self.arr[h].pop(i)
        return ""


# if __name__ == '__main__':
#     obj = HashTable()
#     obj.__setitem__("march 6", 120)
#     obj.__setitem__("march 6", 78)
#     obj.__setitem__("march 8", 67)
#     obj.__setitem__("march 9", 4)
#     obj.__setitem__("march 17", 459)
#     print(obj.__delitem__('march 6'))
#     print(obj.arr)
