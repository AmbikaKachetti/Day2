# print('Hello World!')
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        newList = []
        for n in nums:
            if n not in newList:
                newList.append(n)
            else:
                return n
