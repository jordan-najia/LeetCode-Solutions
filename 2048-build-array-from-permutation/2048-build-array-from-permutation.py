class Solution(object):
    def buildArray(self, nums):
        
        output = []
        
        for i in range(len(nums)):
            output += [nums[nums[i]]]
        
        return output

s = Solution()
s.buildArray([0,2,1,5,3,4])