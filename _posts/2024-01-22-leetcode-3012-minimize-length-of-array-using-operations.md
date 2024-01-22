---
layout      : single
title       : LeetCode 3012. Minimize Length of Array Using Operations
tags        : LeetCode Medium Array Math Greedy
---
雙周賽122。這題大概也算是腦筋急轉彎，快把我搞吐血。  

## 題目

輸入正整數陣列 nums。  

你可以執行以下操作**任意(包含零)次**，並將 nums 的長度**最小化**：  

- 選擇兩個不同的索引 i, j，滿足 nums[i] > 0 且 nums[j] > 0  
- 將 nums[i] % nums[j] 的結果加入 nums 尾端  
- 刪除 nums[i] 和 nums[j]  

求任意次操作後，nums 的**最小長度**。  

## 解法

分類討論選擇 a, b 兩數做 a % b 的情形：  

- 若 a < b，一定得到 a
- 若 a >= b：  
  - a 是 b 的倍數，得到 0  
  - a 不是 b 的倍數，得到 a % b  

整理後發現，只要存在不同大小的數，則一定可以刪除**較大者**。  
最後剩下的幾個相同的數，倆倆一組變成 0，不成對的則維持不變。  
例如：  
> [1,1,1,2,2,3,4]  
> 先透過 1 把較大的數都刪掉，得到 [1,1,1]  
> 剩下的 1 倆倆成對變成 0，得到 [0,1]  
> 落單的 1 能留著不變，答案最小長度是 2  

若最後剩下 cnt 個相同的最小值，操作則會剩下 (cnt + 1) / 2 個。  
大功告成，提交答案。得到一個免費的 WA。  

---

試想以下例子：  
> nums = [15,15,15,21]  
剛才的作法會得到 [0,15]，最小長度是 2。  

但正確作法是：  
> 選 21 % 15，得到 [15,15,15,6]  
> 然後刪掉較大者，得到 [6]  
> 最小長度 1  

我靠，這個 6 是哪來的？仔細想想這個 a % b 好像有點眼熟，正是**輾轉相除法**。  
只要求整個 nums 的 gcd，就可以知道透過操作得到的**最小值**g，進而把其他大於 g 的數全刪掉。  

這下又有兩種情況：  

- nums 中原本不存在 g，那全部的元素都會被刪掉，只剩下一個 g
- nums 原本就有 g，那就先刪掉大的，剩下的倆倆相消  

最終答案是 max(1, (cnt+1) / 2)。  

---

對於 a, b 兩數求 gcd 的時間複雜度是 O(log min(a, b))，總共需要求 N-1 次。  
但根據元素順序不同，如果由大到小求 gcd，則複雜度會稍微超過 O(N \* log min(nums))，乾脆以最大值計算。  

時間複雜度 O(N \* log MX)，其中 MX 是 max(nums)。  
空間複雜度 O(1)。  

```python
class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        g = gcd(*nums)
        cnt = nums.count(g)
        
        return max(1, (cnt+1) // 2)
```
