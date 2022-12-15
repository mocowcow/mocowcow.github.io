--- 
layout      : single
title       : LeetCode 2496. Maximum Value of a String in an Array
tags        : LeetCode Easy Array String
---
雙周賽93。距離上次遇到例外處理應該超過半年了，這種小技巧真方便。  

# 題目
一個**英數**字串的值應為：  
- 若只包含數字，則等於其十進位所代表的數  
- 否則為字串長度  

輸入英數字串陣列strs，求其中的**最大值**。  

# 解法
遍歷strs中所有字串s，必須先判斷其中是否只含數字，才能決定要轉整數或是長度來計算**值**。  

最基本的方法就是遍歷字串，若其中出現非數字字元，則代表非純數字串。  
或是使用python字串內建isdigit方法，直接判斷是否為純數。  

時間複雜度為O(NM)，其中N為strs長度，M為strs[i]長度。不需額外空間，空間複雜度O(1)。  

```python
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans=0
        
        for s in strs:
            ok=True
            for c in s:
                if c<"0" or c>"9":
                    ok=False
                    break
            if ok: # or s.isdigit()
                ans=max(ans,int(s))
            else:
                ans=max(ans,len(s))
                
        return ans
```

另外比較偷雞的做法是利用錯誤處理，直接試著把字串轉成整數，如果出錯就代表包含其他字元，這時再來改成以長度判斷即可。  

```python
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans=0
        
        for c in strs:
            try:
                ans=max(ans,int(c))
            except:
                ans=max(ans,len(c))
                
        return ans
```

最後附上python一行版。  

```python
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(s) if s.isdigit() else len(s) for s in strs)
```