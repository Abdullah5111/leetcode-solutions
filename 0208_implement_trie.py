"""
208. Implement Trie (Prefix Tree)  (Medium)

Implement a trie with insert, search, and startsWith methods. All
inputs consist of lowercase English letters.

Approach: nested dicts — each node is a dict of child chars plus an
end-of-word marker.

Time:  O(m) per op  (m = word length)
Space: O(total chars)
"""


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def _walk(self, prefix: str) -> dict | None:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return bool(node) and "$" in node

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True
    print("ok")
