class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.key_store.get(key, [])
        begin = 0
        end = len(values) - 1
        result = ""
        while begin <= end:
            mid = begin + (end - begin) // 2
            if values[mid][1] > timestamp:
                end = mid - 1
            else:
                result = values[mid][0]
                begin = mid + 1
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
