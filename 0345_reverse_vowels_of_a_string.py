"""
345. Reverse Vowels of a String  (Easy)

Time:  O(n)
Space: O(n)
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        lo, hi = 0, len(chars) - 1
        while lo < hi:
            if chars[lo] not in vowels:
                lo += 1
            elif chars[hi] not in vowels:
                hi -= 1
            else:
                chars[lo], chars[hi] = chars[hi], chars[lo]
                lo += 1
                hi -= 1
        return "".join(chars)


if __name__ == "__main__":
    assert Solution().reverseVowels("IceCreAm") == "AceCreIm"
    assert Solution().reverseVowels("leetcode") == "leotcede"
    assert Solution().reverseVowels("aA") == "Aa"
    assert Solution().reverseVowels("bcdfg") == "bcdfg"
    assert Solution().reverseVowels("") == ""
    print("ok")
