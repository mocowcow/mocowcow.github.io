---
layout      : single
title       : LeetCode 189. Rotate Array
tags 		: LeetCode Medium Array TwoPoints
---
聽說至少有三種解法，各位不妨先試試能想出幾種？

# 題目
輸入一個長度N陣列，將所有元素向右搬移k次。  
不要回傳任何值，直接修改輸入陣列。

# 解法
最直覺的應該是O(N)空間解法，直接複製整個陣列，對k模N，將元素搬移至(index+k)%N。

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k %= N
        arr = nums[:]
        if k == 0:return
        for i in range(N):
            nums[(i+k) % N] = arr[i]
```

Follow up:沒有辦法用O(1)空間解決？  
提示3說了有種方法基於陣列反轉。自己寫一個副函數，可以反轉陣列特定區間。一樣先將k模N，整個反轉，再分別反轉0~k-1、k~N-1即可。  

例如nums=[1, 2, 3, 4, 5, 6, 7], k=3：
> [1, 2, 3, 4, 5, 6, 7]  
[7, 6, 5, 4, 3, 2, 1]  
[5, 6, 7,|| 4, 3, 2, 1]  
[5, 6, 7,|| 1, 2, 3, 4]

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k %= N
        if k == 0:return 

        def reverse(l, r):
            while l <= r:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r -= 1

        reverse(0, N-1)
        reverse(0, k-1)
        reverse(k, N-1)
```

再來一種解法。使用prev及curr暫存陣列值，idx紀錄當前指針，start紀錄起點，每次將idx加k，處理完可觸及的位置後定會回到start，此時再把start、idx、curr，全部右移一格。

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k %= N
        if k == 0:return

        start = prev = idx = 0
        curr = nums[0]
        for _ in range(N):
            prev = curr
            idx = (idx+k) % N
            curr = nums[idx]
            nums[idx] = prev
            if start == idx:
                start += 1
                idx = start
                curr = nums[idx]
```

還有我很久以前亂寫的解法，因為python只有list，把末項元素pop出，壓回頂端k次即可。  
在運行時間分布圖可以看到右端有一座小山丘，全都是這種解法的兄弟，笑死我了。

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k = k % N
        for _ in range(k):
            nums.insert(0, nums.pop())
```