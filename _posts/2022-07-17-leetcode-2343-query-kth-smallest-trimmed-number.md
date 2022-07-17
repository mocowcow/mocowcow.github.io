--- 
layout      : single
title       : LeetCode 2343. Query Kth Smallest Trimmed Number
tags        : LeetCode
---
周賽302。有點麻煩的題目，花了一些時間才搞懂意思。  

# 題目
輸入字串陣列nums，每個字串的長度相等且只由數字組成。  
另有一個二維整數陣列queries，其中queries[i] = [ki, trimi]。
對於每個queries[i]進行以下動作：  
- 將nums中的每個數字修剪，只留下最右方trimi個數字  
- 找到修建完的數字中第k小數字的索引。如果兩個數字相等，索引值較低者視為較小  
- 將nums中的每個數字恢復原始長度  

回傳與queries長度相同的陣列answer，其中answer[i]是第queries[i]的答案。  

# 解法
看了測資範圍不算是很大，字串數量M<=100，字串長度N<=100，查詢次數k<=100。  
如果照著描述直接暴力法的話，複雜度是O((M\*N\+M log M)*k)，雖然在10^6附近，感覺可以過，但還是有點怕。  

結果我稍微繞了遠路，把所有修剪的值建表，這樣每次查詢只需要O(1)，但是建表成本為O(M\*N^2+M log M)。  
在M、N和k都是100的情況下，兩者其實差不多，但是k不夠大，我的方法跑起來反而會更慢一些，只有k夠大才有優勢。  

維護雜湊表d，紀錄各長度修剪後產生的數字。  
首先遍歷nums中的所有數字字串n，從最後一個字元開始加回去到子字串t，並將t轉回整數，和原索引i一起加入雜湊標d[修剪長度]裡面。  

列舉完所有字串的所有修剪結果之後，全部排序，然後遍歷queries，將所求的第k個索引加入答案。  

```python
class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        N=len(nums[0])
        d=defaultdict(list)
        ans=[]
        
        for i,n in enumerate(nums):
            t=''
            for c in reversed(n):
                t=c+t
                d[len(t)].append([int(t),i])

        for v in d.values():
            v.sort(key=itemgetter(0))

        for k,t in queries:
            ans.append(d[t][k-1][1])
            
        return ans
```
