"""
1415. The k-th Lexicographical String of All Happy Strings of Length n  (Medium)

Time:  O(n)
Space: O(n)  (for the output)
"""


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        x = 3
        for i in range(1, n):
            x *= 2
        if k > x:
            return ""

        ans = ""
        temp = x // 3
        if k <= x // 3:
            ans += 'a'
            x -= temp * 2
        elif k <= (x // 3) * 2:
            ans += 'b'
            x -= temp * 2
            k -= temp
        else:
            ans += 'c'
            x -= temp * 2
            k -= temp * 2
        n -= 1
        i = 0
        while n:
            temp = x // 2
            if k <= x // 2:
                if ans[i] == 'a':
                    ans += 'b'
                else:
                    ans += 'a'
            else:
                if ans[i] == 'c':
                    ans += 'b'
                else:
                    ans += 'c'
                k -= temp
            x -= temp
            n -= 1
            i += 1
        return ans


if __name__ == "__main__":
    assert Solution().getHappyString(1, 3) == "c"
    assert Solution().getHappyString(1, 4) == ""
    assert Solution().getHappyString(3, 9) == "cab"
    assert Solution().getHappyString(2, 1) == "ab"
    assert Solution().getHappyString(10, 100) == "abacbabacb"
    print("ok")
