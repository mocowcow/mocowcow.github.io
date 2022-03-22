---
layout      : single
title       : LeetCode 1663. Smallest String With A Given Numeric Value
tags 		: LeetCode Medium String Greedy
---
每日題。

# 題目
令字母數值a=1、b=2...z=26，求長度為n且數值總和為k的字串，此字串必須是**最小字典順序**。

# 解法
說要最小字典順序，那就要盡可能在左方塞入較小的字元，且必須顧及剩下的k值是否能全部用完。  
先從最小值curr=1開始，若加入curr後，還剩下n-1個字元和k-curr可用。  
若(k-curr)/(n-1)>26則表示無法用完所有k，所以該curr值必須更大，才能符合答案；若合法，將curr值轉成對應字元加入答案中。  
上述動作一直重複到n=1為止，因為這時候若再進入迴圈會出現分母為0錯誤。手動將剩下的k轉成字元加入即可。

```python
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans=[]
        curr=1
        while n>1:
            if (k-curr)/(n-1)>26:
                curr+=1
                continue
            ans.append(chr(96+curr))
            k-=curr
            n-=1
            
        ans.append(chr(96+k))
            
        return ''.join(ans)
```

預先建立字元對照表，時間從1026ms降到756ms。

```python
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        alp=[chr(96+i) for i in range(0,27)]
        ans=[]
        curr=1
        while n>1:
            if (k-curr)/(n-1)>26:
                curr+=1
                continue
            ans.append(alp[curr])
            k-=curr
            n-=1
            
        ans.append(alp[k])
            
        return ''.join(ans)
```

