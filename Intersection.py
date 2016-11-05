import copy

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        if len(beginWord)==1:
            return 2
        if self.oneChar(beginWord,endWord):
            return 2
        return self.ladder([beginWord],endWord,wordList,2)


    def ladder(self,startWords,endWord,wordList,llen):
        if len(wordList)==0:
            return 0
        nstartWords=[]


        for sword in startWords:
            for i in range(len(sword)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = sword[:i] + c + sword[i+1:]
                    if next_word==endWord:
                        return llen
                    if next_word in wordList:

                        wordList.remove(next_word)
                        nstartWords.append(next_word)
        if len(nstartWords)==0:
            return 0

        return self.ladder(nstartWords,endWord,wordList,llen+1)








    def oneChar(self,word1,word2):

        i=0
        for c1,c2 in zip(word1,word2):
            if c1!=c2:
                i+=1

        return i==1

