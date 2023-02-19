--- 
layout      : single
title       : LeetCode 2568. Minimum Impossible OR
tags        : LeetCode Medium Array HashTable BitManipulation Greedy
---
雙周賽98。又是老朋友位元運算，比Q2好想一些。  

# 題目
輸入整數陣列nums。  

如果一個整數x可以透過nums中的某些元素進行位元OR而得到，則稱為**可表達的**。  

求最小且不為零的**不可表達**正整數。  

# 解法
**可表達的**數有兩種方式：  
1. 本身就在nums中出現過  
2. 由nums中若干的元素OR而成  

以3為例子，其二進位 = "11"  
1. 3可以直接出現在nums中  
2. 或是由1和2組成，"01" | "10" = "11"  

若是2的冪次，如1,2,4,8..，則只會有一個1位元，所以只有在nums中出現，才是**可表達的**。  

可以從1開始逐項窮舉整數x，若x不在nums中，則直接回傳。  

再來看看3,5,6,7..這些非2的冪次數。如果3不在nums中，必須藉由1和2組成；如果5不在nums中，則需1和4組成。這些數是由比自己小的**2的冪次數**組成。故能證明最小的**不可表達數**必定是2的冪次。  

依照上述結果，直接由小到大窮舉2的冪次數，若不在nums中出現就是答案。  

時間複雜度O(N + log MX)，其中N為nums長度，MX為max(nums)。空間複雜度O(N)。  

```python
class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s=set(nums)

        for i in range(32):
            if (1<<i) not in s:
                return (1<<i)
```

上面迴圈數寫死是因為上限10^9最多30個位元。若測資範圍改變可以不寫死。  

```python
class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s=set(nums)
        ans=1
        
        while ans in s:
            ans<<=1 # ans*=2
            
        return ans
```