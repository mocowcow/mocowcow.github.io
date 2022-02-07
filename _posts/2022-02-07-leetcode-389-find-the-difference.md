---
layout      : single
title       : LeetCode 389. Find the Difference
tags 		: LeetCode Easy String HashTable Sorting BitManipulation
---
天氣回暖，凍僵的腦袋總算舒服一些。

# 題目
輸入一個小寫純英文字串s及t，t比s多一個字元，並打亂順序，回傳t多出來的那個字元。

# 解法
提供四個解法，由淺入深。  
排序可以保證字母依序出現。兩個字串排序後依序比對，不相同時就是答案。

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]    
```

但是排序需要nlogn，使用雜湊表可以在線性時間內完成。
將s的所有元素計數-1，t的所有元素計數+1，最後遍歷table，值為-1就是答案。

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ctr=Counter()
        for c in s:
            ctr[c]+=1
        for c in t:
            ctr[c]-=1
        for k,v in ctr.items():
            if v==-1:
                return k
```

直接將字元換成ascii也可以，改成先加入t，再扣s，將差值轉回字元回傳。

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff=0
        for c in t:
            diff+=ord(c)
        for c in s:
            diff-=ord(c)
            
        return chr(diff)    
```

最後是利用XOR兩兩相消的特性，上個方法改成以s和t每個字元做XOR。  
因為每個字母出現次數一定是2n，除了新增的那個，所以只會剩下答案的ascii。

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans=0
        for c in s+t:
            ans^=ord(c)
            
        return chr(ans)
```