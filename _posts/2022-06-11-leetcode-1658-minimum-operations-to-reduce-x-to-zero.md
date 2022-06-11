--- 
layout      : single
title       : LeetCode 1658. Minimum Operations to Reduce X to Zero
tags        : LeetCode Medium Array SlidingWindow
---
每日題。今天這題還真有點難度，腦子稍微轉一下就會變簡單很多。  

# 題目
輸入整數陣列nums和整數x。在每次操作中，你可以從數nums中刪除最左邊或最右邊的元素，然後從x中減去該值。  
求最少需要幾次刪除可以使x成為0，若不可能則回傳-1。  

# 解法
剛開始想說左右各維護一個deque，先把左邊塞滿，然後試著減少左邊，增加右邊。結果這條件太麻煩，不好處理。  
看了提示才想通，與其用左右兩個子陣列達到總和x，不如藉由刪除中間的子陣列使左右只剩下x。  

試想把nums拆成左中右三個部分，而左右的目標總和為x。那麼先計算出nums的總和sm，中間的部分總和應為sm-x，記為remove。  
現在問題簡化成找總合為remove的最常子陣列了，使用滑動窗口nums中的每個元素n依序加入，若窗口總和window大於remove，則彈出左側元素。邊界調整後，若總合正好為remove，則以當前窗口長度更新最大子陣列長度mx。  
最後檢查若mx為0，則代表不可能達成，回傳-1；否則回傳nums長度扣掉mx，即為左右兩方刪除的元素數量。  

```python
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sm=sum(nums)
        if sm<x:
            return -1
        if sm==x:
            return len(nums)
        
        q=deque()
        remove=sm-x
        window=0
        mx=0
        for n in nums:
            q.append(n)
            window+=n
            while window>remove:
                window-=q.popleft()
            if window==remove:
                mx=max(mx,len(q))
                
        return -1 if mx==0 else len(nums)-mx
```

不用deque，改成雙指標寫法。  

```python
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sm=sum(nums)
        if sm<x:
            return -1
        if sm==x:
            return len(nums)
        
        remove=sm-x
        l=0
        window=0
        mx=0
        for r,n in enumerate(nums):
            window+=n
            while window>remove:
                window-=nums[l]
                l+=1
            if window==remove:
                mx=max(mx,r-l+1)
                
        return -1 if mx==0 else len(nums)-mx
```