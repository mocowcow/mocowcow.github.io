--- 
layout      : single
title       : LeetCode 2663. Lexicographically Smallest Beautiful String
tags        : LeetCode Hard Array String Greedy DFS
---
周賽343。關鍵點都有推出來，結果實作做不出來。  
但我沒發現輸入的s也是**美麗的**，一直在糾結**索引i進位後，從i+1開始所有字串都要變回a**，其實在最尾端字元+1的情況下，當非尾端的索引i進位時，**i+1肯定也是進位過的**。  
卡在奇怪的地方上，有點難受。  

# 題目
一個**美麗的**字串必須：  
- 由前k個小寫字母組成  
- 且不包含長度2以上的回文子陣列  

輸入一個長度n的美麗字串s，以及正整數k。  

回傳長度同為為n、且字典順序大於s的最小**美麗字串**。若無則回傳空字串。  

# 解法
一個長度n的字串若回文，則必定由n-2的回文字串組成。例如"abcba"由"bcb"擴展而成，以此類推。  
因此有兩個重點：  
1. 不可存在長度2或3的回文字串，對於每個索引i只要確保不可和i-1或i-2相同  
2. 字典順序盡可能小，則必須從最後方的字元開始增加  

先把s轉成整數字串，以ascii碼扣掉97，得到由0\~k-1組成的陣列a。  
把最後端加1，開始往前檢查，若某處等於k則不合法，需要進位。  

重點，在a[i]增加1後，除了a[i]改變，**也可能讓a[i-1]的字元改變**。以k=4為例：  
- cba加1變成cbb，bb回文  
- bcad加1變成bcba，bcb回文  
- 更經典的：dacd加1變成dada，dad和ada都回文  

若在a[i]進位改變a[i-1]時，一定要要往前檢查a[i-1]是否和a[i-2]、甚至a[i-3]造成回文；但如果是在a[0]進位，則代表沒有合法答案，回傳空字串。  
檢查a[i]時有四種情形：  
1. a[i]=k需要進位，但是i=0，不合法  
2. a[i]=k需要進位，將a[i]設為0，a[i-1]增加1，並檢查i-1  
3. 造成回文，將a[i]增加1  
4. 沒有回文，檢查i+1  

時間複雜度O(N)。最差形況下，N個位置都要檢查回文。但是回文只檢查前兩個位置，所以a[i]最多增加三次。  
空間複雜度O(N)。  

```python
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        N=len(s)
        a=[ord(c)-97 for c in s]
        i=N-1
        a[i]+=1
        
        while i<N:
            # need carry
            # check previous if any palindrome
            if a[i]==k:
                # out of bound
                if i==0:
                    return ""
                a[i-1]+=1
                a[i]=0
                i-=1
            # palindrome found
            # try next char
            elif (i>0 and a[i]==a[i-1]) or (i>1 and a[i]==a[i-2]):
                a[i]+=1
            # check next position
            else:
                i+=1
        
        return ''.join([chr(x+97) for x in a])
```

寫成類似dfs的版本。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        N=len(s)
        a=[ord(c)-97 for c in s]
        a[-1]+=1
        
        def check(i):
            if i==N:
                return
            # need carry
            if a[i]==k:
                if i==0:
                    return
                a[i]=0
                a[i-1]+=1
                check(i-1)
            # palindrome found
            elif (i>0 and a[i]==a[i-1]) or (i>1 and a[i]==a[i-2]):
                a[i]+=1
                check(i)
            else:
                check(i+1)
            
        check(N-1)

        if a[0]==k:
            return ""
            
        return ''.join([chr(x+97) for x in a])
```