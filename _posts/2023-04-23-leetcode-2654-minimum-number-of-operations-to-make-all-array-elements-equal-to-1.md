--- 
layout      : single
title       : LeetCode 2654. Minimum Number of Operations to Make All Array Elements Equal to 1
tags        : LeetCode Medium Array Math
---
周賽342。理論上，這次也是無壓軸題的簡單周賽，但怎麼每次我碰到送分場都會有一題莫名打結。  
原本做完Q3是80名，卡Q4最後變成2000名，有夠慘。  

# 題目
輸入**正整數**陣列nums。你可以執行以下操作任意次：  
- 選擇一個滿足0 <= i < N-1的索引i，將nums[i]或是nums[i+1]變成兩者的gcd  

求**最少**需要幾次操作才可以nums中所有元素變成1。若不可能，則回傳-1。  

# 解法
若想使a,b兩數的gcd比a和b更小，則兩者必須要有不共通的公因數。而任何數和1的gcd都是1。  
只要nums中本來就有1，可以直接讓非1的數和1做gcd，答案是N-(1的出現次數)。  

否則必須試著透過某些數的gcd變出一個1，然後再用這個1把其他數也變成1。  
如例題的[2,6,3,4]：  
> 先讓nums[2]和nums[3]做gcd  
> 變成[2,6,3,1]  
> 找到1後讓其他的也變成1

雖然說[3,4]可以變出1，不過[2,6,3]也可以。但是後者需要多一次操作，所以要盡可能使用較少的數來組成1。  
若使用k個數組成1，則需要k-1次操作，然後把其他N-1個數都變成1，總共是k+N-2次操作。  

從k=2開始嘗試，枚舉每個索引i作為左邊界，若成功以[i,i+k-1]的子陣列得到gcd=1，代表找到答案，回傳上述公式。  
窮舉完畢都沒找到，代表整個nums的gcd不為1，回傳-1。  

時間複雜度O(N^2 \* (N + log MX))，其中MX為nums[i]的最大值，gcd至多從MX減半log MX次，到1不會繼續變化。  
空間複雜度O(1)。  

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N=len(nums)
        
        if 1 in nums:
            return N-nums.count(1)
        
        for k in range(2,N+1):
            for i in range(N-k+1):
                x=0
                for j in range(i,i+k):
                    x=gcd(x,nums[j])
                if x==1:
                    return k+N-2
                
        return -1
```

如果改成先窮舉起點i，再窮舉長度k的子陣列gcd，就不用每次都重頭計算。  

時間複雜度降低到O(N \* (N + log MX))。空間複雜度O(1)。  

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N=len(nums)
        
        if 1 in nums:
            return N-nums.count(1)
        
        k=inf
        for i in range(N):
            x=0
            for j in range(i,N):
                if j-i+1>=k:
                    break
                x=gcd(x,nums[j])
                if x==1:
                    k=j-i+1
                    
        if k==inf:
            return -1
            
        return k+N-2
```
