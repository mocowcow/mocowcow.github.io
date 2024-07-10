---
layout      : single
title       : LeetCode 3211. Generate Binary Strings Without Adjacent Zeros
tags        : LeetCode Medium Array String Backtracking
---
周賽 405。好像很久沒出現回溯題。  

## 題目

輸入正整數 n。  

若一個二進位字串 x 中所有長度為 2 的子字串都至少包含一個 "1"，則稱為**有效的**。  

求所有長度為 n 的有效二進位字串，並以任意順序回傳。  

## 解法

回溯法，暴力生成所有可能的二進位字串，枚舉每個位置選 0 或是 1。  
達到長度 N 時，檢查確定有效後加入答案。  

時間複雜度 O(2^n \* n)。  
空間複雜度 O(n)，答案空間不計入。  

```python
class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        curr = []

        def bt():
            if len(curr) == n:
                # check
                if all("1" in [a, b] for a, b in pairwise(curr)):
                    ans.append("".join(curr))
                return 

            for c in "01":
                curr.append(c)
                bt()
                curr.pop()

        bt()

        return ans
```

與其說長度為 2 的子字串要有 "1"，不如說不允許兩個 "0" 相連。  
直接在生成子字串的時候剪枝，就不用在最後重新檢查浪費時間。  

時間複雜度 O(2^n)。  
空間複雜度 O(n)。  

```python
class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        curr = []

        def bt():
            if len(curr) == n:
                ans.append("".join(curr))
                return 
            if not curr or curr[-1] == "1":
                curr.append("0")
                bt()
                curr.pop()
            curr.append("1")
            bt()
            curr.pop()

        bt()

        return ans
```
