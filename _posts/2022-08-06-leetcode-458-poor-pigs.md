--- 
layout      : single
title       : LeetCode 458. Poor Pigs
tags        : LeetCode Hard Math
---
每日題。這好像是微軟的毒老鼠面試題改版，難怪覺得眼熟眼熟。

# 題目
你有buckets桶水，其中正好有一桶有毒。你可以拿一些豬來試毒，找出到底哪桶水有毒。但是你只有minutesToTest分鐘可以測試。  

按照以下步驟給豬試毒：  
1. 選擇要試毒的豬
2. 選擇每頭豬要喝的水，豬會乖乖喝完，且不消耗時間  
3. 等後minutesToDie分鐘，在這段時間不可以繼續給其他豬試毒  
4. 經過minutesToDie分鐘後，有喝到毒的豬會立即死亡  
5. 重複以上過程，直到時間結束  

輸入buckets、minutesToDie和minutesToTest，求在給定的時間內找出有毒的水，**最少**需要幾頭豬。

# 解法
一開始想說用二分法，但是不符合時間限制，想一陣子沒什麼結論。  

後來看到滿精闢的[題解](https://leetcode.cn/problems/poor-pigs/solution/hua-jie-suan-fa-458-ke-lian-de-xiao-zhu-by-guanpen/)，他指出：若你有T次測試機會，則一頭豬可以包含T+1的訊息量。  

試想以下情況：  
> 8桶水 1次測試機會  

1次測試機會代表一頭豬可以包含2種訊息。將8桶水轉為2進位，分別為[000,001,..110,111]。由一號豬喝下所有第一位為10的水，二號豬喝所有第二位為0的水，三號豬喝所有第三位為0的水。  
如果一號豬死了，代表第一個位元為0。若最後一二號豬死亡，三號豬活著，則代表二進位為100的水有毒，也就是4號桶。  

> 8桶水 2次測試機會  

這次一頭豬可以包含3種訊息。將8桶水轉為3進位，變成[00,01,02,10,11,12,20,21]。測試分成兩階段：第一階段先讓所有豬喝對應位元為0的水，若死亡則代表對應位元為0。若順利存活，則繼續喝對應位元為1的水，死亡則代表位元為1，否則為2。  

最後結論，若有T次測試機會，則每頭豬有x=T+1種訊息量。而總訊息量為(X^豬數量)，所以我們只要增加豬的數量，直到總訊息量滿足buckets為止。  

```python
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        turn=minutesToTest//minutesToDie
        x=turn+1
        ans=0
        comb=1
        while comb<buckets:
            ans+=1
            comb*=x

        return ans
```
