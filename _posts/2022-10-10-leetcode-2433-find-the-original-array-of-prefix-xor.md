--- 
layout      : single
title       : LeetCode 2433. Find The Original Array of Prefix Xor
tags        : LeetCode Medium Array BitManipulation PrefixSum
---
周賽314。又又又是哩扣最愛的位元運算，好像連續三次出現XOR了。  

# 題目
輸入一個大小為n的整數陣列pref。找到並回傳滿足以下條件大小n的陣列arr：  
- pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]  

注意，^表示位元XOR運算。  
可以證明答案是獨一無二的。  

# 解法
再次複習XOR的特性：兩兩相消。  

我們要找到陣列arr，使得pref[i]等於arr前i個元素的XOR總和。也就是說，pref[i]=pref[i-1]^arr[i]。  
最後通過移項得到arr[i]=pref[i-1]^pref[i]。除了arr[0]=pref[i]以外，其他都可以透過此公式推出。  

時間複雜度O(N)，空間複雜度O(N)。  

```python
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        N=len(pref)
        arr=[0]*N
        arr[0]=pref[0]
        
        for i in range(1,N):
            arr[i]=pref[i-1]^pref[i]
            
        return arr
```

python一行版本。  

```python
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return (a^b for a,b in pairwise([0]+pref))
```

另一個思路是前綴和的還原。前綴和做差分可以得到原陣列，直接在pref上計算出差分也可以。  

```python
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        N=len(pref)
        
        for i in range(N-1,0,-1):
            pref[i]^=pref[i-1]
            
        return pref
```