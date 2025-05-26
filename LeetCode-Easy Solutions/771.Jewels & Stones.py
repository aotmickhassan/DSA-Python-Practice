class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Complexity => Time: O(n+m); Space: O(n); 
        # where-> n=len(jewels), m=len(stones)
        jewel_set=set(jewels) #jewel_set = {'a', 'A'}
        count=0
        
        for stone in stones:
            if stone in jewel_set: #Time: O(1)
                count+=1
                
        return count
    
    
    
        #    # Complexity => Time: O(n*m); Space: O(1); 
        #    # where-> n=len(jewels), m=len(stones)
        #     count=0
            
        #     for stone in stones:
        #         if stone in jewels:  #Time: O(n)
        #             count+=1
                    
        #     return count


"""
Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
"""