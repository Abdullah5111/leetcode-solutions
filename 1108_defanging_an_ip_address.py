"""
1108. Defanging an IP Address  (Easy)

Time:  O(n)
Space: O(n)
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


if __name__ == "__main__":
    assert Solution().defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
    assert Solution().defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
    assert Solution().defangIPaddr("0.0.0.0") == "0[.]0[.]0[.]0"
    print("ok")
