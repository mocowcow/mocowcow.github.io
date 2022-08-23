--- 
layout      : single
title       : LeetCode 2383. Minimum Hours of Training to Win a Competition
tags        : LeetCode Easy Array Greedy
---
周賽307。這大概也是近來最難的Q1之一了，不僅題目又臭又長，參數也是有夠長，還長得很像，一不小心打錯字就再見WA。  

# 題目
你要參加比賽，初始精力為initialEnergy，而初始經驗為initialExperience。  
有兩個長度為n的整數陣列energy和experience，代表接下來n個對手的精力和能量。你必須擁有高於對方的精力和經驗才能獲勝。  

打敗第i個對手會增加和experience[i]的經驗，但會減少energy[i]的精力。  
在開始比賽之前，你可以透過訓練來增加精力或經驗，每訓練1小時，可以讓精力**或**經驗提升1。  

求打敗所有對手至少需要訓練幾個小時。  

# 解法
雖然說是在開打之前訓練，其實只要發現打不過的時後在補訓練而已。  
維護當前精力ene和經驗exp，並遍歷energy和experience。若在途中發現精力/經驗不足，則補到剛好打贏的程度。  

只要注意每場比完是**扣精力**、**加經驗**，然後變數名稱不要看錯而已。  

```python
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans=0
        ene=initialEnergy
        exp=initialExperience
        
        for x in energy:
            if ene<=x:
                train=x-ene+1
                ene+=train
                ans+=train
            ene-=x
        
        for x in experience:
            if exp<=x:
                train=x-exp+1
                exp+=train
                ans+=train
            exp+=x
        
        return ans
```
