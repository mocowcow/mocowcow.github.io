---
layout      : single
title       : LeetCode 2212. Maximum Points in an Archery Competition
tags 		: LeetCode Medium Backtracking 
---
周賽285。看到N=12馬上確定是回溯法，只是沒注意要把所有箭矢用光，粗心吃了個WA。

# 題目
Alice和Bob在比賽射箭。箭靶有12個區域，由編號0~11。  
每個區域由射中箭多者得到與區域編號相同分數，若箭數相同則不給分。例：  
> 在區域11，Alice和Bob各射中2箭，沒人得分  
> 在區域11，Alice射中0箭，Bob射中2箭，由Bob獲得11分  

每人各有numArrows支箭矢，而陣列aliceArrows代表Alice在各區域分別射中幾發。求Bob要如何射才能將得分最大化。  
若有多種方法可以獲得最高分，回傳其中一種即可。

# 解法
題目很長，但很容易理解。  
Bob的最佳策略沒辦法簡單計算出來，但是可以窮舉所有可能性：對每個區域射或不射兩種選擇，共2^12種組合。  
但區域0射了也沒分，其實可以不管他，簡化為2^11。而每個區域決定要射的話，一定要比Alice多一發，才能得到分。  

整理出這些基本決策，就可以開始撰寫回溯函數。  
定義bt(i,remain,score,use)為：目前在第i區域，剩下remain支箭矢可用，已經得到score分，且use陣列為先前在各區域射過的箭矢數。  
因為最後一個區域為11，所以將i=12定為終止條件，在此檢查是否更新最高分。更新最佳解時，**若有剩餘箭矢通通射到0去**。  
剩下決定射不射的部分了，不射的話就是使用0箭，快進到下一區；要射比Alice多一箭就好，再多也是浪費。

```python
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        ans=None
        mx=0
        
        def bt(i,remain,score,use):
            nonlocal ans,mx
            if remain<0:
                return 
            if i==12:
                if score>mx:
                    mx=score
                    ans=use[:]
                    if remain>0:
                        ans[0]=remain
            else:
                #skip
                use.append(0)
                bt(i+1,remain,score,use)
                use.pop()
                #shoot
                use.append(aliceArrows[i]+1)
                bt(i+1,remain-aliceArrows[i]-1,score+i,use)
                use.pop()
                
        bt(1,numArrows,0,[0])
        
        return ans
```

