class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in hashMap:
                return(i, hashMap[diff])
            else:
                hashMap[n] = i
