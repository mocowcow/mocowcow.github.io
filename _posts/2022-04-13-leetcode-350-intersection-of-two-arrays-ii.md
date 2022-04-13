---
layout      : single
title       : LeetCode 350. Intersection of Two Arrays II
tags 		: LeetCode Easy HashTable Array TwoPointers Sorting
---
二分搜學習計畫出現的。看完follow up還是覺得跟二分搜沒有什麼關係。

# 題目
輸入兩個數列nums1和nums2，找出他們的交集元素，若一個數字在兩陣列都出現n次，則要輸出n次。以任何順序輸出都可以。

# 解法
最直接的解法，因為數字範圍只有在0\~1000，直接開兩個1001的陣列計數，最後遍歷0\~1000對個數字輸出共通出現次數即可。

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1=[0]*1001
        c2=[0]*1001
        
        for n in nums1:
            c1[n]+=1
        for n in nums2:
            c2[n]+=1
            
        ans=[]
        for i in range(1001):
            if c1[i] and c2[i]:
                ans+=[i]*min(c1[i],c2[i])
        
        return ans
```

改成雜湊表。  

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1=Counter(nums1)
        c2=Counter(nums2)
        ans=[]
        
        for k in c1:
            ans+=[k]*min(c1[k],c2[k])
        return ans
```

follow up 1：如果輸入的數列已經排序好，要如何改進演算法？  
答1：使用雙指標i, j，如果n1較小則i往後移；n2較小則j往後移；兩者相同表示交集，加入ans後兩者都向後移。  

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #假設已經排序好
        nums1.sort()
        nums2.sort()
        
        M,N=len(nums1),len(nums2)
        i=j=0
        ans=[]
        while i<M and j<N:
            if nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
                j+=1
        
        return ans

```

follow up 2：如果nums1長度比nums2小，哪種演算法更好？  
答2：若長度分別為M, N，只把nums1裝入雜湊表計數，遍歷nums2，若對應次數有剩餘再加入ans，時間為O(M+N)，空間O(M)。  

follow up 3：如果nums2很大而且存在硬碟上，記憶體不夠讓你全部讀入，要怎麼處理？  
答3：如果nums1裝得下的話，一樣先把nums1裝入雜湊表計數，分次讀取nums2找交集；若兩個都裝不下，則使用外部排序，分別讀入部分的區塊，成為X個排序好的部分，最後兩兩合併，得到兩個排序好的資料，再以雙指標方法處理。時間為排序O(M log M)+O(N log N)+找交集O(M+N)，空間為(排序切割區塊大小)。