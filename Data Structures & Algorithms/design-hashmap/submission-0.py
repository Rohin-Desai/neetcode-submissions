class MyHashMap:

    def __init__(self):
        self.cap = 1000
        self.buckets = [[] for _ in range(self.cap)]
        self.size = 0
        

    def put(self, key: int, value: int) -> None:
        bucketNum = hash(key) % self.cap
        b = self.buckets[bucketNum]
        updated = False
        for t in b:
            if t[0] == key: #it's already here!
                t[1] = value
                updated = True
        if updated == False:
            b.append([key,value])
            self.size += 1
        

    def get(self, key: int) -> int:
        bucketNum = hash(key) %  self.cap
        b = self.buckets[bucketNum]
        for t in b:
            if t[0] == key:
                return t[1]
        return -1

        

    def remove(self, key: int) -> None:
        bucketNum = hash(key) % self.cap
        b = self.buckets[bucketNum]
        for t in b:
            if t[0] == key:
                b.remove(t)
                self.size -= 1
                break

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)