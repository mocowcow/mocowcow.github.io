--- 
layout      : single
title       : LeetCode 2791. Count Paths That Can Form a Palindrome in a Tree
tags        : LeetCode Hard Array String Tree DFS BitManipulation Bitmask HashTable
---
周賽355。最重要的問題轉換都有做出來，只差在樹的遍歷方向不對，太可惜了。  

# 題目
輸入一棵有n個節點，編號由0 \~ n-1，且根節點為0的樹(無向無環連通圖)。  
有個長度同為n的陣列parent，其中parent[i]代表節點i的父節點。因為節點0是根，所以parent[0]為-1。  

還有一個長度同為n的字串s，其中s[i]是節點i與其父節點連接邊上的字元。可以無視s[0]。  

求有多少滿足u < v的節點對(u, v)，在兩者間的路徑上，包含的字元能夠被重組成**回文字串**。  

# 解法
首先想想回文的條件：  
1. 最多只能有一個字元的出現次數是奇數  
2. 其他的字元出現次數都是偶數  

也就是說，只要某個字元出現偶數次，其實等價於沒有出現過，不會影響是否回文。  

加上題目保證s[i]只由小寫字母組成，最多只有26種，可以用bitmask表示其出現次數的奇偶性。  
所以就是用bitmask搭配XOR運算相消的特性，以1位元來記錄哪些字元的出現次數是奇數。  
只有mask為0，或只有一個1位元時是回文字串。  

比賽時，**到目前為止**的思路都是正確的，結果我搞了自下而上的dfs。每次更新一個邊，最差情況下需要更新2^26種mask，理所當然的TLE了。紀錄一下當時的錯誤方法。  

定義dfs(i)：以i為根節點的子樹的所有路徑。       
維護雜湊表d，紀錄i的所有路徑。然後所有子節點j，將所有路徑連接s[j]後，順便找找看哪條出現過的路徑可以組成回文。  
需要注意的是：只有一條從i出發的路徑也可以達成回文，不一定要兩條。所以連接s[j]後要馬上檢查是否回文。  

反正光是將每個路徑加上s[j]就已經高達O(2^26)，更不用說枚舉兩條路徑需要O(2^52)，然後外面再套一個O(N)，絕對TLE。  

```python
class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        N=len(parent)
        g=[[] for _ in range(N)]
        ans=0
        
        for i in range(1,N):
            g[parent[i]].append(i)
            
        def dfs(i):
            nonlocal ans
            d=Counter()
            for j in g[i]:
                char=1<<(ord(s[j])-97)
                d2=Counter()
                d2[char]=1
                
                # concact new edge, O(2^26)
                for mask,v in dfs(j).items():
                    merge=mask^char
                    if merge==0 or merge.bit_count()==1:
                        ans+=v
                    d2[merge]+=v
                
                # match two path, O(2^26) * O(2^26)
                for mask1,v1 in d.items():  
                    for mask2,v2 in d2.items(): 
                        XOR=mask1^mask2
                        if XOR==0 or XOR.bit_count()==1:
                            ans+=v1*v2
                            
                # update counter, O(2^26)
                d+=d2
            return d
            
        dfs(0)
        
        return ans+N-1
```

正確的方法是自上而下，維護根節點0到當前節點i的路徑mask，並透過mask和先前出現過的所有路徑匹配。  

假設目前的路徑是mask，那麼只能和以下的路徑XOR形成回文：  
1. 同樣是mask，所有字元出現次數都變成偶數  
2. mask把其中一個0位元變成1，只有一個字元是奇數次  
3. mask把其中一個1位元變成0，只有一個字元是奇數次  

對於第k個位元來說，情況2和3是互斥的，只可能擇一出現，而且剛好都是對k做XOR。  
匹配完之後再把當前路徑mask的計數+1，繼續遞迴處理子樹。  

總共只有26種字元，所以每個節點只要枚舉26次，可以視為常數時間。  

時間複雜度O(N)，其中N為s長度。  
空間複雜度O(N)。  

```python
class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        N=len(parent)
        g=[[] for _ in range(N)]
        ans=0
        d=Counter()
        
        for i in range(1,N):
            g[parent[i]].append(i)
            
        def dfs(i,mask):
            nonlocal ans
            # mask ^ mask = 0
            ans+=d[mask]
            
            # mask ^ othermask = power of 2
            for k in range(26):
                ans+=d[mask^(1<<k)]
                
            # extend path
            d[mask]+=1
            for j in g[i]:
                char=1<<(ord(s[j])-97)
                dfs(j,mask^char)
        
        dfs(0,0)
        
        return ans
```