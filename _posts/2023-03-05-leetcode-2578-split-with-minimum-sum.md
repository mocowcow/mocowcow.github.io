--- 
layout      : single
title       : LeetCode 2578. Split With Minimum Sum
tags        : LeetCode Easy Array String Sorting Greedy Math
---
雙周賽99。腦袋卡住十分鐘，差點暴斃。  

# 題目
輸入正整數num，將其分割成兩個非負整數num1和nums2：  
- num1和num2連接起來是num的一種排列。也就是說，num1和num2中各數字的出現次於等於num中各數字出現次數  
- num1和num2可以有前導零  

求num1和num2的**最小和**。  

# 解法
若num是n位數，num1為a位數，num2為b位數，且a+b=n。  
1. 既然要使總和盡可能小，則兩數位數需平均分配  
2. 將較大數放在較低位，將較小數放在較高位  

總之先把num的數字拆出來排序。  
如果有奇數位數，則把最小的先挑出來。剩下的數字倆倆成對，先把前面加起來的數字移位，在加上兩個新數字。  

時間複雜度瓶頸為排序的O(N log N)，其中N為nums的位數，也就是log num。空間複雜度O(N)。  

```python
class Solution:
    def splitNum(self, num: int) -> int:
        a=sorted(int(c) for c in str(num))
        ans=0
        i=0
        if len(a)%2==1:
            ans=a[0]
            i+=1
        
        while i<len(a):
            ans=ans*10
            ans+=a[i]
            ans+=a[i+1]
            i+=2
        
        return ans
```

後來發現有人是維護兩個數字，最後才加總。這種方法更加直觀。  
順便改成求餘來分解num的位數，複雜度同上不變。  

```python
class Solution:
    def splitNum(self, num: int) -> int:
        a=[]
        while num:
            a.append(num%10)
            num//=10
            
        a.sort()
        num1=num2=0
        for x in a:
            if num1<num2:
                num1=num1*10+x
            else:
                num2=num2*10+x
        
        return num1+num2
```