--- 
layout      : single
title       : LeetCode 2789. Largest Element in an Array after Merge Operations
tags        : LeetCode Medium Array Greedy Stack
---
周賽355。似乎很久沒有出貪心題了。  

# 題目
輸入**正整數**陣列nums。  

你可以執行以下操作任意次：  
- 選擇滿足0 <= i < nums.length - 1以及nums[i] <= nums[i+1]的整數i  
- 將nums[i+1]替換成nums[i] + nums[i+1]，並將nums[i]從陣列中刪除  

求陣列中可以達到的**最大元素**值為多少。  

# 解法
簡單說就是找兩個相鄰的數a和b，只要a <= b就可以把兩個合併。  

假設有三個連續的數字[a,b,c]，且滿足a <= b <= c。  
如果先讓bc合併，那麼之後一定也可以把a合併過來；如果先讓ab合併了，之後有可能因為過大而無法和c合併。  
又假設[a,b,c]，其中b > c，那麼無論如何c都不可能變大，之後左邊的數字越來越大，c也就更不可能合併了。  
因此得出貪心的結論：從右往左遍歷，可以合併就合併，不能合併就丟掉。  

又根據此結論，被丟棄的元素肯定是較小的值，不可能是答案；所以nums中最後剩下的一個元素，若不是被留下的較大值，不然就是兩者合併後的新值，反正他一定是答案。  
我們可以直接把nums當做堆疊，模擬上述的過程。  

時間複雜度O(N)。  
空間複雜度O(1)，原地修改輸入。  

```python
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        st=nums
        while len(st)>1:
            b=st.pop()
            a=st.pop()
            if a<=b: # merge
                st.append(a+b)
            else: # discard
                st.append(a)
        
        return st[0]
```
