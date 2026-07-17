"""
1957. Delete Characters to Make Fancy String  (Easy)

A fancy string is one where no three consecutive characters are equal. Given a
string `s`, delete the minimum number of characters so that it becomes fancy,
and return the result. The answer is guaranteed to be unique.

Approach: scan left to right tracking the run length of the current character.
Reset the run to 1 whenever the character changes; otherwise increment it. Keep
a character only while its run length is at most 2 — the third (and beyond) of
any run is deleted. Constraints guarantee len(s) >= 1, so s[0] is safe to seed.

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
