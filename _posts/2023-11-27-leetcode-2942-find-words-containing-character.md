---
layout      : single
title       : LeetCode 2942. Find Words Containing Character
tags        : LeetCode Easy Array String Simulation
---
雙周賽118。

## 題目

輸入字串陣列words和字元x。  

回傳一個**索引陣列**，代表著包含字元x的字串。  
索引陣列順序不限。  

## 解法

好像沒什麼好說的，就是枚舉第i個字串，如果找到字元x，就把i加入答案。  

時間複雜度O(NM)，其中N為words長度，M為max(len(words[i]))。  
空間複雜度O(1)。  

```python
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for i,w in enumerate(words):
            if x in w:
                ans.append(i)
                
        return ans
```

python一行版本。  

```python
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i,w in enumerate(words) if x in w]
```
