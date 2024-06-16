---
layout      : single
title       : LeetCode 3187. Peaks in Array
tags        : LeetCode Hard Array SortedList BinarySearch
---
周賽 402。又是線段樹題，這次我有把樹搞出來，但是題目查詢的地方沒想通，又繞了大遠路去搞 sorted list。  
除了思路有點障礙之外，寫得還很醜，真的差點沒寫出來。  

## 題目

若陣列 arr 中的某個元素**大於**其前後的元素，則稱為**峰值**。

輸入整數陣列 nums 以及二維整數陣列 queries。  
你必須執行以下兩種操作：  

- queries[i] = [1, l<sub>i</sub>, r<sub>i</sub>]  
    查詢子陣列 nums[l<sub>i</sub>..r<sub>i</sub>] 中的峰值數量  
- queries[i] = [2, index<sub>i</sub>, val<sub>i</sub>]  
    將 nums[index<sub>i</sub>] 改成 val<sub>i</sub>

回傳一個陣列，依序代表每次查詢的結果。  

注意：子陣列中**第一個**和**最後一個**元素都**不是**峰值。  

## 解法

陣列中的每個元素只有**是峰值**或**不是峰值**兩種狀態。  
因此可以使用有序容器 sorted list 維護峰值的索引，並搭配二分搜找到區間 [l..r] 之間的個數。  
首先遍歷 nums 並將所有峰值加入容器中。  

---

先來看查詢：  
題目有說到，子陣列中第一和最後一個元素不是峰值，因此查詢 [l..r] 實際上只要找 [(l+1)..(r-1)] 之間的索引。  
先二分找到第一個大於等於 l+1 的索引 i，然後找 最後一個小於等於 r-1 的索引 j，峰值個數為 j-i+1。  
為了避免 l+1 > r-1 而造成負值，記得和 0 取最大值。  

---

再來看更新：  
想想看，改變 nums[i] 的值會有什麼影響？  

1. 讓 nums[i] 變成峰值 / 不是峰值  
2. 讓 nums[i-1] 變成峰值 / 不是峰值  
3. 讓 nums[+1] 變成峰值 / 不是峰值  

因此修改 nums[i] 後，要重新判斷以上三個位置的峰值狀態。  
實際上只要處理 **峰值=>不是峰值** 和 **不是峰值=>峰值** 兩種變化，依照狀態從有序容器中增刪索引。  

時間複雜度 O((N + Q) log N)。  
空間複雜度 O(N)，答案空間不計入。  

```python
from sortedcontainers import SortedList as SL
class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        sl = SL()  # peaks
        is_peak = [False] * N

        for i in range(1, N - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                sl.add(i)
                is_peak[i] = True

        ans = []
        for q in queries:
            if q[0] == 1:
                _, l, r = q
                i = sl.bisect_left(l + 1)
                j = sl.bisect_right(r - 1) - 1
                ans.append(max(0, j - i + 1))
            else:
                _, i, val = q
                nums[i] = val
                for j in range(max(1, i - 1), min(N - 2, i + 1) + 1):
                    to_peak = nums[j - 1] < nums[j] and nums[j] > nums[j + 1]
                    if is_peak[j] and not to_peak:  # remove peak
                        is_peak[j] = False
                        sl.remove(j)
                    elif not is_peak[j] and to_peak:  # add peak
                        is_peak[j] = True
                        sl.add(j)

        return ans
```

處理峰值變化那塊長的有夠醜，又長又難寫，不小心就寫錯了。  
有種技巧可以搞得更簡潔：**恢復現場**。  
若受到影響的索引 j 原本是峰值，則先把狀態標記取消，待 nums[i] 更新值後再重算一次。  

```python
from sortedcontainers import SortedList as SL
class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        sl = SL()  # peaks

        def update(i):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                sl.add(i)
            
        def reset(i):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                sl.remove(i)
                
        for i in range(1, N - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                update(i)

        ans = []
        for q in queries:
            if q[0] == 1:
                _, l, r = q
                i = sl.bisect_left(l + 1)
                j = sl.bisect_right(r - 1) - 1
                ans.append(max(0, j - i + 1))
            else:
                _, i, val = q
                # reset peak state
                for j in range(max(1, i - 1), min(N - 2, i + 1) + 1):
                    reset(j)
                # update peak state
                nums[i] = val
                for j in range(max(1, i - 1), min(N - 2, i + 1) + 1):
                    update(j)

        return ans
```

最後是我當初寫一半的線段樹解法。  
當時改完 nums[i] 的值發現旁邊的峰值不見，一時沒想通就放棄了，真可惜。

與上面方法最大的差別在於：查詢一的 [l..r] 的範圍必須手動檢查。  
還有查詢二不必**恢復現場**，因為線段樹每次更新都會用新值一路向上合併，一定會更新成正確的區間值。  

時間複雜度 O((N + Q) log N)。  
空間複雜度 O(N)，答案空間不計入。  

```python
class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        seg = SegmentTree(N, nums)
        for i in range(1, N - 1):
            seg.update(1, 0, N - 1, i)

        ans = []
        for q in queries:
            if q[0] == 1:
                _, l, r = q
                if l + 1 <= r - 1:
                    res = seg.query(1, 0, N - 1, l + 1, r - 1)
                else:
                    res = 0
                ans.append(res)
            else:
                _, i, val = q
                nums[i] = val
                for j in range(max(1, i - 1), min(N - 2, i + 1) + 1):
                    seg.update(1, 0, N - 1, j)

        return ans


class SegmentTree:

    def __init__(self, n, nums):
        self.tree = [0]*(n*4)
        self.nums = nums
        self.n = n

    def op(self, a, b):
        """
        任意符合結合律的運算
        """
        return a+b

    def push_up(self, id):
        """
        以左右節點更新當前節點值
        """
        self.tree[id] = self.op(self.tree[id*2], self.tree[id*2+1])

    def query(self, id, L, R, i, j):
        """
        區間查詢
        回傳[i, j]的總和
        """
        if i <= L and R <= j:  # 當前區間目標範圍包含
            return self.tree[id]
        res = 0
        M = (L+R)//2
        if i <= M:
            res = self.op(res, self.query(id*2, L, M, i, j))
        if M+1 <= j:
            res = self.op(res, self.query(id*2+1, M+1, R, i, j))
        return res

    def update(self, id, L, R, i):
        """
        單點更新
        判斷 nums[i] 是否為峰值
        """
        if L == R:  # 當前區間目標範圍包含
            if self.nums[L - 1] < self.nums[L] and self.nums[L] > self.nums[L + 1]:
                self.tree[id] = 1
            else:
                self.tree[id] = 0
            return
        M = (L+R)//2
        if i <= M:
            self.update(id*2, L, M, i)
        else:
            self.update(id*2+1, M+1, R, i)
        self.push_up(id)
```
