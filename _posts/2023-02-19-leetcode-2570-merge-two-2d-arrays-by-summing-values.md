--- 
layout      : single
title       : LeetCode 2570. Merge Two 2D Arrays by Summing Values
tags        : LeetCode Easy Array HashTable Sorting TwoPointers
---
周賽333。

# 題目
輸入二維整數陣列nums1和nums2。  
- nums1[i] = [id<sub>i</sub>, val<sub>i</sub>]，代表其id和val  
- nums2[i] = [id<sub>i</sub>, val<sub>i</sub>]，代表其id和val  

兩個陣列所包含的id都是**唯一值**，且依照id**遞增**排序。  

依照以下規則將陣列合併：  
- 只有在nums1或nums2出現過的id才能在答案中出現  
- 每個id只能出現一次，且其val為兩陣列中同id所對應的val加總。若另一個陣列不包含此id，則val視為0  

回傳合併後的陣列。答案必須依照id遞增排序。  

# 解法
懶人法，直接將兩個陣列裝到同一個雜湊表中，輸出kv對後重新排序。  

時間複雜度O(M+N log M+N)。空間複雜度O(M+N)。  

```python
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d=Counter()
        
        for id,val in nums1:
            d[id]+=val

        for id,val in nums2:
            d[id]+=val
        
        return sorted(d.items(),key=itemgetter(0))
```

最佳解應該是雙指針，類似合併linked list的方法，每次加入較小的id；若id相同則合併val。  

時間複雜度O(M+N)。輸出陣列不計，空間複雜度O(1)。  

```python
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        M,N=len(nums1),len(nums2)
        i=j=0
        ans=[]

        while i<M and j<N:
            if nums1[i][0]<nums2[j][0]:
                ans.append(nums1[i])
                i+=1
            elif nums1[i][0]>nums2[j][0]:
                ans.append(nums2[j])
                j+=1
            else:
                ans.append(nums1[i])
                ans[-1][1]+=nums2[j][1]
                i+=1
                j+=1
                
        while i<M:
            ans.append(nums1[i])
            i+=1
        
        while j<N:
            ans.append(nums2[j])
            j+=1
        
        return ans
```