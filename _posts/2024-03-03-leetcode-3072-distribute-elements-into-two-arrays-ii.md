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

哩扣時間限制真的是很詭異，也不知道是時間累計還是 python 限制太嚴格。  
直接開 [1, 1e9] 的動態開點線段樹會超時；如果按照各 TC 最小/最大值開點，還是要跑將近 9 秒，快要超時。  

把 nums 離散化之後，動態開點變成 4 秒多。  
但是都離散化了，那我乾脆用 BIT，只需要 2 秒。  

以上這幾種方法的時間複雜度都一樣，但最快的還是 sorted list，耗時僅 1.5 秒。  

```python
from sortedcontainers import SortedList as SL

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        mp = {x:i for i, x in enumerate(sorted(set(nums)))}
        b1, b2 = BIT(N), BIT(N)
        a1, a2 = [], []
        
        def append(b, a, x):
            b.update(mp[x], 1)
            a.append(x)
        
        append(b1, a1, nums[0])
        append(b2, a2, nums[1])
        for i in range(2, N):
            x = nums[i]
            mpx = mp[x]
            gc1 = b1.query_range(mpx + 1, N - 1)
            gc2 = b2.query_range(mpx + 1, N - 1)
            if gc1 > gc2 or (gc1 == gc2 and len(a1) <= len(a2)):
                append(b1, a1, x)
            else:
                append(b2, a2, x)

        return a1 + a2

class BIT:
    """
    tree[0]代表空區間，不可存值，基本情況下只有[1, n-1]可以存值。
    offset為索引偏移量，若設置為1時正好可以對應普通陣列的索引操作。
    """

    def __init__(self, n, offset=1):
        self.offset = offset
        self.tree = [0]*(n+offset)

    def update(self, pos, val):
        """
        將tree[pos]增加val
        """
        i = pos+self.offset
        while i < len(self.tree):
            self.tree[i] += val
            i += i & (-i)

    def query(self, pos):
        """
        查詢[1, pos]的前綴和
        """
        i = pos+self.offset
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & (-i)
        return res

    def query_range(self, i, j):
        """
        查詢[i, j]的前綴和
        """
        return self.query(j)-self.query(i-1)
```
