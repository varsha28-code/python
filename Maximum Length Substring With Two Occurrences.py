class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        left = 0
        ans = 0
        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1
            while count[ch] > 2:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
