--- 
layout      : single
title       : LeetCode 2499. Minimum Total Cost to Make Arrays Unequal
tags        : LeetCode Hard Array HashTable Greedy
---
雙周賽93。如果上一題青蛙是思考題，那這題就是超級思考題，我整個沒有頭緒，連暴力法都想不到怎麼做。  

# 題目
輸入兩個長度皆為n的陣列nums1和nums2。  

每次動作中，你可以將nums1的兩個元素交換位置，其**成本**為兩者**索引值總和**。  
你必須透過上述動作，使得所有nums1[i] != nums2[i]。  

求達成條件的**最小總成本**。若不可能達成則回傳-1。  

# 解法
以下將所有nums1[i]==nums2[i]的索引稱為**非法**；而nums1[i]!=nums2[i]的索引稱為**合法**。  

先找出所有非法的位置，最理想的情況下，應該是兩個非法索引互換，例如：  
> nums1 = [1,2], nums2 = [1,2]  
> nums1[0]和nums1[1]交換  
> nums1 = [2,1], nums2 = [1,2]  

那什麼時候不能這樣換？  
當某數占了非法總數的一半以上，例如：  
> nums1 = [1,1], nums2 = [1,1]  
> 或是 nums1 = [1,1,1,2], nums2 = [1,1,1,2]  
> 不管怎樣換都無法避免  

這時候就要試著找合法的索引來**救援**，例如：  
> nums1 = [3,2,1,1], nums2 = [2,3,1,1]  
> nums1[0]和nums1[2]換  
> nums1[1]和nums1[3]換  
> nums1 = [1,1,3,2], nums2 = [2,3,1,1]  

最後剩下非法總數是奇數，且眾數不超過一半的情形：  
> 若nums1長度=1，眾數一定超過一半，不屬於此類  
> 若nums1長度=2，非法總數為偶數，不屬於此類  
> 從長度3開始，且眾數不超過一半，也就是說至少會有3種不同的整數  
> 所以多出的奇數索引一定可以和nums1[0]交換  
> nums1 = [1,2,3], nums2 = [1,2,3]  
> nums1[0]和nums1[1]交換  
> nums1 = [2,1,3], nums2 = [1,2,3]  
> nums1[2]還是重複，所以和nums[0]換  
> nums1 = [3,1,2], nums2 = [1,2,3]  

將以上情形整理後，歸納出兩類：  
1. 非法眾數不超過總數一半的情況下(無論奇偶)，倆倆交換，答案為非法索引總和  
2. 超過一半，則貪心地找索引較小的合法索引，協助交換，並將使用到的索引加入答案  

最多只需要遍歷兩次，時間複雜度O(N)。若nums1與nums2完全相同，且每個數只出現一次，會有N個整數，空間複雜度O(N)。  

```python
class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        ans=0
        same=0
        d=Counter()
        for i,(a,b) in enumerate(zip(nums1,nums2)):
            if a==b:
                ans+=i
                same+=1
                d[a]+=1
                
        most_key=None
        most_freq=0
        for k,v in d.items():
            if v>most_freq:
                most_freq=v
                most_key=k
                
        if most_freq<=same//2:return ans
        
        for i,(a,b) in enumerate(zip(nums1,nums2)):
            if most_freq<=same//2:break
            if a!=b and a!=most_key and b!=most_key:
                same+=1
                ans+=i
                
        if most_freq<=same//2:return ans
        return -1
```

可以使用Boyer–Moore voting，先找出眾數，在遍歷一次計算眾數出現次數，將空間複雜度壓到O(1)。  

```python
class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        ans=0
        same=0
        most=None
        freq=0
        for i,(a,b) in enumerate(zip(nums1,nums2)):
            if a==b:
                same+=1
                ans+=i
                if freq==0:most=a
                if a==most:
                    freq+=1
                else:
                    freq-=1

        freq=0
        for i,(a,b) in enumerate(zip(nums1,nums2)):
            if a==b==most:freq+=1
                
        for i,(a,b) in enumerate(zip(nums1,nums2)):
            if freq<=same//2:break
            if a!=b and a!=most and b!=most:
                same+=1
                ans+=i
                
        return ans if freq<=same//2 else -1
```