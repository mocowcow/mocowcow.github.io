---
layout      : single
title       : LeetCode 2835. Minimum Operations to Form Subsequence With Target Sum
tags        : LeetCode Hard Array Greedy Sorting Stack BitManipulation
---
周賽360。這題原本是medium，賽後改成hard了。  
雖然難，但不需要特殊的DSA，應該還算是個不錯的面試題。  

## 題目

輸入由數整數陣列nums還有整數target，其中nums只由**非負**的2的次方數組成。  

每次操作，你可以：  

- 選擇任意nums[i]，其中nums[i] > 1  
- 將nums[i]從陣列中移除  
- 在陣列**末端**加入兩個nums[i] / 2  

求使得nums中存在一個總和為target的**子序列**，需要操作的**最小次數**。若無法達成，則回傳-1。  

## 解法

滿多不重要的垃圾訊息，2的次方數不管怎樣都不可能是負數，不如說是nums都是**整數**。  
而且求的是子序列，代表元素次序不重要，所以加在末端還是哪裡都無所謂。  

target以二進位表示，也可以分解成若干的不重複的**2的次方數**，稱為sub。  
我們目標試著從nums中組出這些東西。  

看看例題二：  
> nums = [1,32,1,2], target = 12  
> sub = [8,4]  
> 需要把32拆成兩個16，再把一個16拆成兩個8  
> 然後1+1+2=4  
> 共2次操作  

每次操作只能產生較小的元素，如果我們對nums由大到小處理，無法知道當前的元素**需不需要拆**。以這題為例，即無法知道32需要被拆解。  
反之，從小到大處理，如果可以用小於等於sub[i]的元素來組成sub[i]最好；若不夠則嘗試拆分第一個大於sub[i]的元素。  

這個例子中，使用了[1,1,2]來滿足sub[i]=4，那如何知道有辦法用小於sub[i]的數組成？  
因為nums中也只出現**2的次方數**，第一個小於sub[i]的數是sub[i]/2，再來是sub[i]/4...，因此只要總和足夠，則保證能滿足sub[i]。  

瓶頸為排序，時間複雜度O(N log N)。  
空間複雜度O(N)，原地排序可達O(1)。  

```python
class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        st=sorted(nums,reverse=True)
        ans=0
        remain=0
        
        for i in range(32):
            sub=1<<i
            if target&sub:
                while remain<sub:
                    if not st:
                        return -1
                    if st[-1]<=sub:
                        remain+=st.pop()
                    else:
                        ans+=1
                        t=st.pop()
                        st.append(t//2)
                        st.append(t//2)
                remain-=sub
        
        return ans
```
