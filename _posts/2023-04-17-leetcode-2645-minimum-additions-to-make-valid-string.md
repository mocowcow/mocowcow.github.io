--- 
layout      : single
title       : LeetCode 2645. Minimum Additions to Make Valid String
tags        : LeetCode Medium Array String Greedy TwoPointers
---
周賽341。

# 題目
輸入陣列word，你可以在任意位置插入字元"a", "b"或"c"任意次。求最少需要插入幾次才能使word**合法**。  

如果一個字串由任意個字串"abc"所組成，則稱其為**合法**。  

# 解法
反正只能插入不能刪除，就找那些位置需要插入就行。  

合法word必須是以"abc"模式循環而成，用一個索引變數i紀錄當前應該要找"abc"中哪個位置。  
遍歷word中每個字元，若是當前應該要找的，則代表需要插入，答案加1。  

記得要檢查最後的abc有沒有找完：  
> 例如word = "a"  
> 遍歷完word後，i=1  
> 應當補上"bc"  

時間複雜度O(N)。空間複雜度O(1)。  

```python
class Solution:
    def addMinimum(self, word: str) -> int:
        pat="abc"
        i=0
        ans=0
        
        for c in word:
            while pat[i]!=c:
                i=(i+1)%3
                ans+=1
            i=(i+1)%3

        # equals to 
        # ans+(3-i)%3
        while i>0:
            i=(i+1)%3
            ans+=1
            
        return ans
```

補一個搞笑方法，每次replace和count應該是O(N + M)，其中N為word長度，M為"abc"長度，也就是3。  
複雜度應該是O(N)。  

```python
class Solution:
    def addMinimum(self, word: str) -> int:
        ans=0
        
        word=word.replace("abc","")
        
        for pat in ["ab","ac","bc"]:
            ans+=word.count(pat)
            word=word.replace(pat,"")
            
        for pat in "abc":
            ans+=word.count(pat)*2
            word=word.replace(pat,"")
        
        return ans
```