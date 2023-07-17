--- 
layout      : single
title       : LeetCode 2781. Length of the Longest Valid Substring
tags        : LeetCode Hard Array String HashTable Sorting TwoPointers
---
周賽354。我又搞出一個沒看到人用的解法，還真是神奇。  

# 題目
輸入字串word，還有一個字串陣列forbidden。  

如果一個字串的所有子字串都不包含在forbidden中，則稱為**有效的**。  

求word的**最長的有效子字串**長度。  

# 解法
forbidden[i]的長度最多只到10，這肯定是可以利用的地方。  

若某個子字串sub包含了被禁止的字串，則以sub為基礎擴展的其他子陣列也同樣無效。  
以範例1為例：  
> word = "cbaaaabc", forbidden = ["aaa","cb"]  
> "aaa"是無效的，因此由"aaa"擴展出去的其他子字串也是無效的  
> 包含"cbaaa", "baaa", "aaaa"等等  
> 同理，"cb"無效，因此"cdb", "cbaa"等也都無效  

在word = "aaaxxx...", forbidden = ["aaa"]這種例子中，從左邊向右配對：  
> 加入word[0]，"a"有效，繼續向右擴展  
> 加入word[1]，"aa"有效，繼續向右擴展  
> 加入word[2]，"aaa"**無效**，所有以"aaa"繼續擴展的都無效，縮減左邊界，剩"aa"  
> 加入word[3]，"aax"有效，繼續向右擴展  

結論：若字串完全包含了某個被禁止的子字串word[i,j]，則有效的子字串左邊界至少為i+1。  

枚舉每個索引i作為左邊界，檢查長度為10以內的子陣列是否在forbidden之中，若存在則將子字串區間[i,j]保存到ban之中。  
先將被禁止的區間以右邊界排序。由左到右枚舉右邊界right，並找到所有右邊界**小於等於**right的區間，並以該區間的左邊界更新**有效左邊界**left。最後[left,right]就是有效的子字串區間，以此更新答案。  
最差情況下，right剛好也被禁止，而左邊界會變成left=right+1，得到有效區間長度為0，也就是空字串。  

M為forbidden[i]長度，對於每個索引要產生M個子字串，每次O(M)，共O(N \* M^2)。  
最多會產生N\*M個被禁止的區間ban。   
瓶頸在於排序ban，時間複雜度O(N\*M log N\*M)。  
空間複雜度O(N\*M)。  

```python
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        N=len(word)
        s=set(forbidden)
        ban=[]
        for i in range(N):
            for j in range(i,min(N,i+10)):
                if word[i:j+1] in s:
                    ban.append([i,j])
                    
        ban.sort(key=itemgetter(1))
        
        ans=0
        left=0
        i=0
        for right in range(N):
            while i<len(ban) and ban[i][1]<=right:
                left=max(left,ban[i][0]+1)
                i+=1
            ans=max(ans,right-left+1)
            
        return ans
```
