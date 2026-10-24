class MyHashSet:

    def __init__(self):
        self.size = 0
        self.capacity = 100
        self.buckets = [[]] * self.capacity

    def add(self, key: int) -> None:
        bucketNum = hash(int) % self.capacity
        bucket = self.buckets[bucketNum]
        if key not in bucket: 
            bucket.append(key)
            self.size += 1
        

    def remove(self, key: int) -> None:
        bucketNum = hash(int) % self.capacity
        bucket = self.buckets[bucketNum]
        if key in bucket:
            bucket.remove(key)
            self.size -= 1

        

    def contains(self, key: int) -> bool:
        bucketNum = hash(int) % self.capacity
        bucket = self.buckets[bucketNum]
        if key in bucket: 
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)