--- 
layout      : single
title       : LeetCode 658. Find K Closest Elements
tags        : LeetCode Medium Array BinarySearch TwoPointers Sorting
---
每日題。以前寫的時候沒有發現有O(N)甚至O(log N)解，今天真是賺到了。  

# 題目
輸入一個排序過的整數陣列arr，以及兩個整數k和x。  
求陣列中k個和x最靠近的整數，並依遞增排序。  

若滿足以下條件，則稱a比b更靠近 x：  
- |a - x| < |b - x|  
- 或是 |a - x| == |b - x|且a < b

# 解法
既然輸入已經排序好了，第一個想到當然是二分搜。  
先找到最靠近x的索引，並使用雙指針依照規定的方式將整數一一加入ans中，最後排序ans後回傳。  

時間複雜度包含二分搜找索引O(log N)，雙指針部分O(k)，排序答案O(k log k)，而k可能等於N，所以整體複雜度應該是O(N log N)。空間複雜度O(k)。  

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N=len(arr)
        right=bisect_left(arr,x)
        left=right-1
        ans=[]
        
        while len(ans)<k:
            diff1=abs(x-arr[left]) if left>=0 else inf
            diff2=abs(x-arr[right]) if right<N else inf
            if diff1<=diff2:
                ans.append(arr[left])
                left-=1
            else:
                ans.append(arr[right])
                right+=1
                
        return sorted(ans)
```

反正既然都要排序了，不如多排幾次，反正複雜度差不多，還比較好寫。這個方法同樣適用於未排序的輸入。  
先把原陣列轉換成[標準差,索引,元素]的格式，排序後可以保證符合題目的規範，抽取出前k個最靠近的結果在排序一次後就是答案。  

時間複雜度O(N log N + k log k)，空間複雜度O(N)。  

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans=[[abs(x-n),i,n] for i,n in enumerate(arr)]
        return sorted([x[2] for x in sorted(ans)[:k]])
```

回想最初的雙指針作法，是從中心點開始往左右找k個最近的元素。  
那如果從左右開始刪除N-k個最遠的元素不也是同樣道理？  

左邊界left初始為0，右邊界right初始為N-1。如果left小，就踢掉右邊的；否則踢掉左邊的。重複以上動作直到剩下k個元素為止。  

時間複雜度O(N)，空間複雜度O(1)。  

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N=len(arr)
        left=0
        right=N-1
        
        while right-left+1>k:
            if x-arr[left]<=arr[right]-x:
                right-=1
            else:
                left+=1
        
        return arr[left:left+k]
```