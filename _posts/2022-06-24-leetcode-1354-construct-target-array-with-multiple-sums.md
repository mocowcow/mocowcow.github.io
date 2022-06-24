--- 
layout      : single
title       : LeetCode 1354. Construct Target Array With Multiple Sums
tags        : LeetCode Hard Array Heap
---
每日題。這題測資好像加強過，按照提示來做竟然TLE。  

# 題目
輸入長度為n的陣列target。你有由n個1組成的陣列arr，執行以下動作：  
- x是當前陣列中所有元素的總和  
- 選擇arr中的任一索引i，使arr[i]設為x  
- 可以重複任何次數  

若能使arr與target相等，則回傳true，否則回傳false。  

# 解法
arr陣列初始全為1，每次修改元素後，一定會比上次修改的元素更大。因此除了1以外，不可能有其他數字重複出現。  
所以我們必須從target中較小的元素開始達成，然後我就想不出怎麼辦了。  

看一下提示說什麼：  
> 鑒於總和是嚴格遞增的，我們可以以相反的方式模擬其過程  
> 把陣列中最大元素扣除陣列其餘部分，直到所有元素都成為1  

有什麼資料結構能夠快速找到最大值？使用max heap。  
把target塞入max heap中，並計算target的總和sm。每次取出最大值mx，則其餘部分remain=sm-mx，若remain大於mx則會使元素小於1，即無法達成，回傳false；否則重複將最大值減少，到最大值也等於1為止。  

```python
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        h=[]
        sm=sum(target)
        for n in target:
            heappush(h,-n)
            
        while -h[0]>1:
            mx=-heappop(h)
            remain=sm-mx
            if mx>remain:
                sm-=remain
                heappush(h,-(n-remain))
            else:
                return False
        
        return True
```

雖然上面程式碼邏輯是正確的，但是碰到特定測資會慘死，例如：  
> target = [1,1000000000]  
> target = [2,900000001]  

這樣會執行10^9次運算，造成TLE，需要有更好的方法來加速。  
對於每個mx，都要扣除掉n個remain，而這正好就是MOD運算在做的事情。直接對mx模運算求餘數，把得到的餘數放回heap中。  
模運算的除數不可為0，當remain等於0時應直接回傳false，而餘數等於0時也是false；但像上面[1,1000000000]的例子，當remain=1時，得到的餘數會是0，可是正確來說應該要使mx成為1，要另外當作特例處理。  

```python
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        sm=sum(target)
        h=[-x for x in target]
        heapify(h)
        
        while -h[0]>1:
            mx=-heappop(h)
            remain=sm-mx
            if remain==1:return True
            if remain>=mx or remain==0:return False
            r=mx%remain
            if r==0:return False
            sm=sm-mx+r
            heappush(h,-r)
            

        return True
```
