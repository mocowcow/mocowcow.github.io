---
layout      : single
title       : LeetCode 3086. Minimum Moves to Pick K Ones
tags        : LeetCode Hard Array PrefixSum Greedy
---
周賽 389。基本上是以前出過題目的大補包，道理我都懂，但就是一直寫錯。  
前綴和求距離和這東西好像是第四次考，該替他準備模板了。  
相似題：  

- [2968. apply operations to maximize frequency score]({% post_url 2023-12-17-leetcode-2968-apply-operations-to-maximize-frequency-score %})  
- [2615. sum of distances]({% post_url 2023-04-11-leetcode-2615-sum-of-distances %})  
- [2602. minimum operations to make all array elements equal]({% post_url 2023-03-26-leetcode-2602-minimum-operations-to-make-all-array-elements-equal %})  

## 題目

輸入長度 n 的二進位陣列 nums，還有正整數 k 跟非負整數 maxChanges。  

Dylan 在玩一個遊戲，目標是用最少的操作來找到 k 個 1。  
遊戲開始時，Dylan 可以選擇站在 [0, n - 1] 之間的任意一個索引，記做 index。  
如果 nums[index] == 1，Dylan 可以撿起當前位置的 1，並把 nums[index] 變成 0 (不需要操作)。  
然後，Dylan 可以進行任意次操作 (包含 0 次)，每次操作可選擇以下**之一**：  

- 選擇索引 j != index 滿足 nums[j] == 0  
    將 nums[j] 變成 1。最多只能進行 maxChanges 次  
- 選擇兩個相鄰的索引 x, y 滿足 (|x - y| == 1) 和 nums[x] == 1, nums[y] == 0  
    將兩者的值交換 (將 nums[y] 變成 1，而 nums[x] = 0)  
    若 y == index，則 Dylan 可以直接撿起 1，並使 nums[y] 變成 0  

求 Dylan **最少**需要幾次操作，才能找到 k 個 1。  

## 解法

總之就是選某個索引 index 站著。  
第二種操作可以從其他索引 j 收集 1，需要 abs(i - j) 次。簡稱**收集**。
第一種操作可以把 1 放到旁邊，然後再用操作二收起來，總共兩次。簡稱**生成**。  

題目保證 maxChanges + sum(nums) >= k，一定能找滿 k 個。  
如果 nums 中沒有 1，那就只能靠生成，答案是 k \* 2。  

---

index - 1, index, index + 1 這三個中心區域索引的收集成本分別是 1, 0, 1。  
中心點的成本最低，優先收集，再來是成本 2 的生成，最後不夠才收集更遠的。  

最理想的狀況是收集中心區域的三個，其餘全用生成的。  
先枚舉每個 1 作為 index，看中心區域最多能收集幾個 1，記為 mid_one。  
中心收集成本 mid_cost = mid_one - 1。  
如果 mid_one + maxChanges >= k，代表剩下的可以靠生成。生成成本 side_cost = (k - mid_one) * 2。  
答案是 mid_cost + side_cost。  

為什麼 index 一定要有 1？試想以下例子：  
> [1,1,0,1,0,1], k = 2  
> 以大括號表示 index，底線表示不收集的  
> [1,{1},\_,\_,\_,\_] 成本 1  
> [\_,1,{0},1,\_,\_] 成本 2  
> [\_,\_,\_,{1},0,1] 成本 2  

很明顯，index 沒有 1 的話根本虧爛。  

---

如果以上兩種特殊情況都不成立，那就代表 maxChanges 不夠用。  
必須額外找 size = k - maxChanges 個 1。  
再從 k 個 1 之中找出 index 使得距離和最小化。  

我們可以很直觀的判斷出 k 個 1 是**連續的**，畢竟散得越開距離肯定越遠。  
但是 k 個之中誰要當 index？答案是**中位數**。  

假設以最左邊的點做 index。  
每把 index 往右移一格，左邊所有點與 index 距離都增加 1；右邊的所有點與 index 距離都減少 1。  
只有在中位數的點作為 index 時，才會使得兩邊變化量平衡。對於左右中位數都是相同的結果。  

這其實正是經典的**貨倉選址問題**。可以用前綴和快速求出距離和。  

---

最後的問題只剩下找到所有大小為 size 的區間的中位數了。  
雖然我們要的是中位數，但如果枚舉中心點的話還要判斷左右邊的 1 夠不夠，很麻煩。  
直接**枚舉左端點** left，而右端點 right = left + size - 1，中位數 index 自然就出來了。  
找到最小的距離和之後，加上生成的成本 max_changes * 2 就是答案。  

時間複雜度 O(N)。  
空間複雜度 O(N)。  

```python
class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        N = len(nums)
        ones = [i for i, x in enumerate(nums) if x == 1]
        if not ones:
            return k * 2
        
        # find mid part
        mid_one = 0
        for index in ones:
            cnt = 1
            if index > 0 and nums[index - 1] == 1:
                cnt += 1
            if index + 1 < N and nums[index + 1] == 1:
                cnt += 1
            mid_one = max(mid_one, cnt)
        
        # only need k
        mid_one = min(mid_one, k)
        # use mid part and maxChanges
        if mid_one + maxChanges >= k:
            mid_cost = mid_one - 1
            side_cost = (k - mid_one) * 2
            return mid_cost + side_cost

        # enumerate median as index
        ans = inf
        M = len(ones)
        ps = list(accumulate(ones, initial=0))
        size = k - maxChanges
        for left in range(M - size + 1):
            right = left + size - 1
            mid = (left + right) // 2
            index = ones[mid]
            l_cnt = mid - left + 1 # [left, mid]
            r_cnt = right - mid + 1 # [mid, right]
            l_part = index * l_cnt - (ps[mid + 1] - ps[left])
            r_part = (ps[right + 1] - ps[mid]) - index * r_cnt
            ans = min(ans, l_part + r_part)
        
        return ans + maxChanges * 2
```
