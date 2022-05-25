--- 
layout      : single
title       : LeetCode 354. Russian Doll Envelopes
tags        : LeetCode Hard Array DP Sorting BinarySearch
---
每日題。連兩天出hard了，對於新人似乎不太友善。

# 題目
輸入整數陣列envelopes，其中envelopes[i] = [w, h]，表示信封的寬度和高度。  
只有當某個信封的寬、高都大於另一個信封時，才能被裝入。  
試著把信封層層包住，求最多能包幾層。注意：信封不可以旋轉。

# 解法 
第一個難點在於：寬、高都要滿足，才能把另一個信封裝起來。  
將所有信封以寬度遞增、高度遞減的方式排序：  
> [[5,4],[6,4],[6,7],[2,3]]   
> 排序後=[[2,3],[5,4],[6,7],[6,4]]  

如此一來可以確保後方的信封一定不會比前方的寬度還小，那我們只要盡可能找到最適合的寬度就好。  
剩下的部分就是和[300. longest increasing subsequence]({% post_url 2022-04-19-leetcode-300-longest-increasing-subsequence %})相同的概念。  

初始化陣列dp，保存遞增的高度，並遍歷所有信封，以每個信封的寬度h在dp中找到第一個大於等於h的位置做替換。  
若dp中所有高度都比h小，則直接將h加入dp尾端。  
注意，dp中儲存的高度**不代表實際信封高度**。例如：  
> [[2,3],[5,4],[6,7],[6,4],[7,5]]    
> dp=[] 當前=[2,3] 加入3  
> dp=[3] 當前=[5,3] 加入4  
> dp=[3,4] 當前=[6,7] 加入7  
> dp=[3,4,7] 當前=[6,4]以4替換4  
> 這時候dp[1]的實際上是[6,4] 而dp[2]是[6,7]  

最後回傳dp大小就是可以重複套疊的信封數量。

```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        e=sorted(envelopes,key=lambda x:(x[0],-x[1]))
        dp=[]
        for _,h in e:
            idx=bisect_left(dp,h)
            if idx<len(dp):
                dp[idx]=h
            else:
                dp.append(h)
                
        return len(dp)
```
