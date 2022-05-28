--- 
layout      : single
title       : LeetCode 268. Missing Number
tags        : LeetCode Easy Array Math HashTable BitManipulation Sorting
---
每日題。一題多解，結果我第一次就想到follow up要求的最佳解。

# 題目
輸入陣列nums，包含[0, n]內的n個不同的數字，返回陣列中唯一缺少的數字。

# 解法
先從最差的方法開始。  
可以把nums排序，這樣子索引i應當等於nums[i]，若碰到i!=nums[i]時，代表i消失了。  
如果迴圈跑完還沒找到，那就代表消失的是N。  
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N=len(nums)
        nums.sort()
        for i in range(N):
            if nums[i]!=i:
                return i
            
        return N
```

換個進步一點的方法，時間複雜度進步到O(N)。  
把0\~N所有數字裝進集合，遍歷nums中所有數字n移出集合，最後集合中只會剩下缺少的那個數。  

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=set(range(len(nums)+1))
        for n in nums:
            s.remove(n)
            
        return s.pop()
```

有點像是上面兩種方法的綜合版，但使用XOR運算。  
ans初始為0，對0\~N全部做一次XOR，再對nums中所有數字做一次XOR。  
數字一樣兩兩相消，只有消失的數字消不掉。  

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N=len(nums)
        ans=N
        for i in range(N):
            ans^=nums[i]^i   
            
        return ans
```

最佳版本，時間O(N)，空間O(1)。  
等差數列和公式求1\~N總和，再把nums中所有數字扣掉，剩下的就是答案。  

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N=len(nums)
        tot=N*(N+1)//2
        return tot-sum(nums)
```