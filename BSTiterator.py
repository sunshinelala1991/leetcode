import string

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}
        self.myword=None



class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        node=self.root
        for c in enumerate(word):
            if c not in node.dic:
                node.dic[c]=TrieNode()
            node=node.dic[c]

        node.myword=word



    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        node=self.root

        for c in word:
            if c not in node.dic:
                return False
            node=node.dic[c]
        return node.myword==word


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        node=self.root

        for c in prefix:
            if c not in node.dic:
                return False
            node=node.dic[c]
        return True



# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

