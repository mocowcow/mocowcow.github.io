--- 
layout      : single
title       : LeetCode 2562. Find the Array Concatenation Value
tags        : LeetCode Easy Array TwoPointers
---
周賽332。

# 題目
輸入整數陣列nums。  

**串接**指的是將兩個數字根據各個位數所合併起來。  
- 例如15和49的串接為1549  

**串接值**最初為0。重複以下動作直到nums為空：  
- 如果nums存在超過一個數，則將**第一個**和**最後一個**數字串接，將串接結果加入**串接值**中，並從nums中刪除  
- 如果只剩下一個數，直接將其加入**串接值**中，並刪除  

求nums的串接值。  

# 解法
這時候使用deque就很方便，可以直接從首尾取數字，也可以簡單的用len來檢查長度。  

按照描述，每次首尾兩數，先轉成字串後連接起來，在轉回整數加入答案。最後如果有落單的數記得加入答案。  

整數轉字串比較沒效率，時間複雜度O(N log max(nums))，其中N為nums長度。空間複雜度O(N)。  

```python
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans=0
        q=deque(nums)
        ans=0
        
        while len(q)>1:
            a=q.popleft()
            b=q.pop()
            ans+=int(str(a)+str(b))
            
        if q:
            ans+=q[0]
            
        return ans
```

如果直接在nums上操作，就不需要額外的空間去做deque。  

一樣每次取首尾兩個數字，只要算出後面那個數字有幾個位數，在前方數字補上相同數量的0就可以。  

時間複雜度O(N log max(nums))，其中N為nums長度。空間複雜度O(1)。  

```python
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans=0
        i=0
        j=len(nums)-1
        
        while i<j:
            x=nums[j]
            mul=1
            while x>0:
                mul*=10
                x//=10
            ans+=nums[i]*mul+nums[j]
            i+=1
            j-=1
            
        if i==j:
            ans+=nums[i]
            
        return ans
```