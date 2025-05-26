class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result_arr = 0
        N = len(arr)
        prefix_cnt = [0] * 1001

        for j in range(N - 1):
            for k in range(j + 1, N):
                if abs(arr[j] - arr[k]) <= b:
                    r = min(arr[j] + a, arr[k] + c)
                    l = max(arr[j] - a, arr[k] - c)

                    l = max(l, 0)
                    r = min(r, 1000)

                    if l <= r:
                        result_arr += prefix_cnt[r] - (
                            0 if l == 0 else prefix_cnt[l - 1]
                        )

            for index in range(arr[j], 1001):
                prefix_cnt[index] += 1

        return result_arr

        # result_arr = 0
        # N = len(arr)

        # for i in range(N - 2):
        #     for j in range(i + 1, N - 1):
        #         for k in range(j + 1, N):
        #             if (
        #                 abs(arr[i] - arr[j]) <= a
        #                 and abs(arr[j] - arr[k]) <= b
        #                 and abs(arr[i] - arr[k]) <= c
        #             ):
        #                 result_arr += 1

        # return result_arr


# Example 1:
# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].

# Example 2:
# Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
# Output: 0
# Explanation: No triplet satisfies all conditions.
