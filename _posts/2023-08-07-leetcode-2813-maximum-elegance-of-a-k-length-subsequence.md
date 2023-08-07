---
layout      : single
title       : LeetCode 2813. Maximum Elegance of a K-Length Subsequence
tags        : LeetCode Hard Array Sorting Greedy Stack HashTable
---
周賽357。完全沒碰過這類型的題目，最近兩次周賽壓軸有夠的難。  

## 題目

輸入長度n的二維整數陣列items，還有整數k。  

items[i] = [profit<sub>i</sub>, category<sub>i</sub>]，分別代表第i個物品的利潤和種類。  

定義item子序列的**優雅度**為total_profit + distinct_categories<sup>2</sup>。  
其中total_profit是子序列中的利潤總和，而distinct_categories是不同種類的個數。  

你的目標是找到大小為k的子序列的**最大優雅度**。  
回傳正好為k的子序列的最大優雅度。  

## 解法

itesm的選擇順序不影響答案，總之先按照profit排個序。  
依倒序來看，會發現一個特性：相同種類中的物品，利潤較高者會先處理到。  

最初先選擇k個利潤最大的物品，之後再考慮要不要拿新的物品來替換已有的。  
因為按profit倒序處理，想要優雅度上升的話，絕對不可能是單靠profit本身，只能試圖讓不同的種類增加。  

當前物品items[i]利潤為p，種類為c，考慮選或不選，分類討論以下情況：

- 如果c出現過，因為profit倒序的關係，絕對不可能使優雅度上升，不選  
- 如果c沒出現過，他有可能使的不同種類增加，再分以下情況：  
    1. 已選的k個物品中，有某種類重複出現，則丟掉profit最小的，加入當前物品  
    2. 沒有種類重複的物品，不管丟哪個都無法讓不同種類增加，不選  

維護變數tot作為profit的加總、集合distinct來記錄出現過的種類，還有一個堆疊extra保存重複出現的種類的profit。  
只有當物品種類c不存在distinct中，且extra中有重複物品可以丟棄時才加入當前物品。  

按照這個方式處理，tot的部分會降低，但distinct會上升。我們沒辦法確定何時出現最高峰，所以再每次加入新物品後都要更新一下答案。  

瓶頸在於排序，時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(reverse=True)
        distinct=set()
        tot=0
        extra=[]
        ans=0
        for p,c in items:
            if k>0: # 不夠k個
                k-=1
                tot+=p
                if c not in distinct: # 第一次出現
                    distinct.add(c)
                else: # 重複的
                    extra.append(p)
            else: # 足夠k個，找重複的丟
                if c not in distinct and extra: # c沒出現過，且有重複的可以丟
                    distinct.add(c)
                    tot+=p
                    tot-=extra.pop()
            
            ans=max(ans,tot+len(distinct)**2)
            
        return ans
```
