---
layout      : single
title       : LeetCode 2840. Check if Strings Can be Made Equal With Operations II
tags        : LeetCode Medium String HashTable Sorting
---
雙周賽112。跟上一題基本一樣，可惜我沒發現可以複製貼上。  

## 題目

輸入字串s1和s2，兩者長度都是4，只由小寫英文字母組成。  

你可以對兩者執行以下操作任意次  

- 選擇兩個索引i和j，滿足 j - i = 2。然後將索引上的字元交換  

若可以使得s1和s2相等，則回傳true，否則回傳false。  

## 解法

跟[2839. check if strings can be made equal with operations i]({% post_url 2023-09-03-leetcode-2839-check-if-strings-can-be-made-equal-with-operations-i %})一樣，只是長度從4變成N，改一下就好。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:

        for i in range(2): # odd/even
            d=Counter()
            for j in range(i,len(s1),2): 
                d[s1[j]]+=1
                d[s2[j]]-=1
            for v in d.values():
                if v!=0:
                    return False

        return True
```

排序解法一樣可以，但字串長度不再是常數，時間複雜度會變成O(N log N)。  
