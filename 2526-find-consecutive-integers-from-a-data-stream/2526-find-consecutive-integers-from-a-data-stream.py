class DataStream:

    def __init__(self, value: int, k: int):
        self.matches = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.matches += 1
        else:
            self.matches = 0
        if self.matches >= self.k:
            return True
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)