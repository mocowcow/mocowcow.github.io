--- 
layout      : single
title       : LeetCode 2788. Split Strings by Separator
tags        : LeetCode Easy String Simulation
---
周賽355。

# 題目
輸入字串陣列words，還有一個字元separator，用separator將每個字串分割。  

回傳所有分割後的**非空**字串。  

注意：  
- separator用於分割後，並不會存留在分割出的新字串  
- 一個字串可能分割出兩個以上的新字串  
- 答案中的字串必須維持原本的相對順序  

# 解法
內建函數應用題。  

遍歷所有字串w，以separator分割，將不為空的結果加入答案即可。  

時間複雜度O(L)，其中L為sum(words[i].length)。  
空間複雜度O(N)。  

```python
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans=[]
        for w in words:
            for x in w.split(separator):
                if len(x)>0:
                    ans.append(x)
                    
        return ans
```
