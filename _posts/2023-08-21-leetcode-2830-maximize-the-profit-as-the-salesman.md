---
layout      : single
title       : LeetCode 2830. Maximize the Profit as the Salesman
tags        : LeetCode Medium Array Sorting DP
---
周賽359。印象中哩扣上有兩題相似題，其中一個幾乎完全一樣，但是這次有四千人通過，也太扯。  
相似題[2008. maximum earnings from taxi]({% post_url 2022-03-24-leetcode-2008-maximum-earnings-from-taxi %})，當初才一千人通過。  

## 題目

輸入整數n，代表有n個房子排成一列，編號分別為0到n-1。  

另外，還有一個二維陣列offers，其中offers[i] = [start<sub>i</sub>, end<sub>i</sub>, gold<sub>i</sub>]，代表第i個買家願意以gold<sub>i</sub>的價格購買區間[start<sub>i</sub>, end<sub>i</sub>]的所有房子。  

身為一個房仲，目標當然是利潤最大化。  

求**最多**可以賺到多少錢。  

注意：一棟房子只能被賣給一個人，但也可以沒賣出去。  

## 解法

先講講比賽中的做法。  

將offers由右端點排序。之後從左到右遍歷時，能夠保證先前處理過的所有offer都不會超過當前的右邊界，我們可以決定要**保留**哪些部分來搭配當前的offer。  

定義dp[i]：出售區間[0, i]的房屋可獲得的最大利潤。  
轉移方程式：dp[i]=max(dp[i-1], prev+p)。當前區間為[s,e]，其中prev是dp[s-1]，而p是當前價格。  
base case：當i<0，是無效的狀態，沒有房子，利潤0。  

注意在遍歷offers的過程中，並不保證右區間都是連續的，所以要維護變數last來紀錄上一個區間的位置，並更新dp[i]。  
例如n = 3, offers = [[0,0,1], [2,2,1]]  
> i=0，出售offers[0]，得到dp[0] = dp[-1]+1 = 1  
> i=1，沒有offer的右邊界是1，延續上一個結果，dp[1] = dp[0]  
> i=2，出售offers[1]，得到dp[2] = dp[1]+1 = 2

時間複雜度O(n + M log M)，其中M為offers長度。  
空間複雜度O(n)。  

```python
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=itemgetter(1))
        dp=[0]*n
        last=0
        for s,e,p in offers:
            while last<e:
                dp[last+1]=dp[last]
                last+=1
            prev=0 if s==0 else dp[s-1]
            dp[e]=max(dp[e],prev+p)
            
        while last+1<n:
            dp[last+1]=dp[last]
            last+=1
            
        return dp[-1]
```

n的範圍很小，可以用類似bucket sort的方式將offers分類，以空間換取排序的時間。  

時間複雜度O(n + M)。  
空間複雜度O(n + M)。  

```python
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        d=[[] for _ in range(n)]
        for s,e,p in offers:
            d[e].append([s,p])
            
        dp=[0]*n
        for i in range(n):
            dp[i]=dp[i-1]
            for s,p in d[i]:
                prev=0 if s==0 else dp[s-1]
                dp[i]=max(dp[i],prev+p)
                
        return dp[-1]
```
