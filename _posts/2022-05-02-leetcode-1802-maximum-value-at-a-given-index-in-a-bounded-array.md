--- 
layout      : single
title       : LeetCode 1802. Maximum Value at a Given Index in a Bounded Array
tags        : LeetCode Medium BinarySearch Math
---
二分搜學習計畫。這題超麻煩，根本就是在考數學公式。

# 題目
輸入整數n, index, maxSum，試著產生一個符合以下規則的陣列nums：  
- nums長度為n  
- nums中所有元素都是正整數  
- 每兩個相鄰元素的差最多為1  
- nums[index]必須最大化  

求nums[index]為多少。  

# 解法
照著題目描述，具體上就是要產生一個山型的陣列，先從nums[index]開始增加，再依序往旁邊擴散。  
可惜測資範圍非常大，用模擬的方式一定會超時，只好改用函數型二分搜，搜nums[index]的值要多少才合法。  

nums中元素最小是1，下界定為1。假設長度為1，則峰值等於nums[index]，故上界定為maxSum，開始做二分搜。  
如果可以無法以nums[index]=mid成功建造陣列，更新上界為mid-1；否則更新下界為mid。  
考慮lo=1, hi=2的情形，若取左中位數mid=1，若更新lo為mid會造成死循環，要改成取右中位數。  

重點是這個判斷的函數canDo(peak)很難搞，nunms[index]為peak，而index+1開始由peak向右遞減，index-1由peak向左遞減，且最少要停在1。  
左右兩邊遞減的動作其實是等價的，可以再寫一個函數lvl(size,h)來減少重複，代表建造一個長度size且由h開始遞減的陣列，其總和為多少。  
最佳狀況當然是size和h相等，例如size=h=3，就是[3,2,1]。那size=3, h=5呢？是[5,4,3]，可以觀察出是由[5,4,3,2,1]扣掉[2,1]。可以總結出若size比h小的話，直接以[h..1]扣掉[h-size..1]，這時a\*(a+1)//2公式又派上用場。  
那麼size大於等於h的情況，一樣會使用到[h..1]的等差數列，但是要補上(size-h)個1。  
最後回到canDo函數裡面，檢查左右遞減陣列+peak值總和是否小於maxSum即可。

```python
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def lvl(size,h):
            if size<h:
                return h*(h+1)//2-(h-size)*(h-size+1)//2
            ans=h*(h+1)//2
            if size>h:
                ans+=size-h
            return ans

        def canDo(peak):
            use=peak+lvl(index,peak-1)+lvl(n-index-1,peak-1)
            return use<=maxSum
        
        lo=1
        hi=maxSum
        while lo<hi:
            mid=(lo+hi+1)//2
            if not canDo(mid):
                hi=mid-1
            else:
                lo=mid
                
        return lo
```
