class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList : return 0
        wordSet = set(wordList)
        graph = defaultdict(list)
        wordList.append(beginWord)
        def isSame(word1, word2 ,idx):
            word1 = word1[:idx] + word1[idx:]
            word2 = word2[:idx] + word2[idx:]
            return word1 == word2
        s = list('wertyuiopasdfghjklzxcvbnm')
        for word in wordList:
            for i in range(len(word)):
                for c in s :
                    word2 =  word[:i]+ c + word[i+1:]
                    if c != word[i] and word2 in wordSet:
                        graph[word].append(word2)
        #run bfs for shortest path 
        
        level = 0
        visited = set()
        temp = [word]
        while temp: 
            q = temp 
            level+=1 
            temp = []
            for word in q: 
                visited.add(word)
                if word == endWord : return level
                for nei in graph[word]:
                    if nei not in visited:
                        temp.append(nei)

       


        # print (graph)
        return 0
        
                    


