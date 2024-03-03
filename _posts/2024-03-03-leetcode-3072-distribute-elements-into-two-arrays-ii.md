---
layout      : single
title       : LeetCode 3072. Distribute Elements Into Two Arrays II
tags        : LeetCode Hard Array BinarySearch SortedList Simulation
---
周賽387。近幾次中最簡單的 Q4，其實應該只有中等難度。  

## 題目

輸入索引由 1 開始，長度為 n 的整數陣列 nums。  

定義函數 greaterCount(arr, val)，回傳 arr 中**嚴格大於** val 的元素有幾個。  

你必須執行 n 次操作，將 nums 中的元素分配到 arr1 和 arr2 中。  
第一次操作，先將 nums[1] 加入 arr1。第二次操作，將 nums[2] 加入 arr2。  
之後第 i 次操作，則按照以下規則：

- 若 greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i])，則將 nums[i] 加入 arr1  
- 若 greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i])，則將 nums[i] 加入 arr2  
- 若 greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i])，則將 nums[i] 加入長度較短者  
- 若兩者長度還是相等，那就將 nums[i] 加入 arr1  

陣列 result 是由 arr1 和 arr2 連接而成。  
例如：arr1 = [1,2,3], arr2 = [4,5,6]，則 result = [1,2,3,4,5,6]。  

回傳陣列 result。  

## 解法

總之先實作函數 greaterCount(arr, val)。  
要範圍計數，可以用 sorted list、線段樹、BIT、前綴和。  
arr 內容會變動，先刪除前綴和；val 範圍太大很麻煩，線段樹、BIT 需要離散化，很麻煩。  
那就選 sorted list。  

先二分找到第一個大於 val 的索引 idx，則 [idx..N-1] 範圍內的元素都大於 val。  

---

但是 sorted list 會破壞元素原本加入的順序，因此還需要維護兩個陣列 a1, a2，保持元素加入的順序。  
每次加入元素時，要同時往 sorted list 和陣列加入新元素 val。  
這也可以提取出來，變成一個函數 append(sl, a, val)。  

最後只要按照題目的比較規則，決定要往哪個陣列新增元素即可。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        s1, s2 = SL(), SL()
        a1, a2 = [], []
        
        append(s1, a1, nums[0])
        append(s2, a2, nums[1])
        for i in range(2, N):
            x = nums[i]
            gc1 = gc(s1, x)
            gc2 = gc(s2, x)
            if gc1 > gc2 or (gc1 == gc2 and len(a1) <= len(a2)):
                append(s1, a1, x)
            else:
                append(s2, a2, x)
                
        return a1 + a2
        
        
def append(sl, a, val):
    sl.add(val)
    a.append(val)

def gc(sl, x):
    idx = sl.bisect_right(x)
    return len(sl) - 1 - idx + 1
```
