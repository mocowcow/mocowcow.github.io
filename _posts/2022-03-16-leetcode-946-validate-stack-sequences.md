---
layout      : single
title       : LeetCode 946. Validate Stack Sequences
tags 		: LeetCode Medium Array Stack Simulation
---
每日題。今天是stack連續第四天出現。  

# 題目
模擬一個stack，數列pushed為押入的順序，檢查有沒有辦法實現popped的順序彈出元素。
> pushed = [1,2,3,4,5], popped = [4,5,3,2,1]  
> st = [1]  
> st = [1,2]  
> st = [1,2,3]  
> st = [1,2,3,4] pop4  
> st = [1,2,3]  
> st = [1,2,3,5] pop5  
> st = [1,2,3] pop3  
> st = [1,2] pop2  
> st = [1] pop1  
> st = [] 回傳true 

# 解法
照著stack的運作方式模擬。  
維護堆疊st和變數i,j分別指向push和pop陣列，如果st為空或是頂端元素不為下個想要的pop值，則不斷壓入新的元素；若可壓入元素中途用完則代表不可能完成。  

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st=[]
        N=len(pushed)
        i=j=0
        while j<N:
            if not st or st[-1]!=popped[j]:
                if i<N:
                    st.append(pushed[i])
                    i+=1
                else:
                    return False
            else:
                st.pop()
                j+=1

        return True
```

討論區大神直接拿pushed陣列當作stack，不需要額外空間的解法。  
i為stack寫入頭，j為下個要求的彈出元素索引，每次彈出則i往回、j向後走。最後i回到原本位置代表stack中沒有剩餘，回傳true。

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N=len(pushed)
        i=j=0
        for n in pushed:
            pushed[i]=n
            while i>=0 and pushed[i]==popped[j]:
                i-=1
                j+=1
                
            i+=1
        return i==0
```

