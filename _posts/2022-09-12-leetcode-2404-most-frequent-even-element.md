--- 
layout      : single
title       : LeetCode 2404. Most Frequent Even Element
tags        : LeetCode Easy Array HashTable Sorting
---
周賽310。久違的在Q1吃到BUG。

# 題目
輸入一個整數陣列nums，回傳出現最多次的偶數元素。  
若有多的元素出現次數相同，則回傳**最小的**元素。若不存在答案則回傳-1。  

# 解法
特別提醒一下，題目要求的是**最小元素**，而不是**索引最小**。 

可以簡單的用雜湊表計算每個元素的出現次數，而變數mx紀錄最高頻率。  
ans預設-1，只有在當前元素頻率高於mx時，或頻率等於mx且當前元素較小時才更新答案。  

時間複雜度O(N)，空間複雜度O(N)。  

```python
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d=Counter()
        mx=0
        ans=-1
        
        for n in nums:
            if n%2==0:
                d[n]+=1
                if d[n]>mx:
                    mx=d[n]
                    ans=n
                elif d[n]==mx and n<ans:
                    ans=n
                    
        return ans
```

也可以透過排序使得相同元素聚集，不用透過額外空間就可以計算出現頻率。  
而且元素是遞增出現，後方元素頻率與mx相同時一定較大，所以只要在頻率高於mx時更新答案。  
時間複雜度O(N log N)，空間複雜度O(1)。  

```python
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        mx=0
        ans=-1
        prev=None
        cnt=0
        
        for n in nums:
            if n%2==0:
                if n!=prev:
                    prev=n
                    cnt=0
                cnt+=1
                if cnt>mx:
                    mx=cnt
                    ans=n
                    
        return ans
```

最後來個懶人解法，先統計所有偶數的出現頻率，如果都沒有偶數直接回傳-1。  
否則找到最高頻率mx，再篩選出頻率為mx的所有元素，回傳當中最小值。  
時間複雜度O(N)，空間複雜度O(N)。  

```python
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d=Counter(x for x in nums if x%2==0)
        if not d:
            return -1
        mx=max(d.values())
        return min(x for x in d if d[x]==mx)
```