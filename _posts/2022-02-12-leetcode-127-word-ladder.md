---
layout      : single
title       : LeetCode 127. Word Ladder
tags 		: LeetCode Hard HashTable String BFS
--- 
每日題，最近幾乎都在DP，復健一下。

# 題目
輸入字串beginWord,endWord及字串陣列wordList，求把beginWord變成endWord的途中總共有多少字串。  
每次轉換只能改變其中一個字元，且轉換完的結果必須要在wordList裡面才合法。如果無法轉換則回傳0。

# 解法
先建立一個叫做wd的set，把wordList塞進去，每次查詢時間壓到O(1)。  
要想要轉換成功，endWord一定要在wd裡面，先檢查有沒有，否則直接回傳0。  
接下來開始做BFS，把初始字串及計數1塞入deque中，對字串的每一個位置分別替換成所有小寫字母，並檢查新字串是否在wd中，若存在則將(新字串,計數+1)押入deque。若當前字詞和endWord相等則回傳計數。  
注意：最短的轉換順序不會出現重複的字詞，所以wd中每個字詞一經配對成功就該即時移除，否則會造成多餘的計算。

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wd = set(wordList)
        if endWord not in wd:
            return 0
        N = len(beginWord)
        q = deque([(beginWord, 1)])

        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            for i in range(N):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i]+c+word[i+1:]
                    if newWord in wd:
                        q.append((newWord, step+1))
                        wd.remove(newWord)

        return 0
```
