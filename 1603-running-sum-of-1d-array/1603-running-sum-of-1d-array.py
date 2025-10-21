class Solution(object):
    def runningSum(self, nums):
        output = []
        total = 0
        for num in nums:
            total += num
            output.append(total)
        return output

s = Solution()
s.runningSum([1, 2, 3, 4])