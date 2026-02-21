
        partition_1 = self.binary_search(nums, target, 0, l-1)
        partition_2 = self.binary_search(nums, target, l, len(nums)-1)
        if partition_1 != -1:
            return partition_1