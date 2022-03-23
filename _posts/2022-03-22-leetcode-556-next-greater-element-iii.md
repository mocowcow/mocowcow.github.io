---
layout      : single
title       : LeetCode 556. Next Greater Element III
tags 		: LeetCode Medium String Math 
---
學習計畫碰到的。用了一個超級爛的方法竟然還能過，笑死了。

# 題目
輸入正整數n，求大於n且和n的數字組成一樣的最小數字。若不存在則回傳-1。整數最大只能到2^32-1。

# 解法
把n轉成字串拿去用內建函數求出所有排列，再用set去重複，就是所有可能的重組數nums了。  
nums排序好，二分搜找第一個大於n的數，如果不存在或是該數超過2^32-1，則回傳-1，否則回傳該數。  

因為n最大可以到2147483647，長度N=10，求排列時間為O(N!)，勉強壓線過去，在大一點可能就不會過了。

```python
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        permu = set(permutations(list(str(n))))
        nums = sorted([int(''.join(x)) for x in permu])
        idx = bisect_right(nums,n)
        
        if idx < len(nums) and nums[idx] <= 2147483647:
            return nums[idx]
        else:
            return -1
```

更新一種解法，數列大致上可以拆成三種情況：  
1. 遞減數列，如321、33220，沒辦法組成更大的數，回傳-1  
2. **嚴格**遞增數列，如1234，將最尾端兩數互換即可。不嚴格遞增如1233不屬於此項  
3. 其他不規則數列  
 
大部分都是屬於第三類，處理起來比較麻煩。  
首先要找到連續的遞減後綴，所以從最後端往回找。如123**987**。  
遞減後綴的左邊第一個數3，會和後綴中一個數交換。因為要最小的增加量，所以選擇大於3的最小數字7。  
將3和7換位後得到127**983**，再將後綴部分反轉，就可以得到答案127389。  

換一個數字546751做驗算：  
> 找遞減後綴546**751**  
> 大於6的最少數字為7，6和7換位=547**651**  
> 後綴反轉547156  

其實也可以不單除處理第一種的遞減數列，只要最後找遞減後綴時檢查i是否停在0即可。

```python
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums=list(str(n))
        N=len(nums)

        # case1:decreasing
        desc=True
        for i in range(1,N):
            if nums[i]>nums[i-1]:
                desc=False
                break
        if desc:
            return -1

        # case2:strictly increasing
        asc=True
        for i in range(1,N):
            if nums[i]<=nums[i-1]:
                asc=False
                break
        if asc:
            nums[-1],nums[-2]=nums[-2],nums[-1]
            return ''.join(nums)
        
        # case3:others
        # find decreasing suffix
        i=N-1
        while i>0 and nums[i-1]>=nums[i]: 
            i-=1
        # find minimum bit greater than nums[i-1]
        j=i
        while j+1<N and nums[j+1]>nums[i-1]:
            j+=1
        # swap i-1 and j
        nums[i-1],nums[j]=nums[j],nums[i-1]
        # reverse suffix
        nums[i:]=nums[i:][::-1]
        ans=int(''.join(nums))
        
        if ans<=2147483647:
            return ans
        else:
            return -1
```        
