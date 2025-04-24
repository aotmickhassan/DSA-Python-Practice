# Input: s = "abccccdd"
# Output: 7 ["dccaccd"]

from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        prevMap = set()
        res = 0
        
        for char in s:
            if char in prevMap:
                prevMap.remove(char)
                res += 2
            else:
                prevMap.add(char)
                
        if prevMap:
            res += 1
            
        return res

        # count = defaultdict(int)
        # res = 0
        # for char in s:
        #     count[char] += 1
        #     if count[char] % 2 == 0:
        #         res += 2
        # for cnt in count.values():
        #     if cnt % 2:
        #         res += 1
        #         break
        # return res
