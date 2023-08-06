---
layout      : single
title       : LeetCode 2808. Minimum Seconds to Equalize a Circular Array
tags        : LeetCode Medium Array HashTable Simulation
---
雙周賽110。剛開始看錯題目錯WA一次，然後看錯測試結果又WA一次，然後想法錯誤又WA一次。好在最後有想出來。  

## 題目

輸入長度n的整數陣列nums。  

每一秒，你可以執行以下操作：  

- 對於所有介於[0, n-1]的索引i，將nums[i]替換成nums[i]、nums[(i-1+n)%n]或是nums[(i+1)%n]  

注意：這些替換操作是在同一個瞬間完成。  

求使得nums所有元素相同，**最少**需要操作幾次。  

## 解法

操作的內容是：把nums[i]換成他左邊或是右邊的元素，不是把他增減1。  
照這個錯誤邏輯正好可以得到例題的正確答案，有夠精心設計。  

看清楚題目後，我以為**把所有元素變成眾數**最省時間，直到這個測資出現：  
> nums = [8,8,9,10,9]  
> 答案1  

8和9的出現次數一樣，卻得出不同結果。  
我才發現，乾脆枚舉所有數字當作目標，看看換成哪個數字的時間最少。  

繼續看同樣例子：  
> nums = [8,8,9,10,9]  
> 假設要把所有元素變成9，就從每個9往兩邊擴散  
> 第一秒[**9**,**9**,9,**9**,9]  
> 若是要變成8，則從每個8擴散  
> 第一秒[8,8,**8**,10,**8**]  
> 第二秒[8,8,,8,**8**,8]  

可以發現，兩個目標元素中間若夾著gap個其他元素，則需要(gap+1)/2秒才能把他們全都變一樣。  
因此將所有依照元素將索引分組，求出每組的**最大時間**，以此更新時間**最小值**。  
注意：陣列是循環的，要記得處理第一個索引和最後一個索引之間包夾的元素。  

實際上每個元素只會被處理到兩次，時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        N=len(nums)
        d=defaultdict(list)
        for i,x in enumerate(nums):
            d[x].append(i)
            
        ans=inf
        for li in d.values():
            gap=N-1-li[-1]+li[0]
            time=(gap+1)//2
            for a,b in pairwise(li):
                gap=b-a-1
                time=max(time,(gap+1)//2)
            ans=min(ans,time)
            
        return ans
```

有個小技巧，直接將陣列的索引重複兩次，就可以直接包含循環範圍。  
而a,b之間共有(b-a+1)個元素，之後還要向上取整，可以簡化成(b-a)/2。  

```python
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        d=defaultdict(list)
        for i,x in enumerate(nums*2):
            d[x].append(i)
            
        ans=inf
        for li in d.values():
            mx=max((b-a)//2 for a,b in pairwise(li))
            ans=min(ans,mx)
            
        return anss
```
