--- 
layout      : single
title       : LeetCode 128. Longest Consecutive Sequence
tags        : LeetCode Array HashTable 
---
每日題。原來我以前的做法都不符合限制，但是這題測資不夠強，O(N log N)跑起來比O(N)還快。  

# 題目
輸入未排序的整數陣列nums，回傳最長連續元素序列的長度。  
複雜度必須在O(N)內。  

# 解法
題目要求在線性時間內完成，排序一定不可能符合，八成是使用雜湊表。  
而且數字範圍從-10^9\~10^9，也不可能開出10^18的陣列當作bucket。  

每次加入新的數字n時，會使得n左方和右方的兩個連續區塊相接，組成一個更大的區塊，最後更新區塊最左和最右端所對應的數字。  
每個數字只能計算一次，否則會使區塊重複計算，得到錯誤結果。因此，即使中間區塊不會再被取用到，也還是需要將其值更新，避免二次計算。  

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d=defaultdict(int)
        ans=0
        for n in nums:
            if n in d:continue
            L=d.get(n-1,0)
            R=d.get(n+1,0)
            # L=d[n-1] # 這樣會使n-1和n+1加入d之中，誤判為已經出現過
            # R=d[n+1]
            curr=L+R+1
            d[n]=d[n-L]=d[n+R]=curr
            ans=max(ans,curr)

        return ans
```

補充個比較直覺的O(N log N)解法。  
先使用set去重複後排序，循序檢查是否每個數相鄰，若不相鄰則重置長度為1；否則長度+1，

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        conn=0
        prev=-inf
        for n in sorted(set(nums)):
            if prev+1!=n:
                conn=1
            else:
                conn+=1
            prev=n
            ans=max(ans,conn)
            
        return ans
```