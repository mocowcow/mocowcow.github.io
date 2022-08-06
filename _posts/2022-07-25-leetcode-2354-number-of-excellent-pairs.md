--- 
layout      : single
title       : LeetCode 2354. Number of Excellent Pairs
tags        : LeetCode Hard Array BitManipulation HashTable
---
周賽303。不僅Q3和上次相似，就連Q4也是超級腦筋急轉彎，兩天都坐牢整整一小時，真是太難過了。  

# 題目
輸入正整數陣列nums和正整數k。  
若一數對(num1, num2)符合以下條件，則稱為**超讚數對**：  
- num1 和 num2 都存在於nums中  
- num1 OR num2和num1 AND num2中，1位元的總數大於或等於k。其中OR和AND都是位元運算  

求有多少不相同的**超讚數對**。

若兩數對(a, b)和(c, d)，只要a!=c或b!=d則視為不同。例：(1, 2)和(2, 1)不相同。  
請注意，即某數num1在nums中只出現一次，依然可以組成(num1, num2)，且num1==num2的超讚數對。  

# 解法
空想半天沒有動手畫畫OR和AND運算的我真是傻，明明只要畫兩三個例子就能想通。以後位元運算想不通一定要先畫才來考慮。  

試想1101和0010做運算會如何：  
> 1101 OR 0010 = 1111  
> 1101 AND 0010 = 0000  
> 共4個1位元  

那麼1111和1111又如何：  
> 1111 OR 1111 = 1111  
> 1111 AND 1111 = 1111  
> 共8個1位元  

可以發現規律，在某位元：  
- 若num1和num2都是1，則AND和OR結果都會是1，提供2個1位元  
- 若只有num1或num2其中一個是1，則OR會是1，AND為0，提供1個1位元  
- 若兩者都是0，則OR和AND都是0，沒有1位元  

講這麼複雜，其實就是num1的1位元個數+num2的1位元各數加總而已。  
問題簡化，以1位元數將nums中的各數字n進行分類計數，裝進雜湊表d中。列舉所有位元數的組合(i,j)，若i+j可以滿足k，代表是**超讚數對**。i位元的數有d[i]個，j位元的數有d[j]個，共可以產生d[i]\*d[j]個答案。  

20220806更新：原來把位元操作畫成圖會這麼好理解，沒想法真的該隨手畫畫。  
![示意圖](/assets/img/2354-1.jpg)

```python
class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        
        def f(n):
            return bin(n).count('1')
        
        d=defaultdict(int)
        ans=0
        for n in set(nums):
            bit=f(n)
            d[bit]+=1
            
        for i in range(1,30):
            for j in range(1,30):
                if i+j>=k:
                    ans+=d[i]*d[j]
        
        return ans
```
