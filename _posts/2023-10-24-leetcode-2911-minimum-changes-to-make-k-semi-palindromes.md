---
layout      : single
title       : LeetCode 2911. Minimum Changes to Make K Semi-palindromes
tags        : LeetCode Hard Array String DP
---
模擬周賽368。這周有事沒參加，結果剛好碰到夠難又剛好會的Q4。  
模擬賽做Q124也有200名，虧了一次上分機會。  

## 題目

輸入字串s和整數k，試將s分割成k個**子字串**，其使得所有子字串滿足**半回文**的情況下，所需的字母修改次數最小化。  

求所需的**最少**字母修改次數。  

注意：  

- **回文**指的是一個字串從左到右，與從右到左讀起來相同  
- 如果一個長度為len的字串存在一個滿足1 <= d < len、也滿足len % d = 0 的正整數d，且將所有索引以d取模後將同餘的字元連接成字串，若新連接出的所有字串都是**回文**，則稱此字串為**半回文**  
- 例如 "aa", "aba", "adbgad" 和 "abab" 是**半回文**；但 "a", "ab" 和 "abca" 不是  

## 解法

其實通過率低的主要原因，有一半是題目不清楚所致，另一半是要求很麻煩。  

分割成k個子字串、最小修改次數，很容易聯想到dp。但是何謂**子回文**就很模糊。  
首先是 1 <= d < len 這點，隱晦的說這個子字串**長度至少為2**。  
然後 len % d = 0 代表子字串長度為r\*d，有d個新連接出的字串長度都是r。  

定義dp(i,k)：將s[i,N-1]分割成k個**半回文**子字串所需要的**最少修改次數**。  
轉移方程式：dp(i,k) = min( dp(j+1,k-1) + cost(i,j) FOR ALL i<j<N )，其中cost(i,j)是s[i,j]滿足半回文的最小修改次數。  
base cases：當i=N且k=0時，子字串分割結束，回傳0；若只出現i=N或k=0其一，代表分割不合法，回傳inf。  

共有N\*k種狀態，各需要轉移N次。  
對於i相同，但k不同的情況下，他們共用到數個相同的cost(i,j)，所以cost也可以做記憶化。  

cost(i,j)要將s[i,j]視為一個獨立的字串，其長度size=j-i+1，找出可整除size的d，以餘數將字元串接，最後判斷回文修改次數。  
對於每個合法的d，都需要遍歷這個長度size的字串一次，每個d複雜度O(N)。  
每個子字串平均下來有log N個合法的d。  

時間複雜度O(N^2\*k\*log N)。  
空間複雜度O(N^2)，瓶頸為cost的狀態數。  

```python
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        N=len(s)
        
        @cache
        def cost(i,j):
            size=j-i+1
            mn_swap=inf
            for d in range(1,size): # d is number of semi-pal
                if size%d!=0:
                    continue
                semi_size=size//d
                cnt=0
                for start in range(d):
                    cs=[]
                    for ii in range(i+start,j+1,d):
                        cs.append(s[ii])
                    for ii in range(semi_size//2):
                        if cs[ii]!=cs[semi_size-1-ii]:
                            cnt+=1
                mn_swap=min(mn_swap,cnt)
            return mn_swap
        
        @cache
        def dp(i,k):
            if i==N and k==0:
                return 0
            if i==N or k==0:
                return inf
            res=inf
            for j in range(i+1,N):
                res=min(res,dp(j+1,k-1)+cost(i,j))
            return res
        
        return dp(0,k)
```

同樣長度的子字串，合法的d都是一樣的，可以先預處理所有長度所包含的有效d。  

預處理過之後，每次計算cost就可以直接拿出有效的d。  
再次複習一下，d一定能夠整除大小為size的子字串，最後一步的位置會停在[size-d, size-d+1, ..., size-d+(d-1)]。  
所以子字串的右邊界會是size-d+offset，其中0<=offset<d。  

```python
MX=200
div=[[] for _ in range(MX+1)]
for i in range(1,MX+1):
    for j in range(i*2,MX+1,i):
        div[j].append(i)

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        N=len(s)
        
        @cache
        def cost(i,j):
            size=j-i+1
            mn_swap=inf
            for d in div[size]:
                cnt=0
                for start in range(d):
                    left=i+start
                    right=j+1-d+start
                    while left<right:
                        cnt+=s[left]!=s[right]
                        left,right=left+d,right-d
                mn_swap=min(mn_swap,cnt)
            return mn_swap
        
        @cache
        def dp(i,k):
            if i==N and k==0:
                return 0
            if i==N or k==0:
                return inf
            res=inf
            for j in range(i+1,N):
                res=min(res,dp(j+1,k-1)+cost(i,j))
            return res
        
        return dp(0,k)
```
