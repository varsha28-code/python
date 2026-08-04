class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        # code here
        arr.sort()
        n = len(arr)
        i = 0
        ans = 0
        for j in range(n):
            while i < j and arr[j] - arr[i] >= k:
                i += 1
            ans += (j - i)
        return ans
