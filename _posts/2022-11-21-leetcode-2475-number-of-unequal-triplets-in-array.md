--- 
layout      : single
title       : LeetCode 2475. Number of Unequal Triplets in Array
tags        : LeetCode Easy Array HashTable
---
周賽320。挺不錯的題目，只要加強測資範圍瞬間變成中等題。  

# 題目
輸入正整數陣列nums，找到所有符合以下條件的三元組(i, j, k)：  
- 0 <= i < j < k < nums.length  
- nums[i], nums[j], 和nums[k]三個整數互不相等  

求有多少符合條件的三元組。  

# 解法
節省時間，最直觀的做法當然是三迴圈窮舉ijk，把題目的三個不等式直接貼上去即可。  

時間複雜度O(N^3)，空間O(1)。  

```python
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        N=len(nums)
        ans=0
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        ans+=1
                        
        return ans
```

如果今天陣列大小改成10^6，暴力法肯定不行，得換個方式。  
題目只要求三個不同的數字，而不在乎大小及位置。我們可以先將各整數分組計數，遍歷各整數的出現次數作為中間的j值，已出現過的作為i，而未出現的作為k，依照乘法原理得到i\*j\*k種組合。  

以例題一的[4,4,2,4,3]為例：  
> 2出現1次，3出現1次，4出現3次  
> 以[2]作為中間，左邊有[]，右邊有[3,4,4,4]，組成0\*1\*4 = 0個答案  
> 以[3]作為中間，左邊有[2]，右邊有[4,4,4]，組成1\*1\*3 = 3個答案   
> 以[4,4,4]作為中間，左邊有[2,3]，右邊有[]，組成2\*3\*0 = 0個答案   

計數時空間皆為O(N)，窮舉各值出現次數最差時間也為O(N)，整體時空間O(N)。  

```python
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        d=Counter(nums)
        ans=0
        i=0
        k=len(nums)
        
        for j in d.values():
            k-=j
            ans+=i*j*k
            i+=j
            
        return ans
```