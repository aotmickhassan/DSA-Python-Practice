# Input: nums = [3,2,3]
# Output: 3


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time => O(n); Space => O(1);
        result, count = 0, 0

        for n in nums:
            if count == 0:
                result = n
            count += (1 if n == result else -1)
        return result


        # Time => O(n); Space => O(n);
        # count = {}
        # result, maxCount = 0, 0
        # for n in nums:
        #     count[n] = 1 + count.get(n, 0)
        #     result = n if count[n] > maxCount else result
        #     maxCount = max(count[n], maxCount)
        # return result
