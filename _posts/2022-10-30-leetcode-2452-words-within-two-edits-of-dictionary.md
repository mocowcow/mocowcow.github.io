--- 
layout      : single
title       : LeetCode 2452. Words Within Two Edits of Dictionary
tags        : LeetCode Medium Array String
---
雙周賽90。本來想要將所有dictionary的字串以星號來代表可用的格式，結果發現測資很小，還是暴力法吧。  

# 題目
輸入兩個字串陣列queries和dictionary。每個陣列中的所有單字都由小寫英文字母組成，且長度相同。  

在一次**編輯**中，你可以在queries選則任一單字，並將其中的任一字母更改為其他字母。  

求queries有哪些單字可以在**兩次編輯以內**，和dictionary任意單字匹配成功。  

# 解法
雖然說是**編輯**，但不用真的去修改，只要找到當前查詢字串q和比對字串d有幾個字元不同，只要小於等於2個就匹配成功。  

查詢、字典和字串長度都是N=100，時間複雜度為O(N^3)。空間複雜度不計輸出陣列，為O(1)。  

```python
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        def ok(q,d):
            diff=0
            for a,b in zip(q,d):
                if a!=b:
                    if diff==2:return False
                    diff+=1
            return True
        
        ans=[]
        for q in queries:
            for d in dictionary:
                if ok(q,d):
                    ans.append(q)
                    break
                    
        return ans
```

python一行版本。  

```python
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        return [q for q in queries if any(sum(a!=b for a,b in zip(q,d))<=2 for d in dictionary)]
```
