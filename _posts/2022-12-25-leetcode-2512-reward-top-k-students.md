--- 
layout      : single
title       : LeetCode 2512. Reward Top K Students
tags        : LeetCode Medium Array String HashTable Sorting
---
雙周賽94。又臭又長題，好在有沉住氣沒噴BUG。  

# 題目
輸入兩個字串陣列positive_feedback和negative_feedback，分別表示正面和負面的評語。注意，評語**不可能**同時具有正面和負面的涵義。  

每個學生初始都為0分，每收到正面評語會+3分；負面評語則-1分。  

共有n個評語報告，由字串陣列report和整數陣列student_id所組成。其中student_id[i]代表第i個學生的ID，而report[i]代表第i個學生的評語。每個學生的ID都是**不同的**。  

輸入整數k，求分數前k高的學生ID，並依其分數**非遞增**排序。若有多個學生分數相同，則以ID較小者為優先。  

# 解法
正評+3分，負評-1分，先各建立集合以備O(1)查詢。  
再來寫一個score函數，傳入字串並依照評價回傳得分。  

遍歷所有學生及其評價，將得分和ID綁定後排序，取前k個就結束了。  

參數有夠多，時間複雜度超難寫，總共是O((p+n+N) + N log N)，其中p為正評個數，n為負評個數，N為學生個數。  
空間複雜度O(p+n+N)。

```python
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos=set(positive_feedback)
        neg=set(negative_feedback)
        
        def score(rep):
            cnt=0
            for x in rep.split():
                if x in pos:
                    cnt+=3
                elif x in neg:
                    cnt-=1
            return cnt
        
        stu=[[score(rep),id]  for rep,id in zip(report,student_id)]      
        stu.sort(key=lambda x:(-x[0],x[1]))
        
        return [x[1] for x in stu[:k]]
```
