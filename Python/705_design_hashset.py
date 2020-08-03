class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Number of buckets assumed reasonably greater than the number of operations
        # if all operations were addition
        self.num_buckets = 15000
        self.buckets = [[] for _ in range(self.num_buckets)]
        
    def get_index(self, key):
        return key % self.num_buckets
    
    
    def add(self, key: int) -> None:
        i = self.get_index(key) 
        if key not in self.buckets[i]:
            self.buckets[i].append(key)
        

    def remove(self, key: int) -> None:
        i = self.get_index(key)
        if key in self.buckets[i]:
            self.buckets[i].remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = self.get_index(key)
        if key in self.buckets[i]:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
