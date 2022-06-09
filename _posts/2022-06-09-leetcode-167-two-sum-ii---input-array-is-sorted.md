--- 
layout      : single
title       : LeetCode 167. Two Sum II - Input Array Is Sorted
tags        : LeetCode Medium Array TwoPointers BinarySearch
---
每日題。二分搜邊界更新寫錯拿到WA，尷尬。

# 題目
輸入索引從1開始的有序整數陣列。找到兩個數字其總和為target。令這兩個數字為numbers[index1]和numbers[index2]，且1 <= index1 < index2 <= numbers.length。  
回傳長度為2的整數陣列[index1, index2]。  

每個測試保證都只有一個答案，且不可以使用同樣的元素兩次。  
空間複雜度必須為常數。  

# 解法
既然說要O(1)空間，那麼最原版的two sum解法就不可以使用了，因為雜湊表並不符合規則。  
而且既然陣列是有序的，很明顯就是使用二分搜的提示。  

列舉每個索引i作為index1，對其右方的數字做二分搜，找出target扣掉numbers[i]後還需要的值n。  
因為我們只要找到正好為n的位置，所以迴圈條件要設成l<=r，才能處理剩下一個元素的情況。  
最差會做N次二分搜，所以時間複雜度為O(N log N)。

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N=len(numbers)
        for i,n in enumerate(numbers):
            t=target-n
            l=i+1
            r=N-1
            while l<=r:
                mid=(l+r)//2
                if numbers[mid]==t:
                    return [i+1,mid+1]
                if numbers[mid]<t:
                    l=mid+1
                else:
                    r=mid-1
```

最佳的解法其實是雙指針，時間只需要O(N)。  

初始化左元素為最小的索引0，右元素為N-1，將左右兩元素加總為n：  
若n正好等於target，則以當前兩個元素為答案回傳；若n小於target，則試將n增加，所以把i向右移動；否則需要將n減少，把j向左移動。  

重點在於如何證明這個方法是正確的？  
試想以下例子：  
> numbers = [2,7,11,15], target = 9  
> i=2, j=15 總和17大於9，所以比15大的元素都不可能是j  
> i=2, j=11 總和13大於9，所以比11大的元素都不可能是j  
> i=2, j=7 總和9  

可以得到結論：  
- 若當前i+j大於target，因為陣列有序，j之後的元素都可以排除(因為使用比j大的數不可能更接近target)  
- 若當前i+j小於target，因為陣列有序，i之前的元素都可以排除(因為使用比i小的數不可能更接近target)  

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while True:
            n=numbers[i]+numbers[j]
            if n==target:
                return [i+1,j+1]
            if n<target:
                i+=1
            else:
                j-=1
```



