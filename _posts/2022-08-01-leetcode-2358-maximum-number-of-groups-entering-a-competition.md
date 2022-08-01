--- 
layout      : single
title       : LeetCode 2358. Maximum Number of Groups Entering a Competition
tags        : LeetCode
---
周賽304。這題跟我電波比較合拍，應該算是很快就寫出來。  

# 題目
輸入正整數陣列grades，代表學生的成績。你要依照以下條件將學生分組：  
- 除最後一組外，第i組學生成績加總小於第i+1組學生成績加總  
- 除最後一組外，第i組的學生人數小於第i+1組的學生人數  

求最多可以分出幾組。

# 解法
每組一定要比前一組多1人，所以最佳的組人數分別是[1,2,3...]。  
而測資規定分數最低為1，假設分數為[3,3,3,3...]，第一組為[3]，第二組為[3,3]，可以保證下一組一定比前一組總分還多。  
那如果學生分數不同呢？優先將低分的學生分組，一樣可以保證符合規律。  

```python
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        ans=0
        remain=len(grades)
        size=1
        while remain>=size:
            ans+=1
            remain-=size
            size+=1
            
        return ans
```
