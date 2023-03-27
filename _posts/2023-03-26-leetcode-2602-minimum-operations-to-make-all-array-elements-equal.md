--- 
layout      : single
title       : LeetCode 2602. Minimum Operations to Make All Array Elements Equal
tags        : LeetCode Medium Array Sorting PrefixSum BinarySearch
---
周賽338。

# 題目
輸入正整數陣列nums。  

另外還有長度為m的整數陣列queries。對於第i次查詢，你要使得nums中所有元素都等於queries[i]。  
你可以執行以下動作任意次：  
- 將nums任意元素**增加**或**減少**1  

回傳長度m的陣列answer，其中answer[i]是第i次查詢的**最小操作次數**。  

注意：每次查詢結束後，nums會恢復成初始值。  

# 解法
若查詢值為q，元素為x，則需要的動作次數為abs(q-x)。  

以範例1為例：  
> nums = [3,1,6,8]  
> 第一次查詢q=1  
> 所有元素都大等於1，總動作次數為sum(nums)-q\*N=14  
> 第二次查詢q=5  
> 只有[6,8]大於等於1，動作次數為(6+8)-q\*2=4；另外[3,1]小於5，動作次數為q\*2-(3+1)=6  
> 總動作次數為4+6=10  

需要一個快速判斷nums中的元素是否大於查詢值q，並且得到總和。  

先將nums排序後，就可以夠過二分搜找最後一個小於等於q的元素索引pivot，從0\~pivot的元素都小於等於q；從pivot\~N-1的元素都大於q。每次複雜度O(log N)  
最後再透過前綴和求0\~pivot的總和，以及pivot+1\~N-1的總和。每次複雜度O(1)。  

時間複雜度為O(N log N)。空間複雜度O(N)。  

```python
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        N=len(nums)
        nums.sort()
        ans=[]
        ps=list(accumulate(nums,initial=0))

        for q in queries:
            pivot=bisect_right(nums,q)-1
            left=(pivot+1)*q-ps[pivot+1]
            right=ps[N]-ps[pivot+1]-(N-1-pivot)*q
            ans.append(left+right)
            
        return ans
```
