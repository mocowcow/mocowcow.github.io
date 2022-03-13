---
layout      : single
title       : LeetCode 2202. Maximize the Topmost Element After K Moves
tags 		: LeetCode Medium Array Greedy
---
周賽284。上一題挖土浪費30分鐘，這題搞快一小時，噴了8次紅字，這周又沒時間去寫第四題。

# 題目
輸入數列nums，定義最頂端為最左邊。求進行k次動作後，數列最頂端數字的最大值可以為多少。若沒有剩下數字則回傳-1。  
每次可以選擇以下一種動作執行：  
1. 移除最頂端的數字，並放到備用區
2. 若備用區不為空，則可任選一數字加回數列頂端

# 解法
題目說了nums大小N至少有1，但是k可能為0。  
先過濾幾個corner cases：  
1. k=0，直接回傳數列首相
2. k=1，一定要移除一個數。若N=1則回傳-1，否則回傳第二個數
3. N=1，且k為奇數，還是剩下空數列，回傳-1  
4. N=k，只能取到前k-1個數，回傳max(nums[:N-1])

剩下就是general case了，k一定>=2，。  
假設nums=[1,2,3,4,5]，k=4時可以連續移除4次，剩下[5]；或是連續移除3次，加上最大的，得到[3,5]；或是移除2次，加回2次的，得[2,1,3,4,5]。  
歸納下來，確定可以得到第k+1個數字，或是第1~k-1的其中一個，但是不能使用正好第k個數。在nums[:k-1]和nums[k+1]之間最大值就是答案。
  
```python
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if k == 0:
            return nums[0]
        if k == 1:
            if N > 1:
                return nums[1]
            else:
                return -1
        if N == 1 and k % 2 == 1:
            return -1
        if N == k:
            return max(nums[:-1])

        return max(max(nums[:k-1]), nums[min(k, N-1)])

```

[這篇解法](https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/discuss/1844179/Python-or-O(N)T-O(1)S-or-Explanation)流程簡化，只留下一種corner case，思路清晰，可讀性比我的高出好幾倍。

```python
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if N == 1 and k & 1:
            return -1

        mx = -1
        for i in range(min(k-1, N)):
            mx = max(mx, nums[i])

        if N > k:
            mx = max(mx, nums[k])

        return mx

```