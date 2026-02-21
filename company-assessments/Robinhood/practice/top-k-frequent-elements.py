class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ 
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
        
        Input: nums = [1,1,1,2,2,3], k = 2

        Output: [1,2]

        Example 2:

        Input: nums = [1], k = 1

        Output: [1]
        """
        
        frequencies = {}
        for i in nums: # n
            if frequencies.get(i) is None:
                frequencies[i] = 1
            else:
                frequencies[i] += 1
        
        return list(dict(sorted(frequencies.items(), key=lambda x : x[1], reverse=True)[:k]).keys()) # n log n