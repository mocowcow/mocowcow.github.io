--- 
layout      : single
title       : LeetCode 1604. Alert Using Same Key-Card Three or More Times in a One Hour Period
tags        : LeetCode Medium Array String HashTable Sorting
---
模擬雙周賽36。這題目有夠臭長，還很麻煩，放在Q2還真有點讓人心態崩潰。

# 題目
LeetCode員工要使用門禁卡開門。每次使用門禁卡，系統都會儲存員工的姓名和使用時間。如果任何員工在一小時內使用門禁卡3次以上，系統就會發出警報。  
輸入字串陣列keyName和keyTime，其中[keyName[i], keyTime[i]]對應於一個員工的姓名和鑰匙卡在**一天內**的使用時間。  

使用時間以24小時制格式"HH:MM"表示，例如"23:51"和"09:49"。  
回傳觸發警報的員工姓名，並以字母升序排序。  

注意，"10:00"-"11:00"算在一小時內，而"22:51"-"23:52"**不算**在一小時內。  
"23:51"-"00:10"也不算在一小時內，因為系統只紀錄一天的使用情況。

# 解法
看了中文站的題目才發現兩邊描述不一樣，英文題目很容易讓人誤會，並把題目想得很複雜。  

首先寫一個輔助函數，把keyTime字串轉成以**分**計算的整數時間。  
還需要一個雜湊表d，一使用者名稱將使用時間分組。遍歷keyName，並將其對應到的時間轉換後，加入雜湊表d中。  

分組完成後，遍歷所有使用者，將其使用時間use排序，並從i=2開始，檢查use[i]和use[i-2]的時間差是否達到**60分鐘**，若是則將使用者加入答案中。  
最後將答案排序後回傳。

```python
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def t(s):
            h,m=map(int,s.split(':'))
            return h*60+m
        
        ans=[]
        d=defaultdict(list)
        for ppl,time in zip(keyName,keyTime):
            d[ppl].append(t(time))
        
        for ppl,use in d.items():
            use.sort()
            for i in range(2,len(use)):
                if use[i]-use[i-2]<=60:
                    ans.append(ppl)
                    break
        
        return sorted(ans)
```
