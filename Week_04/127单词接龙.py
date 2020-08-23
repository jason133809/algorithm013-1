class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        res = 1
        queue = [beginWord]
        seen = set()
        next_level = set()
        wordList = set(wordList)
        length = len(beginWord)
        tag = 0
        while queue:
            num = len(queue)
            while num:
                num -= 1
                curr = queue.pop()
                curr_li = list(curr)
                for i in range(length):
                    char = curr_li[i]
                    for j in string.ascii_lowercase:
                        curr_li[i] = j
                        word = "".join(curr_li)
                        if word not in seen and word in wordList:
                            next_level.add(word)
                            if word == endWord:
                                tag = 1
                    curr_li[i] = char
            res += 1
            if tag == 1:
                break
            seen |= next_level
            queue = list(next_level)
            next_level.clear()
        return res if tag else 0