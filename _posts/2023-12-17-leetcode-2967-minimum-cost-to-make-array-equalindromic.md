---
layout      : single
title       : LeetCode 2967. Minimum Cost to Make Array Equalindromic
tags        : LeetCode Medium Array Math Sorting Greedy
---
周賽376。應該算是奇怪的數學題。和付費每周題有點相關，~~有不公平的嫌疑~~。  

## 題目

輸入長度n的整數陣列nums。  

你可以對nums執行特殊操作**任意**次(包含0次)。每次操作的流程是：  

- 選擇[0, n-1]之間的索引i，以及**正整數**x  
- 將|nums[i] - x|加入總成本  
- 將nums[i]的值變成x  

**回文數**指的是一個數字反過來讀也和原本相同。例如121, 2552, 65756都是回文數，但24, 46, 235不是。  
若一個陣列中的所有數都是小於10^9的**回文數**y，則稱其為**等數的**。  

求最少需要幾次操作，才能使得nums變成**等數陣列**。  

## 解法

將陣列中的每個元素想像成數線上的座標，要從這些座標中移動到某個點。  
為了使總移動距離最小，應該要選擇**中位數**。  

但題目多了限制，目標必須是**回文數**。  
中位數m可能不是回文數。目標離m越遠，則總距離增加越多。  
最佳目標肯定是**小於m**或**大於m**的第一個回文數，兩者其一。  

若m不是回文數，則分別往左右找到第一個回文t，並以t當作目標來更新答案。  

複雜度不好算，但是就算中位數在大，也只需要少少幾次都可以快速找到回文數。  
時間複雜度大概是排序的O(N log N)。  
空間複雜度O(1)。  

```python
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        N=len(nums)
        MX=10**9
        nums.sort()
        if N%2==1:
            median=nums[N//2]
        else:
            median=(nums[N//2]+nums[N//2-1])//2
        
        def find(i,dir):
            while True:
                s=str(i)
                if s==s[::-1]:
                    return i
                i+=dir
                if i<1 or i==MX:
                    return inf
        
        l=find(median,-1)
        r=find(median,1)        
        ans=inf
        for t in [l,r]:
            tot=0
            for x in nums:
                tot+=abs(x-t)
            ans=min(ans,tot)
            
        return ans
```

預處理所有小於10^9的回文數，然後二分找到最接近中位數的兩個回文數，分別更新答案。  

每次只要枚舉左半邊的的數x，並將其反轉連接後就是**偶數**位回文數x+x；至於奇數只要多枚舉中心點mid，構造成x+mid+x的。  
回文數最多只有9位數，也就是說左半邊的枚舉範圍只從[1,9999]而已，非常小。  
總共大約有P=10^5個回文數。  

時間複雜度O(N log N + log P)，其中P為回文數個數。預處理時間不計。  
空間複雜度O(1)，預處理空間不計。  

```python
pa=[]
for x in range(1,10):
    pa.append(x)

for x in range(1,10000):
    # even: x+x
    left=right=x
    while right>0:
        right,r=divmod(right,10)
        left=left*10+r
    pa.append(left)
    
    # odd: x+mid+x
    for mid in range(10):
        left=x*10+mid
        right=x
        while right>0:
            right,r=divmod(right,10)
            left=left*10+r
        pa.append(left)
    
pa.sort()
print(len(pa))
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        N=len(nums)
        nums.sort()
        median=(nums[(N-1)//2]+nums[N//2])//2
        
        idx=bisect_right(pa,median)
        ans=inf
        for i in [idx-1,idx]:
            if i>=0 and i<len(pa):
                t=pa[i]
                tot=0
                for x in nums:
                    tot+=abs(t-x)
                ans=min(ans,tot)
        
        return ans
```
