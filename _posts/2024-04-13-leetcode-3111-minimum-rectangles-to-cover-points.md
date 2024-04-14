---
layout      : single
title       : LeetCode 3111. Minimum Rectangles to Cover Points
tags        : LeetCode Hard Array HashTable SortedList BinarySearch
---
雙周賽 128。太急吃兩次 WA，可惜了上分的好機會。  
這次是 LCUS 有不公平的嫌疑，連續三天每日題都是單調堆疊，剛好可以用在這次 Q4。  

## 題目

輸入正整數陣列 nums。  

求 nums 有多少個子陣列，其滿足**第一個**和**最後一個**元素都等於子陣列中的最大值。  

## 解法

求子陣列個數的題型，通常可以枚舉子陣列的左右端點來做。  

先想想暴力法，如果 nums[i] 作為子陣列的右端點，那要怎麼找到合法的左端點？  
是不是從 i 往左邊找 nums[j]，如果找到 nums[j] 等於 nums[i] 則答案加 1，直到出現某個 nums[j] 超過 nums[i] 為止。  
試想以下例子：  
> nums = [3,4,3,3]  
> i = 0，合法左端點有 nums[0] 一個  
> i = 1，合法左端點有 nums[1] 一個  
> i = 2，合法左端點有 nums[2] 一個  
> i = 3，合法左端點有 nums[2], nums[3] 兩個  
> 答案共 5 個  

可以發現，左端點的數量相當於 i 到上一個出現比 nums[i] 大的元素為止，所累計的**出現次數**。  
換句話說，當枚舉 nums[i] = x 時，除了將 x 的出現次數加 1 並加入答案之外，還要將所有小於 x 的元素的出現次數**歸零**。  

---

綜上所述，我們**看似**只需要一個雜湊表來記錄各元素的出現次數。  

但是在 nums 為遞減的情況下，雜湊表中的元素會逼近 N 個，而且每次都無法刪除，使複雜數上升到 O(N^2)。  
為了有效率的找到所有小於 x 的元素，需要把出現過的元素裝入**有序容器**，並透過**二分搜**找到小於 x 的所有元素，**歸零**其出現次數後從容器刪除。  

時間複雜度 O(N log N)。  
空間複雜度 O(N)。  

```python
from sortedcontainers import SortedList as SL
class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        d = Counter()
        sl = SL()
        ans = 0 
        
        for x in nums:
            # track x as valid leftmost point
            if d[x] == 0:
                sl.add(x)
                
            d[x] += 1
            ans += d[x]
            
            # remove elements between [1, x - 1]
            for rmv in list(sl.irange(1, x - 1)): 
                sl.remove(rmv)
                d[rmv] = 0
                    
        return ans
```

剛才提到過，在 nums 呈現遞減時，所有元素都不會被歸零；反過來說，出現**遞增**的時候就有元素會被歸零！  

當 nums[i] = x 時，會往左找到所有小於 x 的 nums[j]，並歸零其出現次數。  
觀察以下例子：
> nums = [1,2,1]  
> nums[0] = 1，第一次出現，加入集合  
> 元素集合 = [1]
> nums[1] = 2，第一次出現，加入集合，並把小於 2 的元素都刪除  
> 元素集合 = [2]  
> nums[2] = 1，(重新)第一次出現，加入集合  
> 元素集合 = [2,1]  

發現**出現次數不為零**的元素集合呈遞減順序，在遇到新元素 x 時刪除小於 x 的所有元素。  
原來是**單調遞減堆疊** (monotonic decreasing stack)！  

依照這個思路從堆疊中刪除元素，並將刪除的元素出現次數歸零即可。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        d = Counter()
        st = []
        ans = 0
        
        for x in nums:
            d[x] += 1
            ans += d[x]
            while st and x > st[-1]:
                rmv = st.pop()
                d[rmv] = 0
            st.append(x)
            
        return ans
```
