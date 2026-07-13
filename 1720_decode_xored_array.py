"""
1720. Decode XORed Array  (Easy)

There is a hidden array `arr` of n non-negative integers. It was encoded into
`encoded` of length n-1 such that encoded[i] = arr[i] XOR arr[i + 1]. You are
also given the integer `first`, which is arr[0]. Return the original array.

Approach: XOR is invertible. Since encoded[i] = arr[i] ^ arr[i + 1], we get
arr[i + 1] = arr[i] ^ encoded[i]. Start from `first` and fold across `encoded`.

Time:  O(n)
Space: O(n)  (for the output)
"""
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for e in encoded:
            arr.append(arr[-1] ^ e)
        return arr


if __name__ == "__main__":
    assert Solution().decode([1, 2, 3], 1) == [1, 0, 2, 1]
    assert Solution().decode([6, 2, 7, 3], 4) == [4, 2, 0, 7, 4]
    assert Solution().decode([], 5) == [5]
    print("ok")
