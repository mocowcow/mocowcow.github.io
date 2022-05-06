--- 
layout      : single
title       : LeetCode 2104. Sum of Subarray Ranges
tags        : LeetCode Medium Array Stack MonotonicStack
---
[2262. total appeal of a string]({% post_url 2022-05-01-leetcode-2262-total-appeal-of-a-string %})的類似題，計算每個位置的貢獻次數。

# 題目
輸入陣列nums。  
**子陣列距離**指的是子陣列中最大和最小元素的差，求nums所有子陣列的**距離**總和。

# 解法
最原始的暴力法就是生成所有子陣列，然後分別找最大最小值，時間O(N^3)，一定會超時。  
優化一下，因為子陣列nums[i:j]由nums[i:j-1]生成，故可以重複利用其最大最小值，降低到O(N^2)。  

```python
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        for i in range(N):
            mx=-math.inf
            mn=math.inf
            for j in range(i,N):
                mx=max(mx,nums[j])
                mn=min(mn,nums[j])
                ans+=mx-mn
            
        return ans
```

follow up要求用O(N)解法，這就直升hard難度了。  

先將問題解析清楚，長度為n的陣列nums，會產生n*(n+1)/2個子陣列，可以拆解成n*(n+1)/2個最大值和最小值，最大值加總-最小值加總就是總距離。  
問題簡化成要怎麼計算那些數字做為最大/最小值出現幾次？既然要找最大/最小值，可以考慮單調堆疊。  

把最大/最小分兩次找，先找最大值。  
維護單調遞減堆疊st，遍歷nums中每個數字n及索引right，當n大於st頂端元素，代表該元素作為最大值的地位到此為止，接著清算他出現在多少子陣列中：  
彈出的元素索引記為mid，而右方還有(right-mid)個元素、左方有(mid-left)個元素可以搭配形成子陣列。左邊界left又是什麼鬼？因為st是遞減的，所以在找st頂端元素就是左方第一個比n大的位置，若st為空則手動設為-1。  
算出左方有L個元素，右方有R個元素，可以算出以mid為最大值的子陣列個數為L*R個，再乘上n，就是這個元素作為最大值的貢獻值。  
nums尾端要加入inf，才可以保證所有數字都被處理過。  

稍微解釋一下為什麼L*R可以得到子陣列個數：  
> nums = [1,2,**5**,3]  
> 計算數字5作為最大值出現在多少子陣列中  
> 左方有2個可用元素，右方有1個可用元素  
> 左方可以選擇{[1,2],[2],[]}，右方可以選擇{[3],[]}  
> 故有3*2個子陣列  
> [1,2,5,3], [1,2,5], [2,5,3], [2,5], [5,3], [5]

最小值計算同理，只是改成單調遞增堆疊，然後尾端加入的數字改成-inf，確保所有值有被處理到。

```python
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans=0
        #find mx
        st=[]
        for right,n in enumerate(nums+[math.inf]):
            while st and n>nums[st[-1]]:
                mid=st.pop()
                left=st[-1] if st else -1
                ans+=(mid-left)*(right-mid)*nums[mid]
            st.append(right)
            
        #find mn
        st=[]
        for right,n in enumerate(nums+[-math.inf]):
            while st and n<nums[st[-1]]:
                mid=st.pop()
                left=st[-1] if st else -1
                ans-=(mid-left)*(right-mid)*nums[mid]
            st.append(right)
            
        return ans
```

