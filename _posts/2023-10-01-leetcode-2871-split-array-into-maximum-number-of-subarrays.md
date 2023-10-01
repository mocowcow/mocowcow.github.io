---
layout      : single
title       : LeetCode 2871. Split Array Into Maximum Number of Subarrays
tags        : LeetCode Medium Array BitManipulation Greedy
---
雙周賽114。

## 題目

輸入非負整數陣列nums。  

定義子陣列nums[l..r]的分數為nums[l] AND nums[l+1] AND ... AND nums[r]的結果，其中AND為位元或運算，且l <= r。  

試著將陣列分割成一或多個子陣列，使其符合以下條件：  

- 陣列中**每個**元素**正好**屬於一個子陣列  
- 所有子陣列的分數總和**最小化**  

求滿足以上條件的分割方式，**最多**可以分割多少子陣列。  

## 解法

先決條件是**分數總和最小**化。  
基於AND運算的特性，值只增不減，所以全部元素做AND後就會得到分數最小值tot。  

如果tot不為0，任何分割出的子陣列分數也不可能為0，都會使得總分增加。  
因此不分割，答案為1。  

如果tot等於0，為使得子陣列數量多，我們再來試著將nums分割成數個分數為0的子陣列。  
一邊遍歷nums，一邊維護AND運算的結果res。只要res變成0，答案加1，然後分割出新的子陣列。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:        
        tot=nums[0]
        for x in nums:
            tot&=x
            
        if tot!=0:
            return 1
        
        ans=0
        res=nums[0]
        for x in nums:
            if res==-1:
                res=x
                
            res&=x
            if res==0:
                ans+=1
                res=-1
                
        return ans
```

特判tot結果很麻煩，但如果不特判的話，他永遠組不出res=0的子陣列，也就是說會把答案1算錯0。  
其實可以不管他，直接在答案和1之前取最大值就好。  

然後在分割子陣列時，為了處理子陣列中第一個元素。剛才把res標記成-1，表示res需要初始化。  
數字x在二補數表示中，是abs(x)的二進位表示取反後再加1，也就是0b..0001取反後加1，等於0b..1111，全部位元都是1。  
-1的二進位表示全都是1，跟任何數做AND，都會得到該數字。  

```python
class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:        
        ans=0
        res=-1
        for x in nums:
            res&=x
            if res==0:
                ans+=1
                res=-1
                
        return max(ans,1)
```
