---
layout      : single
title       : LeetCode 316. Remove Duplicate Letters
tags 		: LeetCode Medium String Stack Greedy MonotonicStack HashTable
---
每日題。stack六連霸，會不會滿一周呢。 

# 題目
輸入小寫英文字串s，刪掉多餘的字母，讓每個字母最多只出現一次，並保持最小的字典順序。

# 解法
stack之王monotonic stack又來了。  
最小的字典順序意思是盡量把越靠近a的擺到前面，越靠近z的擺到後面。例如'acbabc'，選擇'abc'。  
那如何決定要把哪個位置的字元刪掉？必須符合以下條件：  
1. 要被刪的字元x在之後至少還會出現一次  
2. x的後面要有一個比他順序更小的字元

試著帶入'acbabc'：  
> 'a'  
> 'ac'  
> 輪到字元'b'，'b'小於'c'且'c'之後還會出現1次，丟掉'c'，得到'ab'  
> 'a'出現過了，略過，還是'ab'  
> 'b'也出現過了，略過，還是'ab'  
> 'abc'  

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ctr = Counter(s)
        st = []
        used = set()
        for c in s:
            ctr[c] -= 1
            if c in used:
                continue
            # if c less than prev one and prev one will appear later
            while st and c < st[-1] and ctr[st[-1]] > 0:
                used.remove(st.pop())
            st.append(c)
            used.add(c)

        return ''.join(st)
```

改用陣列紀錄是否出現過，並將出現計數改成最後出現位置，減少多餘運算。

```python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastSeen={x:i for i,x in enumerate(s)}
        st=[]
        used=[False]*123
        for i,c in enumerate(s):
            if used[ord(c)]:
                continue
            while st and c<st[-1] and lastSeen[st[-1]]>i:
                used[ord(st.pop())]=False
            st.append(c)
            used[ord(c)]=True
            
        return ''.join(st)
```

