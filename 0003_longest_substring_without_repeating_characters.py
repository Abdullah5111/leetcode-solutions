"""
3. Longest Substring Without Repeating Characters  (Medium)

Given a string s, find the length of the longest substring without
repeating characters.

Approach: sliding window — remember each char's last index; when a
char repeats inside the window, jump the left edge past its last seen spot.

Time:  O(n)
Space: O(min(n, alphabet))
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        best = left = 0
        for i, ch in enumerate(s):
            if last.get(ch, -1) >= left:
                left = last[ch] + 1
            last[ch] = i
            best = max(best, i - left + 1)
        return best


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("") == 0
    assert Solution().lengthOfLongestSubstring("abba") == 2
    print("ok")
