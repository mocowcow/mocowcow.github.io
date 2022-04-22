---
layout      : single
title       : LeetCode 1818. Minimum Absolute Sum Difference
tags 		: LeetCode Medium Array BinarySearch Sorting
---
二分搜學習計畫。好多天都是函數型的二分搜，終於來點不一樣的。

# 題目
輸入兩個長度都為N的陣列nums1和nums2。  
絕對差和指的是nums1和nums2所有數字的差，其絕對值的總和。  
你可以將nums1中的任一數字，替換成另一個也在nums1中出現過的數字。求替換後的**最小絕對差和**為多少，答案可能很大，模10^9+7後再回傳。

# 解法
想要把絕對差和最小化，要優先選擇絕對值較大的索引i做替換，將nums1[i]和nums2[i]變成相同值，進而將i的絕對值變為0。  
但是我們只能改變nums1的值，而且新值還要有在nums1出現過，這樣變成每個位置i都有可能使答案最佳化了。  

先把nums1的數字全部裝進雜湊表中去重複後排序，存為s1，供之後二分搜使用。  
ds為原本的絕對差和，現在試著找出替換某個位置後可以省下最多的絕對差save。
對每個位置i的數字n1, n2計算出原本的絕對差diff，再以n2的值在s1中找最接近的兩個數，分別判斷這兩個新的值能夠將原本的絕對差減少多少。  
最後回傳**原本的絕對差和**-**可以省下的最大絕對差**就是答案。

```python
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1==nums2:
            return 0
        
        MOD=10**9+7
        N=len(nums1)
        s1=sorted(set(nums1))
        M=len(s1)
        ds=0
        save=-math.inf
        for n1,n2 in zip(nums1,nums2):
            diff=abs(n1-n2)
            ds=(ds+diff)%MOD
            idx=bisect_left(s1,n2)
            if idx<M:
                save=max(save,diff-(s1[idx]-n2))
            if idx>0:
                save=max(save,diff-(n2-s1[idx-1]))
           
        return (ds-save)%MOD
```

