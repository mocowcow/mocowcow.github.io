--- 
layout      : single
title       : LeetCode 456. 132 Pattern
tags        : LeetCode Medium Array Stack MonotonicStack
---
每日題。竟然是單調堆疊，這幾天我和他很有緣份。

# 題目
輸入陣列nums，檢查是否存在**132模式**。  
**132模式**指的是nums[i], nums[j], nums[k]組成的子序列，符合i<j<k且nums[i]<nums[k]<nums[j]。

# 解法
從前面找往後找太麻煩，要同時確認比n1大比n3小。改成由後往前找，只要找到比n2小的數字就可以，因為比n2小一定也比n3小。  
n2初始化為-inf，因為n3要找最大的數，所以使用單調遞減堆疊。  
由後往前遍歷所有數n1，如果n1小於n2，這時n1也一定小於n3，成功找到132模式，回傳true；否則堆疊頂端應為最大的數字，也就是n3，將所有較小的數字彈出並更新n2。  
如果遍歷完還沒找到，代表無法找到模式，回傳false。

```python
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n2=-math.inf
        st=[]
        for n1 in reversed(nums):
            if n1<n2:
                return True
            while st and n1>st[-1]:
                n2=st.pop()
            st.append(n1)
            
        return False
```
