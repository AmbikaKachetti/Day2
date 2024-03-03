class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newNums = [nums[0]]
        value = nums[0]
        for i in range(1, len(nums)):
            value = value + nums[i]
            newNums.append(value)
        return newNums