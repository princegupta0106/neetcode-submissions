class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = set()
        q = deque()
        q.append(0)
        while q:
            i = q.popleft()
            for word in wordDict:
                if i+len(word) in visited:
                    continue
                if s.startswith(word, i):
                    q.append(i+len(word))
                    visited.add(i+len(word))
        return len(s) in visited





        