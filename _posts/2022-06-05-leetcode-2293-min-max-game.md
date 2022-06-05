--- 
layout      : single
title       : LeetCode 2293. Min Max Game
tags        : LeetCode
---
周賽296。模擬題，幸好腦筋轉得快，似乎不少人糾結在怎麼找規律而卡很久。

# 題目


# 解法
本來說想說應該是有個規律可以依照索引位置來判斷取最大或最小，想十秒沒想到就放棄了，反正easy題不需要最佳解，當下之急是先通過再說。  

直接維護一個變數flag，若為true則代表當前取min，否則取max。  
一次取兩個數做運算後加到新的數列中，並將flag做not，一直重複到數列只剩下一個數為止。  

```python
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        flag=True
        while len(nums)>1:
            temp=[]
            for i in range(0,len(nums),2):
                if flag:
                    temp.append(min(nums[i],nums[i+1]))
                else:
                    temp.append(max(nums[i],nums[i+1]))
                flag=not flag
            nums=temp
            
        return nums[0]
```

後來發現規律也很簡單，只是當時一急就沒想到。  
每次取2個數做運算，而只有2種運算，所以2*2=4個數字會形成一次循環。  
對索引i模4就可以知道當前對應哪一種運算，若餘0代表min，餘2則代表max。  

```python
class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums)>1:
            a=[]
            for i in range(0,len(nums),2):
                if i%4==0:
                    a.append(min(nums[i],nums[i+1]))
                else:
                    a.append(max(nums[i],nums[i+1]))
            nums=a
            
        return nums[0]
```
