--- 
layout      : single
title       : LeetCode 2542. Maximum Subsequence Score
tags        : LeetCode Medium Array Heap Sorting HashTable
---
雙周賽96。和上題的輸入一樣都是nums1和nums2配上k，還以為我精神錯亂。  

# 題目
輸入兩個長度為N的整數陣列nums1和nums2，以及整數k。你必須選擇k個nums1的索引來組成子序列。  

若你選擇了數個索引i<sub>0</sub>, i<sub>1</sub>, ... , i<sub>k-1</sub>，則**分數**為：  
- 所有選到的nums1[i]的**總和**，乘上所有選到的nums2[i]中的**最小值**  
- 也就是(nums1[i<sub>0</sub>] + nums1[i<sub>1</sub>] +...+ nums1[i<sub>k-1</sub>]) \* min(nums2[i<sub>0</sub>] + nums2[i<sub>1</sub>] +...+ nums2[i<sub>k-1</sub>])

求**最大的可能分數**為多少。  

# 解法
陣列長度N高達10^5，要窮舉出所有子序列肯定不現實，直接不考慮。  
我們要找的是**子序列**，代表只在乎每個索引i**選或者不選**，並不在乎被選中的次數，必要時甚至可以將陣列重排序。  

根據上述，試想能不能依照某個順序遍歷陣列，以達到目標？  
既然是要乘以nums2選中的最小值，所以nums2中只要是大於最小值的索引全部都可以選擇。窮舉，盡可能找到nums1[i]較大，且nums2[i]>=最小值的索引i。  

所以可以以nums2[i]的值作為key，將nums1[i]加入對應的雜湊表中。由大到小窮舉nums[i]中出現過的數當作最小值，逐漸將可用的nums1[i]加入，並選擇最大的k個nums1[i]求總和，乘上nums2[i]最小值即為分數，最後以分數更新答案。  

現在問題只剩下要找k個最大的值。這時候使用min heap，順便維護總和，在窮舉nums2最小值的nums1[i]加入heap，若heap中超過k個值，則不斷彈出最小值。  

時間瓶頸在於nums2中出現的key值排序，若nums2中所有元素都不同，排序需要O(N log N)。雜湊表分類的時間為O(N)，heap的時間為O(N log k)。
整體時間複雜度O(N log N)。空間複雜度O(N)。  

```python
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        d=defaultdict(list)
        for a,b in zip(nums1,nums2):
            d[b].append(a)
            
        ans=0
        h=[]
        sm=0
        
        for mn in sorted(d.keys(),reverse=True):
            for x in d[mn]:
                heappush(h,x)
                sm+=x
            while len(h)>k:
                sm-=heappop(h)
            if len(h)==k:
                ans=max(ans,sm*mn)
            
        return ans
```

也可以直接把nums1和nums2綁定成數對pair，依nums2[i]的值遞減排序，直接遍歷排序好的pair，依序加入heap中。  

```python
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pair=sorted(zip(nums1,nums2),key=lambda x:-x[1])
        ans=0
        h=[]
        sm=0
        
        for val,mn in pair:
            heappush(h,val)
            sm+=val
            if len(h)>k:
                sm-=heappop(h)
            if len(h)==k:
                ans=max(ans,sm*mn)
                
        return ans
```