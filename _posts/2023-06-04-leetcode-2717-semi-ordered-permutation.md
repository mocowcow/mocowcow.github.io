--- 
layout      : single
title       : LeetCode 2717. Semi-Ordered Permutation
tags        : LeetCode Medium Array Simulation
---
周賽348。其實這應該才要放到Q1。  

# 題目
輸入整數陣列nums，是整數1\~n的排列。  

如果某個排列方式，第一個字元素是1，且最後一個元素是n，則稱為**半有序**。  
你可以執行以下操作任意次使得nums符合**半有序**。  
- 選擇nums中兩個相鄰的元素，並將其交換  

求使得nums**半有序**所需的**最小操作次數**。  

# 解法
找到1和n的位置，如果分別不在頭尾的話，就要將其依序換位回去。  

直接使用暴力法模擬換位的過程。  
就算測資很大也可以透過模擬來解決，畢竟至少要遍歷nums才能找到1和n的位置，但竟然允許遍歷一次，那麼多交換兩數、多遍歷兩次也是沒什麼關係。  
而且模擬的好處在於不用考慮1和n的相對位置，不然有時候移動1的過程中會連帶影響到n的位置。  

如果1在不為0的索引i，則必須往左換位i次。加到答案中，把它搬到正確的位置上。  
又如果n在不為n-1的索引i，則必須往右換位n-1-i次，也加到答案中。  

時間複雜度O(n)。  
空間複雜度O(1)。  

```python
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        
        if nums[0]!=1:
            i=nums.index(1)
            ans+=i
            nums.pop(i)
            nums=[1]+nums
            
        if nums[-1]!=N:
            i=nums.index(N)
            ans+=N-1-i
        
        return ans
```

如果不模擬位移，則要分類討論，考慮1和n的初始相對位置。  
假設1在n的左邊，位移不互相影響，例如：  
> ..1.n.    
> 把1移到左邊，操作2次  
> 1...n.
> 把n移到右邊，操作1次  
> 1....n  

否則移動其中一個的時候，會讓另一個脫離原始的位置，例如：  
> ..n.1.  
> 把1移到左邊，操作4次  
> 1..n..  
> 這時候n也往右偏了一步  
> 把n移到右邊，操作2次  
> 1....n  

時間複雜度O(n)。  
空間複雜度O(1)。  

```python
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        
        i=nums.index(1)
        j=nums.index(N)
        
        if i!=0:
            ans+=i
            
        if j!=N-1:
            if i>j:
                ans-=1
            ans+=N-1-j
        
        return ans
```