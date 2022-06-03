--- 
layout      : single
title       : LeetCode 1224. Maximum Equal Frequency
tags        : LeetCode Hard Array HashTable 
---
隨便抽的題。算是偏簡單的hard，不需要什麼神奇的資料結構就能過。

# 題目
輸入整數陣列nums，回傳符合以下條件的最大**前綴長度**：  
- 從前綴中刪除任一個數字  
- 刪除後使剩下的每個數字出現次數都相同  

如果刪除後沒有剩餘元素，則算是每個元素都出現0次，也符合要求。

# 解法
題目只能做一次刪除動作，要使刪除完的前綴中的所有出現次數相同，那麼一定要刪除出現最多次的元素，因此維護一個變數mx紀錄至為止的**最大相同元素出現次數**是多少。
從例題一可以看出來，當前綴中有x種數字時，其中只有1個數字出現mx次，而剩下(x-1)數字個都出現mx-1次，這時候刪除一個出現mx次的數字即可使出現次數都相同。  
再看看例題二，當前綴中有(x-1)個數字都出現mx次，而剩下1個數字只出現一次，這時候刪除只出現一次的數也合法。  

結果我沒有考慮清楚，漏掉一個corner case：有x個數字，但是**全部都只出現一次**，這時刪掉任一個都可以。  

```python
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq=[0]*(10**5+5)
        cnt=defaultdict(int)
        mx=0
        ans=0
        for size,n in enumerate(nums,1):
            freq[cnt[n]]-=1
            cnt[n]+=1
            freq[cnt[n]]+=1
            mx=max(mx,cnt[n])
            if freq[mx]==1 and size-mx==freq[mx-1]*(mx-1):
                ans=size
            if freq[1]==1 and size-1==freq[mx]*mx:
                ans=size
            if freq[1]==size:
                ans=size
            
        return ans
```
