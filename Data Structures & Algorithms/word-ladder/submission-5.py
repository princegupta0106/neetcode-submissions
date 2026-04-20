from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        wordSet = set(wordList)
        graph = defaultdict(list)

        for word in wordSet:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    word2 = word[:i] + c + word[i+1:]
                    if word2 in wordSet:
                        graph[word].append(word2)

        # BFS
        level = 1
        visited = set([beginWord])
        temp = [beginWord]
        print (graph)

        while temp:
            q = temp
            temp = []

            for word in q:
                if word == endWord:
                    return level

                for nei in graph[word]:
                    if nei not in visited:
                        visited.add(nei)
                        temp.append(nei)

            level += 1

        return 0