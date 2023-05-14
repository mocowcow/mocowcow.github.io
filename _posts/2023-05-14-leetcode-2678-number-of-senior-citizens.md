--- 
layout      : single
title       : LeetCode 2678. Number of Senior Citizens
tags        : LeetCode Easy Array String
---
雙周賽104。

# 題目
輸入字串陣列details。  
details中的每個字串皆為15，代表著每個乘客的個人資料。  
- 前10個字元是電話號碼  
- 下一個字元是性別  
- 再下兩個字元是年齡  
- 最後兩個字元是座位號碼  

求有多少乘客的年齡**嚴格大於60歲**。  

# 解法
[0,9]是電話，[10]是性別[11,12]是年齡。  
直接取[11,12]的子字串轉成整數，若大於60則答案加1。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=0
        
        for s in details:
            age=int(s[11:13])
            if age>60:
                ans+=1
        
        return ans
```

一行版本。  

```python
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(s[11:13])>60 for s in details)
```