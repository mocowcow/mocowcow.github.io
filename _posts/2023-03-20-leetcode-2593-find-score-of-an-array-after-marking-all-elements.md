--- 
layout      : single
title       : LeetCode 2593. Find Score of an Array After Marking All Elements
tags        : LeetCode Medium Array Heap
---
雙周賽100。就是單純考排序或是heap的應用。  

# 題目
輸入正整數陣列nums。  

初始分數為0，你必須執行以下運算：  
- 找到nums中最小且未被**標記**的元素。如果有多個最小值，則選擇索引最小者  
- 將選中的元素加到分數中  
- 將選中的元素和其相鄰元素(如果有的話)**標記**  
- 不斷重複直到所有元素都被**標記**  

求執行完運算後的分數。  

# 解法
維護一個min heap，遍歷nums將所有數對(val, idx)加入。  
再建立一個長度為N的布林陣列vis，vis[i]代表索引i是否被標記。  

逐次將heap中所有數對(val, i)取出，如果i已經被標記過則跳過；否則標記i和其鄰居，並將val加入答案。  

出入heap每次log(N)，共N次，時間複雜度O(N log N)。空間複雜度O(N)。  

```python
class Solution:
    def findScore(self, nums: List[int]) -> int:
        N=len(nums)
        h=[]
        vis=[False]*N
        for i,val in enumerate(nums):
            heappush(h,[val,i])
            
        ans=0
        while h:
            val,i=heappop(h)
            if vis[i]:continue
            vis[i]=True
            ans+=val
            if i>0:
                vis[i-1]=True
            if i+1<N:
                vis[i+1]=True
        
        return ans
```
