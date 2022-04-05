---
layout      : single
title       : LeetCode 2223. Sum of Scores of Built Strings
tags 		: LeetCode Hard String 
---
雙周賽75。  
題目要的是longest common prefix，總覺得和KMP的longest suffix prefix有八成像，但是沒有成功做出來。後來才知道出題者想考z-function。  

# 題目
輸入長度為N的字串s。  
有N個子字串，長度分別為1~N，由s的後方開始往前數。  
例如：  
> s = 'abaca'  
> s1 = 'a'  
> s2 = 'ca'  
> s3 = 'aca'  
> s4 = 'baca'  
> s5 = 'abaca'  

子字串i與s的**最長共通前綴**即為子字串i的分數，求所有子字串的分數總和為多少。

# 解法
真的奇怪，z-function這東西我連聽都沒聽過，竟然一堆人能過。  

定義陣列z[i]為s與子陣列s[i:N]的LCP，由z[1]開始往右計算。計算z[i]時，藉由重複利用先前計算過的z[j]來減少比對次數，進而將複雜度降至O(N)。  
z-box為先前配對過的共通LCP位置。索引L, R為z-box的範圍，z-box的位置越靠右越好。  

每次計算z[i]時有三種情況：  
1. z-box在i的左邊，沒有重疊到，沒有先前的結果可以利用，只能自己逐一比對  
2. j+z[j]小於z[L]，代表重複利用j的部分被z-box完全包住，已經都處理過了，所以z[i]=z[j]  
3. 自己和z-box同樣長或是更長，重複利用部分，剩下的自己比對  

經過上述處理，z[i]的值可能有所變化，而z[i]正好是s的開始比對位置，i+z[i]，則為子字串的開始比對位置，若兩字元相同則向後移。  
位置停止後，如果子字串的比對位置i+z[i]比當前的z-box位置更加靠右，則更新x-box位置。  
因為z-algorithm通常默認z[0]為0，為了符合題意，手動把z[0]設成字串長度N，再回傳z加總。  

```python
class Solution:
    def sumScores(self, s: str) -> int:
        N = len(s)
        z = [0]*N
        z[0] = N
        L = R = 0 # right most z-box 

        for i in range(1, N):
            if i > R:  # not covered by z-box
                pass # z[i] = 0
            else: 
                j = i-L
                if j+z[j] < z[L]: # fully covered
                    z[i] = z[j]
                else: # partial covered
                    z[i] = R-i+1

            while i+z[i] < N and s[z[i]] == s[i+z[i]]:  # remaining substring
                z[i] += 1
            if i+z[i]-1 > R:  # R out of prev z-box, update R
                L = i
                R = i+z[i]-1
        
        return sum(z)
```

參考資料：
http://wiki.csie.ncku.edu.tw/acm/course/String_Matching#z-algorithm  
https://web.ntnu.edu.tw/~algo/Substring.html#10  
https://codeforces.com/blog/entry/3107  
https://oi-wiki.org/string/z-func  
https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm  
