---
layout      : single
title       : LeetCode 3277. Maximum XOR Score Subarray Queries
tags        : LeetCode Hard DP BitManipulation
---
weekly contest 413。看到位運算我就往**拆位**的方向去思考。方向錯誤當然是沒想出答案。  

## 題目

輸入長度 n 的整數陣列 nums，還有長度 q 的二維整數陣列 queries，其中 queries[i] = [l<sub>i</sub>, r<sub>i</sub>]。  

每次查詢，你必需找到 nums[l<sub>i</sub>..r<sub>i</sub>] 的任意**子陣列**的**最大 XOR 分數**。  

**XOR 分數**指的是一個陣列 a 不斷執行以下操作，直到剩下一個元素，該元素就是分數：  

- 除了最後一個 a[i] 以外，同時將所有 a[i] 的值改成 a[i] XOR a[i + 1]。  
- 刪除 a 的最後一個元素。  

回傳長度 q 的陣列 answer，其中 answer[i] 是第 i 次查詢的答案。  

## 解法

老實說這題還真有點小陷阱，查詢是找 nums 的**子陣列的子陣列**的最大分數，而不是固定範圍的 nums[l..r]。  

先手玩幾個例子看有沒有規律。  
以下 (x3) 符號代表有三個元素 x 做 XOR 的總和。  
先看三個元素：  
> score[a,b,c]  
> 操作 1 次 = [ab, bc]  
> 操作 2 次 = [a(2b)c]  

再試試看四個元素：  
> score[a,b,c,d]  
> 操作 1 次 = [ab, bc, cd]  
> 操作 2 次 = [a(2b)c, b(2c)d]  
> 操作 3 次 = [a(3b)(3c)d]  

發現 a(2b)c 這東西好像很眼熟，不就是 score[a,b,c] 嗎？  
那 b(2c)d 應該是 score[b,c,d] 。  
感覺 score[a,b,c,d] 好像是由 score[a,b,c] 和 score[b,c,d] 拼起來的。  

再看看五個元素：  
> score[a,b,c,d,e]  
> 操作 1 次 = [ab, bc, cd, de]  
> 操作 2 次 = [a(2b)c, b(2c)d, c(2d)e]  
> 操作 3 次 = [a(3b)(3c)d, b(3c)(3d)e]  
> 操作 4 次 = [a(4b)(6c)(4d)e]  

發現 score[a,b,c,d,e] 確實是由 score[a,b,c,d] 和 score[b,c,d,e] 拼起來的。  
大膽假設 score[i..j] 的是由 score[i+1..j] 和 score[i..j-1] 所組成。  
直到子陣列長度為 1 時，分數就是元素自己本身。  

---

上面規出的規律有許多**重疊的子問題**，因此考慮 dp。  
定義 score(i, j)： nums[i..j] 的分數。  
轉移：score(i, j) = score(i+1, j) ^ score(i, j-1)。  
BASE：當 i = j 時，答案為 nums[i]。  

這部分複雜度是 O(N^2)。  

---

但別忘記一開始說的小陷阱。
查詢是要問 nums[l..r] 的任意**子陣列**的最大分數。  

nums[i..j] 的子陣列可以由 nums[i+1..j], nums[i..j-1] 的子陣列**聯集**而成，再加上新產生的 score[i..j]。  
還是**重疊的子問題**，再次 dp。  

定義 mx(i, j)： nums[i..j] 的**子陣列的最大分數**。  
轉移：mx(i, j) = max(
    mx(i+1, j),
    mx(i, j-1),
    score(i, j)
)  
BASE：當 i = j 時，答案為 nums[i]。

轉移時多一個來源，但複雜度還是 O(N^2)。  

---

處理完兩次 dp 後，只需要按照查詢範圍回答 mx[l][r] 即可。  

時間複雜度 O(N^2)。  
空間複雜度 O(N^2)，答案空間不計入。  

注意：本題測資有點大，記憶化寫法會 TLE / MLE，似乎只有遞推可以過。  

```python
class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        @cache
        def score(i, j): # score of nums[i..j]
            if i == j:
                return nums[i]
            return score(i, j - 1) ^ score(i + 1, j)

        @cache
        def mx(i, j): # max score of subarrays of nums[i..j]
            if i == j:
                return nums[i]
            return max(
                mx(i, j - 1),
                mx(i + 1, j),
                score(i, j)
            )

        return [mx(l, r) for l, r in queries]
```

改寫成遞推版本。  

```python
class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)

        score = [[0] * N for _ in range(N)]
        mx = [[0] * N for _ in range(N)]
        for i in range(N):
            score[i][i] = nums[i]
            mx[i][i] = nums[i]

        # score of nums[i..j]
        for i in reversed(range(N)):
            for j in range(i + 1, N):
                score[i][j] = score[i + 1][j] ^ score[i][j - 1]

        # max score of subarrays of nums[i..j]
        for i in reversed(range(N)):
            for j in range(i + 1, N):
                mx[i][j] = max(score[i][j], mx[i + 1][j], mx[i][j - 1])

        return [mx[l][r] for l, r in queries]
```
