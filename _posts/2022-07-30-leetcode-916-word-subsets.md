--- 
layout      : single
title       : LeetCode 916. Word Subsets
tags        : LeetCode Medium Array String HashTable
---
每日題。其他語言都要寫一長串，就只有python寫起來特別簡單，而且還可以簡化到非常誇張的程度。  

# 題目
輸入字串陣列words1和words2。  
如果字串b中的每個字元都出現在字串a中，則稱b是a的子集合。例如：  
> "wrr"是"warrior"的子集合，但不是"world"的子集合  

對於words1中的某個字串a來說，若words2中的每個字串都是a的子集合，則稱a是**通用字串**。  
求word1中所有**通用字串**，可以依照任何順序回傳答案。  

# 解法
words1和words2長度都達1000，若使用暴力法逐一檢查，複雜度O(N^2)一定超時。  

假設以下情況：  
> words2 = ['aa','bb']  
> 若'aa'要是子集合，則字串必須有兩個'a'  
> 若'bb'要是子集合，則字串必須有兩個'b'  

每次要檢查的項目都是一樣的，我們可以先透過預處理，將檢查的最終條件計算好，這樣可以將檢查時間O(N)化簡為O(1)。  
維護雜湊表target，紀錄每個字元所需的次數。遍歷words2中的每個字串w，算出各自元出現次數，並以最大值更新target。  

例如：  
> words2 = ['aa','bb']  
> 合併為 2次a、2次b  
> words2 = ['abb','aaa','ccb']  
> 合併為 3次a、2次b、2次c

最後遍歷words1中的字串w，若target為w的子集合，則加入答案中，整體複雜度降低至(N+M)。

```python
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        target=Counter()
        for w in words2:
            t=Counter(w)
            for c in t:
                target[c]=max(target[c],t[c])
                
        ans=[]
        for w in words1:
            t=Counter(w)
            if all(t[c]>=target[c] for c in target):
                ans.append(w)
                
        return ans
```
