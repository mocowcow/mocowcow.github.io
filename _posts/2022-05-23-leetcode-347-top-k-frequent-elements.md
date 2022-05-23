--- 
layout      : single
title       : LeetCode 347. Top K Frequent Elements
tags        : LeetCode Medium Array Sorting Counting HashTable
---
聽說是抖音面試題，特地來複習一下。

# 題目
輸入整數陣列nums和一個整數k，回傳前k個出現最多次的元素。  
可以以任何順序回傳，且答案保證是**唯一**的。

# 解法
我第一個想法是用雜湊表計數。  
根據以每個元素及其出現次數組成(key,val)的形式，以val為鍵值遞減排序，在回傳前k個。  
時間複雜度O(N log N)。

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        items=sorted(Counter(nums).items(),key=itemgetter(1),reverse=True)
        return [x[0] for x in items[:k]]
```

follow up問：有沒有比O(N log N)更快的方法？  
那只能選擇一些O(N)的排序法了。  

bucket sort，犧牲空間以加快執行速度。  
先計算出每個數字的出現次數，再依照出現次數將元素分組，例：  
> [1,1,1,2,2,3]  
> 出現1次=[3]  
> 出現2次=[2]  
> 出現3次=[1]  

從出現次數1遍歷到N，並將元素串接起來，得到出現次數遞增的陣列[3,2,1]，取後方k個元素就是答案。  
時間複雜度為O(N+k)。

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N=len(nums)
        ctr=Counter(nums)
        freq=defaultdict(list)
        for key,v in ctr.items():
            freq[v].append(key)
        
        ans=[]
        for i in range(N+1):
            if freq[i]:
                ans+=freq[i]
        
        return ans[-k:]
```

把freq改成list，並使用內建函數串接ㄋ的寫法。  

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        N=len(nums)
        ctr=Counter(nums)
        freq=[[] for _ in range(N+1)]
        for key,v in ctr.items():
            freq[v].append(key)
        ans=list(chain(*freq))
        
        return ans[-k:]
```