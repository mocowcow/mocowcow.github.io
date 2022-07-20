--- 
layout      : single
title       : LeetCode 792. Number of Matching Subsequences
tags        : LeetCode Medium Array String HashTable
---
每日題。官方標籤雖然有字典樹，硬要說的話應該勉強算是吧。不過竟然有人用二分搜來解這題，他們的思路是真的神奇。  

# 題目
輸入字串s和字串陣列words，求words中有多少字串是s的子序列。  

# 解法
把words中所有字元裝進佇列中，並維護雜湊表d，將各個佇列以最前端的字元為key值放入雜湊表中。  
遍歷s中的所有字元c，將以c開頭的佇列全部取出，並彈出前方元素。若佇列清空代表該word為s的子序列，答案+1；否則放回雜湊表對應的位置中。  

s長度N=50000，words最多5000，每個word長度50，乍看之下這個方法複雜度是50000\*5000，其實不然。最壞的情況下，每個word都是只有一種字元的超長字串，那麼最多也只會pop掉5000\*50次，所以事實上複雜度為O(N+(5000*50))=O(N)。  

```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans=0
        d=defaultdict(list)
        
        for w in words:
            d[w[0]].append(deque(w))
            
        for c in s:
            qs=d[c]
            d[c]=[]
            for q in qs:
                if len(q)==1:
                    ans+=1
                else:
                    q.popleft()
                    d[q[0]].append(q)
        
        return ans
```
