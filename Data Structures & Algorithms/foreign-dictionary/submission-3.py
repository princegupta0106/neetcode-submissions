class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph =defaultdict(set)
        indegree ={}
        # initialized indegree to 0 
        for word in words:
            for char in word: 
                indegree[char] =0
        # build graph
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            # wrong case
            if len(word1) > len(word2) and word1.startswith(word2):
                return ''
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]: 
                        indegree[word2[j]] += 1
                    graph[word1[j]].add(word2[j])
                    break
        
        q = deque()
        for c in indegree.keys(): 
            if not indegree[c] :
                q.append(c)
        res = ''
        while(q):
            char = q.popleft()
            res += char
            for nei in graph[char]:
                indegree[nei] -=1 
                if  indegree[nei] ==0: 
                    q.append(nei)
        if len(res) != len(indegree):
            return ''
        return res



        