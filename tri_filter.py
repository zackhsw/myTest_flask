import collections


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:
    instance = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def __new__(cls):
        if cls.instance is None:
            obj = super(Trie, cls).__new__(cls)
            cls.instance = obj

        return cls.instance

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True


if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    word = '六六六'
    word1 = '剧毒'
    prefix = '剧'
    obj = Trie()
    obj1 = Trie()
    print('id----', id(obj), id(obj1))
    obj.insert(word)
    obj.insert(word1)
    param_2, ret = obj.search(word)
    param_3 = obj.startsWith(prefix)
    print('---' * 10, param_2, ret, param_3, '*' * 5, obj.root.children)
#  

# https://blog.csdn.net/IOT_victor/article/detail/88936762
