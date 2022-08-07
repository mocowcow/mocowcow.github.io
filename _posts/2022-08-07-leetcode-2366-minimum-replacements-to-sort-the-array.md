--- 
layout      : single
title       : LeetCode 2366. Minimum Replacements to Sort the Array
tags        : LeetCode Hard Greedy Math
---
雙周賽84。靠著手算算半天才明白，在多個5分鐘就能做出來了，真可惜。  

# 題目
輸入整數陣列nums。在每次動作中，你可以將陣列中的任何元素替換為任何兩個相加的元素。  
例如，nums = [5,6,7]。在一次操作中，可以將nums[1]的6替換為2和4，所以nums變成[5,**2,4**,7]。  

求使nums成為非遞減數列的最少動作次數。  

# 解法
因為每次動作只能將元素拆成更小的兩個數，若要使數列非遞減，只能將左方的元素拆分成更小的數字，所以從數列右方逆著處理。  

維護變數last表示前一個元素的值，我們必須將當前元素n拆分成不大於last的若干個數。  
最後尾的元素永遠不需要拆分，因此從倒數第二個元素開始逆序遍歷所有數字n。
對於每個n有兩種可能：  
1. n小於等於last，不須拆分，所以直接更新last為n  
2. n大於last，需要將n拆成若干個不超過last的數字  

對於情況2來說，至少我們可以很確定需要拆成ceil(n/last)個數，多拆只會使得last更小，不可能是更佳解。將一個數字分成part個部分，需要part-1刀，將part-1加入答案中。  

再來要更新last值，考慮以下幾種狀況：  
> n=8, last=3, part=[2,3,3]  
> n=7, last=3, part=[2,2,3]
> n=6, last=3, part=[3,3]

發現如果n可被last整除，則last維持不變；否則last必須更新。又因為要使得左方元素盡可能大，又不能遞減，所以採取平均分配，那麼最最左方元素就會是floor(n/part)。  

```python
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        N=len(nums)
        last=nums[-1]
        ans=0
        
        for i in range(N-2,-1,-1):
            n=nums[i]
            if n<=last:
                last=n
            else:
                part=(n+last-1)//last
                ans+=part-1
                if n%last!=0:
                    last=n//part
  
        return ans
```

其實可以不必寫這麼多分支，因為n小於等於last的情況下，求出來的part會等於1，代入part-1之後不影響答案。至於更新last的時候，n/part一樣也是n。  
然後更新last的時候也不必判斷是否整除，例如：  
> n=15, last=3, part=5, floor(n/part)=3  
> n=14, last=3, part=5, floor(n/part)=2  

part=n/last，而last=n/part，一樣會保持不變。  

```python
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        N=len(nums)
        last=nums[-1]
        ans=0
        
        for i in range(N-2,-1,-1):
            n=nums[i]
            part=(n+last-1)//last
            ans+=part-1
            last=n//part
            
            
        return ans
```

