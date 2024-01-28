---
layout      : single
title       : LeetCode 3020. Find the Maximum Number of Elements in Subset
tags        : LeetCode Medium Array HashTable
---
周賽382。藏了小小的 edge case，好像不少人中計。  

## 題目

輸入**正**整數陣列 nums。  

你必須從 nums 中選擇一個**子集**，其滿足：  

- 能夠將子集的元素按照 [x, x<sup>2</sup>, x<sup>4</sup>, ..., x<sup>k/2</sup>, x<sup>k</sup>, x<sup>k/2</sup>, ..., x<sup>4</sup>, x<sup>2</sup>, x] 的規律排列  
- k 可以是任何**非負**的 **2 的次方數**  

例如： [2, 4, 16, 4, 2] 和 [3, 9, 3] 符合規律，但 [2, 4, 8, 4, 2] 不符合規律。  

求滿足條件的子集中，**最大**的子集大小。  

## 解法

可以發現這個子集是類似於山狀的陣列，中間的值最大，往左右遞減。山頂只有一個，子集大小必定是奇數。  
至於兩邊的山坡一定要同時增加，一個元素至少要出現兩次，才能放在山坡。  

山坡的規律是 x, x^2, x^4, ..，直接將元素乘上自己，就可以得到下一個數。  
~~有點像**快速冪**~~。  

但是好像沒有什麼根據可以快速找到最好的**山頂**或是**山坡起點**。那能不能暴力枚舉？  
山坡上的元素每次成長至少是**兩倍以上**，就算陣列中 N 個元素剛好都可以裝進子集，最多也只需要 O(log N)。  
但是 nums[i] 的上限是 10^9，約等於 2^30。也就是說山坡大約只能成長 30 次，其實遠遠小於 O(log N)。  

---

首先紀錄所有元素的的出現頻率。枚舉每個元素 x 作為山坡上的數，最差的情況下子集就只有這一個數。  
如果 x 至少出現兩次，那就是著找下一個數 x\*x 做為新的山頂，不斷重複。  

但有例外：1 不管幾次方都是 1，選擇一個**全是 1 的子集**也是合法的。  
不得不說範例很有良心，裡面隱約提醒你有 1 這個元素，沒注意到就虧大了。  

時間複雜度 O(N log MX)，其中 MX = max(nums)，此為 10^9。  
空間複雜度 O(N)。  

```python
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        d = Counter(nums)
        ans = 1
        
        # edge case: 1 only
        cnt = d[1]
        if cnt % 2 == 0:
            cnt -= 1
        ans = max(ans, cnt)
        
        # general case
        for x in d:
            if x == 1:
                continue
             
            cnt = 0
            while x in d:
                ans = max(ans, cnt + 1)
                if d[x] >= 2:
                    x *= x
                    cnt += 2
                else:
                     break

        return ans
```
