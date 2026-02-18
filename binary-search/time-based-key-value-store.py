class TimeMap:
     def __init__(self):
          self.times = {}

     def set(self, key: str, value: str, timestamp: int) -> None:
          if self.times.get(key) is not None:
               self.times[key].append([timestamp, value])
          else:
               self.times[key] = [[timestamp, value]]

     def get(self, key: str, timestamp: int) -> str:
          # binary-search
          # Returns most recently saved timestamp <= timestamp
          if self.times.get(key) is None or len(self.times[key]) == 0:
               return ""
          
          timestamps = self.times[key]
          l, r = 0, len(timestamps) - 1
          highest = 0
          while l <= r:
               mid = (l+r) // 2
               if timestamps[mid][0] == timestamp:
                    return timestamps[mid][1]
               if timestamps[mid][0] < timestamp:
                    highest = timestamps[mid][1]
                    l = mid + 1
               else:
                    r = mid - 1

          if highest == 0: return ""
          return highest


timemap = TimeMap()
# timemap.set("alice", "happy", 1)
# print(timemap.get("alice", 1))
# print(timemap.get("alice", 2))
# timemap.set("alice", "happy", 3)
# print(timemap.get("alice", 3))

timemap.set("key1", "value1", 10)
print(timemap.get("key1", 1))
print(timemap.get("key1", 10))
print(timemap.get("key1", 11))

["TimeMap", "set", ["key1", "value1", 10], "get", ["key1", 1], "get", ["key1", 10], "get", ["key1", 11]]

# "foo" → [(1,"bar"), (4,"bar2"), (10,"bar3")]
# get(foo, 6)


# [1,4,10,20], 6 | return 1
# [1,4,5,20,100,120], 101 | return 100
# [1,4,6,20,100,120], 5 | return 4

# def modified_binary_search(nums, target):
#      if len(nums) == 0: return -1
#      l, r = 0, len(nums)-1
#      highest = 0
#      while l <= r:
#           mid = (l+r)//2
#           if nums[mid] == target: 
#                return mid
#           if nums[mid] < target:
#                highest = mid
#                l = mid+1
#           else:
#                r = mid-1
#      return highest

# nums = [1,4,10,20]
# target = 23
# x = modified_binary_search(nums, target)
# print(x)
               
          