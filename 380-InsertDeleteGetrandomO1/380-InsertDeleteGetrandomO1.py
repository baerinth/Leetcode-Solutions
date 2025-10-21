# Last updated: 10/21/2025, 2:03:14 PM
class RandomizedSet:

    def __init__(self):
        self.lst = set()

    def insert(self, val: int) -> bool:
        if val not in self.lst:
            self.lst.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.lst:
            self.lst.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(tuple(self.lst))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()