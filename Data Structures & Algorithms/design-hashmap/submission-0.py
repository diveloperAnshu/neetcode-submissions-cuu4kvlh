class MyHashMap:
    def __init__(self):
        # Create a list filled with -1 for all possible keys (0 to 1000000)
        self.Map = [-1] * 1000001
        

    def put(self, key: int, value: int) -> None:
        # Directly overwrite the value at that specific index
        self.Map[key] = value
        

    def get(self, key: int) -> int:
        # Just return the value at the index (it will be -1 if never set)
        return self.Map[key]
        

    def remove(self, key: int) -> None:
        # Instead of deleting the index, reset it back to -1
        self.Map[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)