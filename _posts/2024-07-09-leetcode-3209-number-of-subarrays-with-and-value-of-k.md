---
layout      : single
title       : LeetCode 3209. Number of Subarrays With AND Value of K
tags        : LeetCode Hard Array BitManipulation HashTable
---
雙周賽 134。  
最近真的是很奇妙，最近幾次周賽會寫的時候都被 unrate 或是卡常數，不會寫就被作弊大軍淹沒，處於一種不太想打的心情。  
基於個人經驗，雙周作弊數比單周還嚴重 (本次 Q4 多達 3000 人通過)。  
乾脆索性不打，只在賽後模擬補題。一補發現有夠簡單，17 分鐘就做完了，心裡更加複雜。  

## 題目

輸入整數陣列 nums 和整數 k。  
求 nums 有多少子陣列，其按位元 AND 運算後的結果等於 k。  

## 解法

原題 [3171. find subarray with bitwise and closest to k]({% post_url 2024-06-02-leetcode-3171-find-subarray-with-bitwise-and-closest-to-k %})。  

差別在於原題只要知道子陣列運算後的結果**值**，本題還需要知道**數量**。  

---

總而言之，因為位運算特性的關係，每次運算後至少會改變 1 個位元，所以同一個索引 i 結尾的子陣列結果至多只會有 log MX 種。  
我們遍歷 nums 中的每個元素 x，逐一與先前所有子陣列做 AND 運算，途中順便統計有多少個子陣列值等於 k 即可。  

時間複雜度 O(N log MX)，其中 MX = max(nums)。  
空間複雜度 O(log MX)。  

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        d = Counter()
        for x in nums:
            # all subarrays AND x
            d2 = Counter()
            for y, val in d.items():
                d2[y & x] += val
            d = d2
            d[x] += 1
            
            # update answer
            ans += d[k]
                
        return ans
```

前陣子自己搞了個[模板](https://github.com/mocowcow/python-cp-library/blob/master/pattern/bit_manipulation/bit_trick.py)，複製貼上就完事了。  

```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        return bit_trick(nums)[k]

def bit_trick(nums):

    class Item:
        """
        以索引 i 為固定右端點
        滿足子陣列 nums[j..i] 所有元素按位運算的結果等於 val
        其中 first <= j <= last
        """

        def __init__(self, val, first, last) -> None:
            self.val = val  # 子陣列按位運算結果
            self.first = first  # 最小的 j
            self.last = last  # 最大的 j

    freq = Counter()  # 依按位運算結果統計子陣列個數
    op_res = []
    for i, x in enumerate(nums):
        # 每個子陣列和 x 按位運算
        for it in op_res:
            it.val &= x  # OR, AND, GCD
        op_res.append(Item(x, i, i))

        # 去重合併，更新端點
        tail = 0
        for it in op_res:
            if op_res[tail].val != it.val:
                tail += 1
                op_res[tail] = it
            else:
                op_res[tail].last = it.last  # 更新最後端點
        del op_res[tail + 1:]  # op_res = op_res[:tail + 1]

        # 依按位運算結果更新答案
        for it in op_res:
            freq[it.val] += it.last - it.first + 1
    return freq
```
