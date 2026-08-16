"""
535. Encode and Decode TinyURL  (Medium)

Time:  O(1) per encode/decode
Space: O(n)  n = number of stored URLs
"""


class Codec:
    def __init__(self):
        self.store = {}

    def encode(self, longUrl: str) -> str:
        key = str(len(self.store))
        self.store[key] = longUrl
        return "http://tinyurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        return self.store[shortUrl.rsplit("/", 1)[1]]


if __name__ == "__main__":
    codec = Codec()
    url = "https://leetcode.com/problems/design-tinyurl"
    assert codec.decode(codec.encode(url)) == url
    a, b = codec.encode("https://a.com"), codec.encode("https://b.com")
    assert a != b
    assert codec.decode(a) == "https://a.com"
    assert codec.decode(b) == "https://b.com"
    print("ok")
