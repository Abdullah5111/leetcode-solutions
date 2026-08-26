class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        x = 1
        n = len(s)
        for i in range(1, n):
            if s[i] == s[i-1]:
                x += 1
            else:
                if x == k:
                    return True
                x = 1
        return x == k
