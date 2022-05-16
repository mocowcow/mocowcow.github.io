--- 
layout      : single
title       : LeetCode 2275. Largest Combination With Bitwise AND Greater Than Zero
tags        : LeetCode Medium HashTable BitManipulation
---
周賽293。這題不知道為啥跟我的電波不太合，想了20分鐘想不出來。  
眼看超過一千人AC，心急之下弄了個O(N^2)暴力法，果不其然的TLE。

# 題目
**陣列AND運算**指的是對陣列中所有的整數做**位元&**。  
- 例如nums=[1,5,3]AND運算，等價於1&5&3=1  
- nums[7]，則結果為7  

輸入正整數陣列candidates，你可以選擇任意個元素形成組合，且每個索引的元素只能被選擇一次。  
求**陣列AND運算**結果大於0的最大**組合長度**。

# 解法
本來以為是DP，一直糾結要怎麼選擇那些要拿或是不拿，對應的最佳結果怎麼紀錄。  
後來仔細想想，只要同位置的1位元出現n次，就可以保證答案不為0，其他位置是0是1根本沒差。  
![示意圖](/assets/img/2275-1.jpg)

維護雜湊表d，紀錄各位元的出現次數，遍歷candidates，將對應的1位元計數+1。  
最後看哪個位置1出現最多次，該出現次數就是答案。

```python
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        d=Counter()
        for n in candidates:
            i=0
            while n>0:
                if n&1:
                    d[i]+=1
                n>>=1
                i+=1
                
        return max(d.values())
```

N<=10**7，換算下來最多24個位元，可以遍歷24次candidates，將空間降低到O(1)。  

```python
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans=0
        for i in range(24):
            ans=max(ans,sum(1 for n in candidates if n&(1<<i)))
                    
        return ans
```