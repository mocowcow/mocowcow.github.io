--- 
layout      : single
title       : LeetCode 936. Stamping The Sequence
tags        : LeetCode Hard String Greedy
---
每日題。這鬼東西還真不好想要怎麼做，看了別人題解還是一知半解。  

# 題目
輸入兩個字串stamp和target。最初，有個長度為target.length的字串s，由"?"字元組成。  
每次動作，你可以將stamp蓋在s[i]上，並將s中的對應位置的變成stamp的字母。  

例如stamp = "abc" 和 target = "abcba"，s初始為"?????"最。這時你可以：  
- 在s[0]蓋章，使s變成"abc??"  
- 在s[1]蓋章，使s變成"?abc?"  
- 在s[2]蓋章，使s變成"??abc"  

注意，stamp必須完全包含在s的邊內中才能可以蓋章。  

回傳一個陣列，代表依序蓋章的每個位置。如果我們無法在10\*target.length次蓋章內使得s成為target，則回傳空陣列。  

# 解法
很多題解都說要逆向操作，透過**還原蓋章**，把taget字串變回最初的全問號。  

若target的長度為N，而stmap長度為M，最多只有N-M+1個位置可以蓋章。  
設置一個迴圈，遍歷所有索引位置i，檢查是否有**非問號**的字元需要還原，直到沒有地方可以修改為止。若每個索引i至少存在一個字元可還原，則將該索引i加入答案中。  

最後檢查target是否已經全部為問號，若是則將ans反轉，得到正確的蓋章順序；否則回傳空陣列。  

其實我不太明白題目限制的10\*target.length次蓋章有什麼含意，理論上最大的蓋章次數應該就是N-M+1次才對，例如：  
> stamp = "abc", target = "aaaabc"  
> 還原順序為[3,2,1,0]  
> "aaaabc"
> "aaa**???**"  
> "aa**?**???"  
> "a**?**????"  
> "**?**?????"  
> 反轉後得到蓋章順序為[0,1,2,3]  

每次迴圈檢查蓋章位置複雜度為O((N-M)*M)，而最多蓋章N-M+1次，整體複雜度應該是O(M\*(N-M)^2)才對，不知道官方題解為啥說是O(N\*(N-M))。  

```python
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        M=len(stamp)
        N=len(target)
        pat='?'*M
        final='?'*N
        ans=[]
        
        def match(s):
            ok=False
            for c1,c2 in zip(s,stamp):
                if c1=='?':continue
                if c1!=c2:return False
                ok=True
            return ok
        
        while True:
            mod=False
            for i in range(N-M+1):
                sub=target[i:i+M]
                if match(sub):
                    mod=True
                    ans.append(i)
                    target=target[:i]+pat+target[i+M:]
            if not mod:break
                
        if target==final:
            return reversed(ans)
        else:
            return []
```
