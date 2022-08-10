--- 
layout      : single
title       : LeetCode 46. Permutations
tags        : LeetCode Medium Array Backtracking
---
LC75學習計畫。以前大一考試碰到的題目，那時候根本什麼都不會，根本是難度超標。考完試後才去查到一個比較偏門的解法，但沒有真正搞懂。今天重新思考了一次，原來是如此的經典。

# 題目
輸入由不同整數組成的陣列nums，回傳所有的排列可能。你可以依任何順序回傳答案。  

# 解法
當時好像是看到[這個網站](https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/)，一直覺得很奇怪，也沒怎麼搞懂，就怕下次考試會碰到，所以死背了下來。沒想到還真給我碰到第二次，這個方法就一直沿用至今。  

簡單來說，每個位置i試著和大於等於自己的所有位置j，透過**換位**來列舉出所有可能性，繼續遞迴處理i+1。直到整個陣列處理完後，複製當前陣列到答案裡面，並退出遞迴，處理其他分支。  

不得不說python要交換元素真的是超級方便。

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N=len(nums)
        ans=[]
        
        def bt(i):
            if i==N:
                ans.append(nums[:])
                return
            for j in range(i,N):
                nums[i],nums[j]=nums[j],nums[i]
                bt(i+1)
                nums[i],nums[j]=nums[j],nums[i]
        
        bt(0)
        
        return ans
```

現在想想，交換法比較不直觀，有點難想像，還是使用正統的回溯法，也就是暴力搜+剪枝比較容易理解。  

排列中每個元素只會被使用到一次，所以建立長度N的陣列used，表示元素是否已經被使用過。  
從一個空串列curr開始，試著依不同順序選用元素。每次遍歷所有元素，若尚未使用過，則加入curr中，遞迴挑選下一個元素。  
直到加滿N個元素，複製一份curr到答案裡面。  

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N=len(nums)
        used=[False]*N
        ans=[]
        
        def bt(curr):
            if len(curr)==N:
                ans.append(curr[:])
                return 
            for i in range(N):
                if not used[i]:
                    curr.append(nums[i])
                    used[i]=True
                    bt(curr)
                    curr.pop()
                    used[i]=False
        
        bt([])
        
        return ans
```