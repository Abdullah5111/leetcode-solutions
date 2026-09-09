"""
394. Decode String  (Medium)

Given an encoded string s, the encoding rule is k[encoded_string],
where the encoded_string inside the square brackets is repeated exactly
k times. k is always a positive integer. Expand it and return the
decoded string. The input is always valid.

Approach: stack of (previous string, repeat count); on ']' pop, repeat
the current segment, and append it to the string from before the '['.

Time:  O(n * maxK) in output size
Space: O(n)
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = []
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((current, num))
                current = []
                num = 0
            elif ch == "]":
                prev, repeat = stack.pop()
                current = prev + current * repeat
            else:
                current.append(ch)
        return "".join(current)


if __name__ == "__main__":
    assert Solution().decodeString("3[a]2[bc]") == "aaabcbc"
    assert Solution().decodeString("3[a2[c]]") == "accaccacc"
    assert Solution().decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert Solution().decodeString("abc3[cd]xyz") == "abccdcdcdxyz"
    assert Solution().decodeString("100[ab]") == "ab" * 100
    print("ok")
