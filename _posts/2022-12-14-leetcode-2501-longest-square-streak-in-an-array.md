--- 
layout      : single
title       : LeetCode 2501. Longest Square Streak in an Array
tags        : LeetCode Medium Array HashTable
---
周賽323。有點考驗數據範圍的小心機，確實坑殺了不少人。  

# 題目
輸入整數陣列nums。  

如果nums的一個子序列符合下列條件，則稱之為**連續平方**：  
- 子序列長度至少為2  
- 將子序列**排序後**，除了第一個元素以外，第i個元素必須是第i-1個元素的平方  

求nums的**最長連續平方**長度。若不存在則回傳-1。  

# 解法
測資範圍高達10^5，乍看很可怕，其實不然。  
從最小值的2開始看看：  
> 2, 4, 16, 256, 65535, 4294967296...  

每個子序列頂多成長5次就超過上限，可以視作是常數時間。那麼窮舉nums中每個數字作為首元素，若其平方有出現過，則使長度+1。  
最後有個小陷阱，長度至少要有2。答案預設值先設為-1，只有子序列長度滿足2才更新答案。  

時間為O(5N)，視為O(N)。集合紀錄各元素是否出現，空間也是O(N)。

```python
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ans=-1
        s=set(nums)
        
        for n in s:
            cnt=1
            while n*n in s:
                n*=n
                cnt+=1
            if cnt>1:ans=max(ans,cnt)
        
        return ans
```
