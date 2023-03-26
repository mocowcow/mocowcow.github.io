--- 
layout      : single
title       : LeetCode 2601. Prime Subtraction Operation
tags        : LeetCode Medium Array Math Greedy
---
周賽338。

# 題目
輸入長度為n的整數陣列nums。  

你可以執行以下動作任意次：  
- 選取未選過的索引i，再找一個**嚴格小於**nums[i]的質數p，將nums[i]減去p  

如果能夠使得nums成為**嚴格遞增**的陣列，則回傳true；否則回傳false。  

# 解法
先篩出所有範圍內的質數。本題nums[i]最大1000，所以只要找1000以內的質數。  

如果從左往右遍歷，找到某個nums[i+1]大於nums[i]，為了要使nums嚴格遞增，則必須將nums[i]減少；而減少nums[i]可能又會使左方其他元素不符合，很難處理。  
如果從右往左遍歷，修改nums[i]則不會影響右方已經處理過的元素。而為了使左邊元素合法的機率更大，必須選擇可以剛好使得nums[i]<nums[i+1]的最小質數p。  

注意：若nums[i]原本就小於nums[i+1]則不需要動作。  

時間複雜度O(MX\*N)，其中MX為max(nums)，N為nums長度。空間複雜度O(MX)。  

```python
n=1000
sieve = [True]*(n+1)
prime = []
for i in range(2, n+1):
    if sieve[i]:
        prime.append(i)
        for j in range(i*i, n+1, i):
            sieve[j] = False

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        N=len(nums)

        for i in range(N-2,-1,-1):
            if nums[i]<nums[i+1]:
                continue
            for p in prime:
                if p<nums[i] and nums[i]-p<nums[i+1]:
                    nums[i]-=p
                    break
            if nums[i]>=nums[i+1]:
                return False
            
        return True
```
