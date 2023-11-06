---
layout      : single
title       : LeetCode 2926. Maximum Balanced Subsequence Sum
tags        : LeetCode Hard Array DP SegmentTree HashTable PrefixSum BIT
---
周賽370。想半天才想通，結果動態開點線段樹模板效能不佳，最後一個測資跑不過。最後優化來不及，好虧啊。  

## 題目

輸入整數陣列nums。  

一個nums的長度k子序列，其包含的索引為i<sub>0</sub> < i<sub>1</sub> < ... < i<sub>k-1</sub>。  
若滿足以下條件則稱為**平衡的**：  

- 對於每個在[1, k-1]之間的j，滿足nums[i<sub>j</sub>] - nums[i<sub>j-1</sub>] >= i<sub>j</sub> - i<sub>j-1</sub>  

長度為1的子序列永遠是平衡的。  

求nums平衡子序列可以得到的**最大元素總和**。  

## 解法

對於j<i的nums[j]和nums[i]來說，只有nums[i]-nums[j] >= i-j，才可以把nums[i]接在nums[j]後面。  

但是隨著i改變，每個i-j和nums[i]-nums[j]值都要重新計算，這樣複雜度會高達O(N^2)。  
後來靈機一動，發現可以把式子變形：  
> nums[i]-nums[j] >= i-j  
> 移項得到nums[i]-i >= nums[j]-j  

把nums[i]-i看成一個變數，就叫他diff[i]好了。  
如此條件就簡化成：只要diff[j]小於等diff[i]，可則nums[i]接在nums[j]後面。  

依序枚舉nums[i]，找到diff[i]的值，記做d。  
找到以小於等於d的nums[j]結尾的最大子序列總和best。則以nums[i]結尾的最大總和sub即是max(0,best)+nums[i]。  
然後以sub更新以d結尾的子序列最大值。  
遍歷完，答案就是所有d結尾的子序列最大值。  

上述操作需要單點修改，區間查詢，使用**線段樹**來達成。  
d的範圍大約在[-10^9, 10^9]之間，理論上動態開點線段樹應該也能過，誰知道就是會TLE。  
最後我使用**離散化**+普通線段樹才通過。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        # 區間查詢
        # 回傳[i, j]的max
        def query(id, L, R, i, j):
            if i <= L and R <= j:  # 當前區間目標範圍包含
                return tree[id]
            ans = -inf
            M = (L+R)//2
            if i <= M:
                ans = max(ans,query(id*2, L, M, i, j))
            if M+1 <= j:
                ans  = max(ans,query(id*2+1, M+1, R, i, j))
            return ans


        # 單點更新
        # 對索引i改成val
        def update(id, L, R, i, val):
            if L == R:  # 當前區間目標範圍包含
                tree[id] = val
                return
            M = (L+R)//2
            if i <= M:
                update(id*2, L, M, i, val)
            else:
                update(id*2+1, M+1, R, i, val)
            tree[id] = max(tree[id*2],tree[id*2+1])  # 以左右子樹更新答案
            
        diff=[x-i for i,x in enumerate(nums)]
        mp={x:i for i,x in enumerate(sorted(set(diff)))}
        N=len(diff)+5
        tree = [-inf]*(N*4)
        for i,d in enumerate(diff):
            d=mp[d]
            best=query(1,0,N-1,0,d)
            sub=max(best,0)+nums[i]
            update(1,0,N-1,d,sub)
            
        return query(1,0,N-1,0,N-1)
```

雖然說是區間查詢，但事實每次查詢的起點都是0(離散化後對應diff最小值)，也就是**前綴**最大值。  
既然是前綴，可以改用常數更小的**樹狀陣列**。  

注意：樹狀陣列用來求極值時，只能求**前綴極值**。若是max，則值只能增大；求min，則值只能減少。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

雖然複雜度相同，但執行時間不到線段樹的一半，空間也只需要1/4。  

```python
class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        diff=[x-i for i,x in enumerate(nums)]
        mp={x:i for i,x in enumerate(sorted(set(diff)))}
        N=len(diff)
        bit=BIT(N)
        for i,d in enumerate(diff):
            d=mp[d]
            best=bit.query(d)
            sub=max(best,0)+nums[i]
            bit.update(d,sub)
            
        return bit.query(N-1)
    
class BIT:
    """
    tree[0]代表空區間，不可存值，基本情況下只有[1, n-1]可以存值。
    offset為索引偏移量，若設置為1時正好可以對應普通陣列的索引操作。
    注意：只能查前綴極值。若求max則tree[i]值只能增、不能減。
    """

    def __init__(self, n, offset=1):
        self.offset = offset
        self.tree = [-inf]*(n+offset)

    def update(self, pos, val):
        """
        將tree[pos]設成val
        """
        i = pos+self.offset
        while i < len(self.tree):
            self.tree[i] = max(self.tree[i], val)
            i += i & (-i)

    def query(self, pos):
        """
        查詢[1, pos]的max
        """
        i = pos+self.offset
        res = -inf
        while i > 0:
            res = max(res, self.tree[i])
            i -= i & (-i)
        return res
```
