--- 
layout      : single
title       : LeetCode 2672. Number of Adjacent Elements With the Same Color
tags        : LeetCode Medium Array Simulation
---
周賽344。沒看懂題目卡死了，總感覺我常常在沒有hard題的周賽超級大爆死。  

# 題目
有個長度n的陣列nums。最初所有元素都是**未上色的**，以0表示。  

輸入二維陣列queries，其中queries[i] = [index<sub>i</sub>, color<sub>i</sub>]。  
對於每次查詢，你必須將nums位於index<sub>i</sub>的顏色改成color<sub>i</sub>。

回傳長度與qeuries相同的的陣列answer，其中answer[i]代表執行完第i次查詢**之後**，有多少相鄰元素的顏色相同。  

更正式的說，answer[i]為執行第i次查詢後，對於所有0<=j<N-1的索引j，滿足nums[j]==nums[j+1]且nums[j]!=0的個數。  

# 解法
個人覺得這個**相鄰同色**的定義非常爛，而且範例沒有講清楚。  
若有x個索引顏色都相同，則貢獻了x-1個**相同**。例如[1,1,0]有1個相同。  
而且不限於一種顏色，不同顏色構成的**相同**都要列入計算。例如[7,7,7,5,5]有2+1=3個相同。  

相同數same初始為0。  
因為i是根據i+1的顏色來判斷是否**相同**，所以在改變nums[i]的顏色之後，實際上只會影響到i和i-1兩個位置。  
- 若鄰居原本同色，**改成不同色**會減少same 
- 若鄰居原本不同色，**改成同色**會增加same  

而原本未上色的0不會貢獻任何相同數，所以在nums[i]從0改成其他色不可能使same減少。  

時間複雜度O(n+Q)，其中Q為查詢次數。  
空間複雜度O(n)。  

```python
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        same=0
        nums=[0]*n
        ans=[]
        
        for i,color in queries:
            # if nums[i] already colored
            # we should check adj if any same color will be broken
            if nums[i]!=0:
                if i+1<n and nums[i]==nums[i+1]:
                    same-=1
                if i>0 and nums[i]==nums[i-1]:
                    same-=1
                    
            # after color changed
            # check adj if any new same color 
            nums[i]=color
            if i+1<n and nums[i]==nums[i+1]:
                same+=1
            if i>0 and nums[i]==nums[i-1]:
                same+=1
            
            ans.append(same)
            
        return ans
```
