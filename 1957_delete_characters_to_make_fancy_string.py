"""
1957. Delete Characters to Make Fancy String  (Easy)

Time:  O(n)
Space: O(n)  (for the output)
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        n = len(s)
        ans = s[0]
        for i in range(1, n):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                ans += s[i]
        return ans


if __name__ == "__main__":
    assert Solution().makeFancyString("leeetcode") == "leetcode"
    assert Solution().makeFancyString("aaabaaaa") == "aabaa"
    assert Solution().makeFancyString("aab") == "aab"
    assert Solution().makeFancyString("a") == "a"
    print("ok")
