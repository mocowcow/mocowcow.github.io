---
layout      : single
title       : LeetCode 991. Broken Calculator
tags 		: LeetCode Medium Math Greedy
---
每日題。總感覺似曾相似，原來是2139. Minimum Moves to Reach Target Score。

# 題目
有個壞掉的計算機，只能進行兩種動作：  
- 將當前值-1  
- 將當前值*2  

由初始數startValue開始，最少需要幾次動作可以變成target。

# 解法
初始值有可能比target更大，也可能更小。  
如果初始值大於target則只剩下-1這個動作可以用，簡單計算差值就是答案；若小於target，則試將target減少至小於startValue為止。若target為奇數就只能先
+1湊成偶數，而偶數時就可以除2，每次都要計算動作回數。最後(將target調整到比初始值的行動次數)+(初始值-調整後的target)就是答案。  

```python
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
            cnt=0
            while target>startValue:
                if target%2:
                    target+=1
                else:
                    target//=2
                cnt+=1
                
            return cnt+startValue-target
```

