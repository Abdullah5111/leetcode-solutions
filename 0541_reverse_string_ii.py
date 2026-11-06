"""
541. Reverse String II  (Easy)

Given a string s and an integer k, reverse the first k characters for
every 2k characters counting from the start of the string. If fewer
than k characters are left, reverse all of them; if between k and 2k
are left, reverse the first k and leave the rest as is.

Approach: walk the string in blocks of k, reversing every other block
(toggled by a flag). The leftover tail of n % k characters is reversed
only if it falls on a "reverse" turn.

Time:  O(n)
Space: O(n)
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        x = n // k
        res = ""
        flag = True
        for i in range(x):
            temp = s[i*k:(i+1)*k]
            if flag:
                temp = temp[::-1]
                flag = False
            else:
                flag = True
            res += temp
        x = n % k
        if x:
            temp = s[-x:]
            if flag:
                temp = temp[::-1]
            res += temp
        return res


if __name__ == "__main__":
    assert Solution().reverseStr("abcdefg", 2) == "bacdfeg"
    assert Solution().reverseStr("abcd", 2) == "bacd"
    assert Solution().reverseStr("abc", 5) == "cba"  # fewer than k left
    assert Solution().reverseStr("abcdef", 4) == "dcbaef"  # between k and 2k left
    assert Solution().reverseStr("a", 1) == "a"
    print("ok")
