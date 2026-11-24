"""
91. Decode Ways  (Medium)

A message of letters A-Z is encoded as numbers with "A" -> "1", ...,
"Z" -> "26". Given a string s of digits, return the number of ways to
decode it. "06" is not valid (no leading zeros), so a "0" can only be
decoded as part of "10" or "20".

Approach: DP like climbing stairs — the ways to decode the prefix ending
at i come from taking one digit (if it isn't "0") plus taking two digits
(if they form 10..26). Only the last two counts are needed.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        prev, cur = 1, 1 if s[0] != "0" else 0  # ways for prefixes of length i-1, i
        for i in range(1, len(s)):
            nxt = cur if s[i] != "0" else 0
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                nxt += prev
            prev, cur = cur, nxt
        return cur


if __name__ == "__main__":
    assert Solution().numDecodings("12") == 2
    assert Solution().numDecodings("226") == 3
    assert Solution().numDecodings("06") == 0  # leading zero
    assert Solution().numDecodings("10") == 1
    assert Solution().numDecodings("100") == 0  # "00" can't be decoded
    assert Solution().numDecodings("27") == 1  # 27 is out of range
    assert Solution().numDecodings("11106") == 2
    print("ok")
