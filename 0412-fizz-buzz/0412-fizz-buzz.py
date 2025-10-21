class Solution(object):
    def fizzBuzz(self, n):
        
        final_list = []

        for i in list(range(1, n+1)):
            if i%3 == 0 and i%5 == 0:
                final_list += ["FizzBuzz"]
            elif i%3 == 0:
                final_list += ["Fizz"]
            elif i%5 == 0:
                final_list += ["Buzz"]
            else:
                final_list += [str(i)]

        return final_list

s = Solution()
s.fizzBuzz(1)
        