--- 
layout      : single
title       : LeetCode 1268. Search Suggestions System
tags        : LeetCode Medium String Trie
---
每日題。一樣又是字典樹，這次我就乖乖照著出題者想法做了。  

# 題目
輸入字串陣列products和字串searchWord。  

設計一個系統，在依序輸入searchWord的每個字元後，從products中提示最多三個產品名稱。提示的產品應該與searchWord有相同的前綴。若建議超過三項，則選擇字典順序最小的三個。

回傳輸入searchWord每個字元後所產生的建議清單。

# 解法
其實這就像是搜尋引擎的提示字，或是IDE的自動完成功能，會依照已經輸入的部分來猜測使用者想要打什麼字。  

建立空節點dummy當作字典樹的起點，每個節點用雜湊表保存可用的子節點child，以及以包含當前前綴的單字word。  
遍歷products中的每個單字w，並從dummy開始往下走，將w加入所有經過的節點。  

字典樹建立完成後，再來處理searchWord的部分。  
一樣從dummy開始出發，照著searchWord中每個字元c往下走，每走一步便篩選當前節點中最小的三個提示字，加入ans。  

因為這題只會搜尋一次，所以在搜尋過程中才依字典順序篩選也沒關係；若要查詢多次，則先遍歷整顆字典樹進行剪枝會比較合適。  

```python
class Node:
    def __init__(self):
        self.child=defaultdict(Node)
        self.word=[]

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        dummy=Node()
        for w in products:
            curr=dummy
            for c in w:
                curr=curr.child[c]
                curr.word.append(w)
        
        ans=[]
        curr=dummy
        for c in searchWord:
            curr=curr.child[c]
            ans.append(nsmallest(3,curr.word))
            
        return ans
```

翻翻其他提交答案，感覺以下這種方法是最佳解。  

一開始直接對products以字典順序遞增排序，之後就不用再處理。  
遍歷searchWord中第i個字元c，從product中篩選出長度足夠，且第i個字元同樣為c的單字，保存在t裡面。  
因為先前已經排序過，且我們也是依序遍歷，所以t中的單字同樣也是按照字典順序出現，直接將t的前三個單字加入ans，再以t更新products，重複到整個搜尋字串處理完成為止。  

```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans=[]
        
        for i,c in enumerate(searchWord):
            t=[]
            for w in products:
                if i<len(w) and w[i]==c:
                    t.append(w)
            
            products=t
            ans.append(products[:3])
            
        return ans
```

結果更神奇的解法，而且也更快。怎麼有人可以想到字串也能二分搜？  

將products排序後，以searchWord的各前綴pref來找第一個大於等於pref的位置i，從i開始數3個單字，如果確實是以pref為開頭，則加入提示字中，最後再將提示字加進ans。  

```python
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans=[]
        pref=''
        
        for c in searchWord:
            pref+=c
            i=bisect_left(products,pref)
            t=[x for x in products[i:i+3] if x.startswith(pref)]
            ans.append(t)
            
        return ans
```