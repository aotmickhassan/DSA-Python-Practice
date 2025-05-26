class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        # Complexity => Time: O(n); Space: O(n)
        N = len(code)
        result = [0] * N

        l = 0
        cur_sum = 0
        
        for r in range(N + abs(k)):
            
            
            cur_sum += code[r % N]
            
            if r - l + 1 > abs(k):
                cur_sum -= code[l % N]
                l = (l + 1) % N

            if r - l + 1 == abs(k):
                if k > 0:
                    result[(l - 1) % N] = cur_sum
                elif k < 0:
                    result[(r + 1) % N] = cur_sum

        return result
    
        # Complexity => Time: O(n); Space: O(n)
        # N = len(code)
        # result = [0] * N

        # for i in range(N):
        #     if k > 0:
        #         for j in range(i + 1, i + 1 + k):
        #             result[i] += code[j % N]
        #     elif k < 0:
        #         for j in range(i - 1, i - 1 - abs(k), -1):
        #             result[i] += code[j % N]

        # return result


"""
Example 1:
Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.

Example 2:
Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 

Example 3:
Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
"""
