--- 
layout      : single
title       : LeetCode 2558. Take Gifts From the Richest Pile
tags        : LeetCode Easy Array Heap
---
周賽331。

# 題目
輸入整數陣列gifts，代表各個禮物堆的禮物個數。每秒鐘，你執行下列動作：  
- 找到一個數量最多的禮物堆  
- 如果有數個一樣最多的禮物堆，任選一個  
- 只留下原本數量的**平方根**，其餘拿走  

求執行k次動作後，總共剩下多少禮物。  

# 解法
其實可以暴力解，但寫起來沒比較快，就直接用heap了。  

因為動作要對最大值操作，所以使用max heap，每次取出最大值，將其開平方根後塞回去，最後回傳總和。  

時間複雜度O(k log N)。空間複雜度O(N)。  

```python
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h=[]
        for x in gifts:
            heappush(h,-x)
            
        for _ in range(k):
            x=-heappop(h)
            x=int(x**0.5)
            heappush(h,-x)

        return -sum(h)
```

如果在陣列上heapify可以將空間複雜度降低到O(1)。  
如果最大元素為1，開根號無法使其變小，可以檢查最大元素等於1時跳出迴圈。  

```python
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i]*=-1
        heapify(gifts)
            
        for _ in range(k):
            if gifts[0]==-1:
                break
            x=-heappop(gifts)
            x=int(x**0.5)
            heappush(gifts,-x)

        return -sum(gifts)
```