class TimeMap:

    def __init__(self):
        self.ansMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ansMap:
            self.ansMap[key] = []
        self.ansMap[key].append([value, timestamp])   

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.ansMap.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = r - 1
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Simulating the commands
commands = ["TimeMap", "set", "get", "get", "set", "get", "get"]
params = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

output = []

for i in range(len(commands)):
    if commands[i] == "TimeMap":
        obj = TimeMap()
        output.append(None)
    elif commands[i] == "set":
        obj.set(*params[i])
        output.append(None)
    elif commands[i] == "get":
        result = obj.get(*params[i])
        output.append(result)

print(output)