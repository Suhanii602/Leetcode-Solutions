class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordset=set(wordDict)
        memo={}
        def dfs(start):
            if start in memo:
                return memo[start]
            if start==len(s):
                return True
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordset:
                    if dfs(end):
                        memo[start]=True
                        return True
            memo[start]=False
            return False
        return dfs(0)