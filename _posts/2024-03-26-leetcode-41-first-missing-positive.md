---
layout      : single
title       : LeetCode 41. First Missing Positive
tags        : LeetCode Hard Array HashTable Sorting
---
每日題。cycle sort 系列。
總覺得這東西很雞肋，姑且記錄一下。  

原版 cycle sort 時間複雜度 O(N^2)，優點是寫入次數比較少 (有點雞肋)。  
這幾次用到的都是閹割版本，不能正確排序重複數字，也因此時間是複雜度比較低的 O(N)。  

從 [1, N] 的連續數字中找**缺失/重複**的數字題型，大部分都可以使用。  

## 題目

輸入未排序的整數陣列 nums。  
回傳在 nums 中**沒有出現**的**最小正整數**。  

時間複雜度必須是 O(N)，且只使用 O(1) 額外空間。  

## 解法

對於 O(1) 額外空間的限制，很多都是靠**修改輸入參數**來乘載**額外的訊息**。  

陣列長度為 N，最差情況下 [1, N] 各出現一次。
而陣列索引為 [0, N-1]，如果把數字 x 放到索引 x - 1 的位置，正好一人一格。  
如果要放的目標位置已經被占用，那就代表**出現重複**。但我們只管缺失，不管重複，就直接把他留著，反正之後會被擠到後面。  

舉個簡單例子：  
> nums = [1,1,2]  
> i = 0，nums[0] = 1  
> 1 正好要放在 nums[0]，不動作  
> i = 1，nums[1] = 1  
> 1 應該放 nums[0]  
> 但是 nums[0] 已經是 1，出現重複，放著不管  
> 這時候一樣 nums = [1,1,2]  
> i = 2，nums[2] = 2  
> 2 應該放 nums[1]  
> nums[1] = 1，沒被占用，所以把 nums[1] 和 nums[2] 交換  
> 最後 nums = [1,2,1]  

回到剛才講的 nums[i] 應該要放 i + 1。  
從頭遍歷 nums 看哪個位置上的數字不對，代表他沒出現。  
如果 [1, N] 都出現了，那答案很明顯只能是 N + 1。  

---

但是 nums 中會出現 [1, N] 以外的數，如**零**、**負數**甚至**N + k**。  
這些東西絕對不可能找到合理的排放位置，碰到的話直接不管，之後同樣會被擠到後面。  

這兩層迴圈乍看之下很像是 O(N^2)，其實不然。  
對於滿足 1 <= x <= N 的元素 x，每次把 x 換位都會換到**正確且空閒**位置上，而陣列中只有 N 個空位，因此最多只會換位 N 次。  

時間複雜度 O(N)。  
空間複雜度 O(1)。  

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            while nums[i] != i + 1:
                # ignore invalid
                if not (1 <= nums[i] <= N):
                    break
                    
                j = nums[i] - 1
                # ignore dup
                if nums[j] == nums[i]: 
                    break
                
                # swap nums[i] to nums[i - 1]
                nums[i], nums[j] = nums[j], nums[i]
        
        for i in range(N):
            if nums[i] != i + 1:
                return i + 1
        
        return N + 1
```
