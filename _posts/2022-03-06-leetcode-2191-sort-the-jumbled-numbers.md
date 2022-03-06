---
layout      : single
title       : LeetCode 2191. Sort the Jumbled Numbers
tags 		: LeetCode Medium Array Sort
---
雙周賽73。  
昨天陪狗在醫院耗了大半天，明明在外都很正常，回家就變得神經質。至少有吃點東西了。  

回顧最近的文章，一堆高重複性的免洗題，總覺得不合當初開始寫文的動機。
我要的是記錄下特別有趣、有價值的題目，而不是每天的刷題流水帳。

# 題目
陣列mapping表示數字i實際上的值為mapping[i]，試把整數陣列nums依照實際的數值大小做遞增排序。

# 解法
這題剛好很適合python的內建排序，只需要寫一個轉換函數f作為鍵值，就可以輕鬆排好。

```python
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        m = {str(i): str(x) for i, x in enumerate(mapping)}

        def f(n):
            s = []
            for c in str(n):
                s.append(m[c])
            return int(''.join(s))
        nums.sort(key=f)
        return nums

```

若是用java的話，可能要以[原本數值,對映值]作為數對儲存，建立新的comparator以x[1]和y[1]比大小。  
排序完再單獨把各數列的原本數值抽出來回傳。