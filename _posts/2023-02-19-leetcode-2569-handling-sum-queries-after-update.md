--- 
layout      : single
title       : LeetCode 2569. Handling Sum Queries After Update
tags        : LeetCode Hard Array BitManipulation SegmentTree
---
雙周賽98。雖然有想到線段樹，但不知道怎麼改。看來我跟線段樹還不夠熟。  

# 題目
輸入長度為n的整數陣列nums1和nums2，以及二維查詢陣列qeuries。共有三種查詢：  
1. 第一種，queries[i] = [1, l, r]。對於所有nums1[i]，把0變成1，把1變成0。其中l <= i <= r  
2. 第二種，queries[i] = [2, p, 0]。對於所有nums2[i]，將值設為nums2[i] + nums1[i] \* p。其中0 <= i < n  
3. 第三種，queries[i] = [3, 0, 0]。求nums2中所有元素的和，加入答案中  

回傳執行所有查詢後的答案陣列。  

# 解法
第一種查詢，就像是對l\~r區間內所有nums1[i]做XOR，翻兩次就等於沒翻。  
第二種查詢，把nums1整個加到nums2上面p次。  
第三種查詢，就是nums2求和。  

因為nums2只會求總和，其實不用真的維護各個索引的值。維護一個變數sm為nums2的總和，每次查詢2的時候看nums1中有幾個1，乘p後加進sm就好。  

因為python沒有位數的限制，所以可以把nums1直接看做是N位元的二進位數字，而每次翻轉區間時，只要產生l\~r對應位元為1的mask進行XOR就可以了。  
例如要產生l=1, r=3的mask：  
1. 找到第r+1個位元設為1，得到10000  
2. 將其減1，這時候0\~r的位元都是1，變成01111  
3. 同理，2^l減掉1，可以使0\~l-1的位元都變成1，也就是00001  
4. 兩者XOR，01111^00001=01110  

如果大數位移依然是O(1)，那麼查詢1時間複雜度為O(1)，查詢2為O(N)，查詢3為O(1)。空間複雜度就不知道了。  

```python
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        sm=sum(nums2)
        ans=[]
        bit=0
        
        for i,n in enumerate(nums1):
            if n:
                bit|=(1<<i)
                
        for q,l,r in queries:
            if q==1:
                mask=(1<<(r+1))-1
                mask^=(1<<l)-1
                bit^=mask
            elif q==2:
                sm+=bit.bit_count()*l
            else:
                ans.append(sm)
 
        return ans
```
