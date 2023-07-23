--- 
layout      : single
title       : LeetCode 2785. Sort Vowels in a String
tags        : LeetCode Medium Array String Sorting Stack Simulation
---
雙周賽109。

# 題目
輸入字串s，依照以下條件將s重排列成t：  
- 每個子音維持原來的位置。也就是說，s[i]和t[i]必須相同  
- 母音必須依照ASCII值**非遞減**排序。也就是說，對於滿足0 <= i < j < s.length的兩個母音s[i]和s[j]，重排列後t[i]的ASCII值不可大於t[j]  

回傳重排列後的字串t。  

# 解法
需要注意的是字母包含大小寫，而大小字母的ASCII小於小寫字母。  

因為只需要將母音重新排列，所以將母音單獨抽出來處理，排序後再依序塞回去s中的母音位置。  

時間複雜度O(N log N)。  
空間複雜度O(N)。  

```python
class Solution:
    def sortVowels(self, s: str) -> str:
        vowel=set("aeiouAEIOU")
        vs=[c for c in s if c in vowel]
        vs.sort()
        
        i=0
        ans=[]
        for c in s:
            if c in vowel:
                ans.append(vs[i])
                i+=1
            else:
                ans.append(c)
                
        return "".join(ans)
```

如果將母音以逆序排序，當作stack使用的話可以寫得更方便一些。  

```python
class Solution:
    def sortVowels(self, s: str) -> str:
        vowel=set("aeiouAEIOU")
        vs=[c for c in s if c in vowel]

        ans=[vs.pop() if c in vowel else c for c in s]
                
        return "".join(ans)
```