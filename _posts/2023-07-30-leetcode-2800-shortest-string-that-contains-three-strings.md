--- 
layout      : single
title       : LeetCode 2800. Shortest String That Contains Three Strings
tags        : LeetCode Medium String
---
周賽356。有點麻煩的字串題，不少人都吃到WA。  

## 題目

輸入三個字串a,b和c，你的目標是找到一個**最短**的字串，且這三個字串都是其**子字串**。  
如果有多種答案，則回傳**字典順序最小**者。  

## 解法

想來想去半天，好想沒什麼比較有效率的方法，好像只能窮舉所有排列方式。  

反正只有三個字串，只有六種順序可以將字串合併：  

1. abc  
2. acb  
3. bac  
4. bca  
5. cab  
6. cba  

假設字串s和t合併，為了使長度盡可能短，所以對t由大到小檢查前綴是否是s的後綴。如果符合，則將t剩餘的後綴加入s。  
例如：  
> s = "abc", t = "bca"  
> "bca"不是"abc"的後綴，跳過  
> "bc"是"abc"的後綴，把t剩下的後綴"a"加入s後面
> 合併後的s = "abc**a**"  

但還有一個特判情況，就是t已經被s包含，根本不需要合併，例如：  
> s = "abbbba", t = "bbbb"  

時間複雜度O(N^2)，其中N為abc三者中最大長度。  
空間複雜度O(N)。  

```python
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        
        def merge(abc):
            res=abc[0]
            for s in abc[1:]:
                if s in res:
                    continue
                for size in range(min(len(res),len(s)),-1,-1):
                    if res[len(res)-size:]==s[:size]:
                        res+=s[size:]
                        break
            return res
        
        ss=[]
        for x in permutations([a,b,c]):
            ss.append(merge(x))
        
        ans=ss[0]
        for s in ss:
            if len(s)<len(ans) or (len(s)==len(ans) and s<ans):
                ans=s
                
        return ans
```
