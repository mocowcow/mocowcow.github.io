--- 
layout      : single
title       : LeetCode 2401. Longest Nice Subarray
tags        : LeetCode Medium Array SlidingWindow BitManipulation
---
周賽309。雖然我有順利做出來，但是似乎繞了一些遠路。  

# 題目
輸入由正整數組成的陣列nums。  
若某子陣列中，每個元素對其他元素做位元AND運算的結果都為0，則稱此子陣列為**好的**。  

求最長的**好的**子陣列長度。  
注意：長度為1的子陣列永遠是**好的**。  

# 解法
找最長的子陣列，又是最近熱門的滑動窗口。  
若兩個數做AND運算結果為0，則其必定沒有共通的1位元。若好幾個數互相做AND都為0，則每個位置最多只能出現一次1位元，否則必定不為0。  

按照以上思路，我們只要維護在哪個位置出現過1位元，在做滑動窗口時，碰到重複位元則縮減左邊界。  
因為要多次標記/清除各位元很麻煩，寫成兩個函數add和remove，分別可以將某數字n的1位元全部標記或清除。  

列舉nums中每個元素作為窗口右邊界，加入新元素並縮減左邊界之後以窗口大小更新答案。  
在add的過程中，如果需要標記的位元已經被占用，則代表有衝突，必須用remove縮減左邊界直到沒有元素衝突為止。  
remove就比較單純，查看哪個位置是1位元，清除標記。  

標記和清除複雜度都是O(1)，每個元素最被標記和清除各一次，共N個元素，整體時間複雜度O(N)。  

```python
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        def add(n):
            for i in range(30):
                if n&(1<<i):
                    while used[i]:
                        remove(nums[left])
                    used[i]=True
        
        def remove(n):
            nonlocal left
            for i in range(30):
                if n&(1<<i):
                    used[i]=False
            left+=1
            
        ans=1
        left=0
        used=[False]*30
        
        for right,n in enumerate(nums):
            add(n)
            ans=max(ans,right-left+1)
            
        return ans
```

其實只要用XOR相消的特性，就可以簡單的把某個數字對應的所有1位元給去掉。  
因為只有在新元素n和已選擇的所有數字沒有衝突之下，才會將新的1位元加入(OR運算)。那麼之後將此元素在做一次XOR時，必定能夠還原到原本的狀態。  

```python
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        sm=0
        ans=1
        left=0
        
        for right,n in enumerate(nums):
            while sm&n!=0:
                sm^=nums[left]
                left+=1
            sm|=n
            ans=max(ans,right-left+1)
        
        return ans
```