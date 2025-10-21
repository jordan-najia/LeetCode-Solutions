class Solution(object):
    def maximumWealth(self, accounts):
        
        wealths = []

        for i in accounts:
            individual_wealth = sum(i)
            wealths.append(individual_wealth)
        
        wealths.sort(reverse = True)
        return wealths[0]
    
s = Solution()
s.maximumWealth([[1,5],[7,3],[3,5]])

    
        


            

        # add each of those to a new list
        # order the new list
        # print the first item in the list

            

        