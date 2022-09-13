--- 
layout      : single
title       : LeetCode 1383. Maximum Performance of a Team
tags        : LeetCode
---
前幾天的每日題。有點像[2398. maximum number of robots within budget]({% post_url 2022-09-05-leetcode-2398-maximum-number-of-robots-within-budget %})的變形。  

# 題目
輸入兩個整數n和k，以及兩個長度n的整數陣列speed和efficiency。代表n個工程師，speed[i]和efficient[i]分別代表第i個工程師的速度和效率。  
你要選擇最多k個不同的工程師來組成一個表現最好的團隊。  
團隊的表現是工程師的**速度總和**乘以**團隊中最低效率者**的總和。  
求最好的表現值為多少。答案很大，需要模10^9+7後回傳。  

# 解法
同樣的，我們不在意選人的順序，那麼可以先將工程師們排序。  
團隊表現受限於最低效率者，因此我們依照效率來遞減排序，這樣每個最後加入的工程師都會是團隊中最沒效率那位。  
那如果最後加入那位，不僅效率差，速度也低，導致他加入後又馬上被踢出團隊，會不會計算出錯的答案？  
會，但是先前同樣的成員已經以更高的效率計算過表現，所以不會影響答案。  

作法確定之後實作就很簡單，我們只需要紀錄當前速度總和，以及將成員以速度排序，以便踢出速度最慢者，我選用min heap。  
開始遍歷排序好的工程師，先把他加入團隊，如果超出人數限制再踢掉最差的。然後以總速度和當前最低效率更新答案即可。  

答案回傳時需要模10^9+7，害我本來以為是dp題，結果是煙霧彈。排序複雜度O(N log N)，維護速度最小值成本O(N log k)，而k不超過N，整體時間複雜度O(N log N)，空間複雜度O(N)。

```python
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD=10**9+7
        eng=sorted(zip(efficiency,speed),reverse=True)
        h=[]
        sm=0
        ans=0
        
        for eff,spd in eng:
            heappush(h,spd)
            sm+=spd
            if len(h)>k:
                sm-=heappop(h)
            ans=max(ans,eff*sm)
            
        return ans%MOD
```
