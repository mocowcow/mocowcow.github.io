---
layout      : single
title       : LeetCode 2227. Encrypt and Decrypt Strings
tags 		: LeetCode Hard HashTable String Trie Design
---
周賽287。第二次全通，雖然MLE、TLE、WA各一次。
開始做的時候就看到AC人數高得誇張，想說暴力法該不會能過，結果不行。後來改成字典樹剪枝才AC。  
後來聽說C++可以用暴力法直接過，感覺個語言的執行限制不是很公平。  

# 題目
設計一個類別Encrypter，可以將字串加密，或是逆推加密字串還原的可能性有幾種。  
包含以下功能：  
1. 建構子  
2. string encrypt(string word1)，將word1加密後回傳  
3. int decrypt(String word2)，依規則逆推word2有幾種可能  

建構子會接收三個陣列，前兩個陣列keys和values長度相同，代表keys[i]加密後會轉成values[i]。keys為**不重複**的單一字元，而values為長度2的字串。  
第三個陣列dictionary代表解密後的合法結果，若word2解密後存在於dictionary中，則可能性+1。  

encrypt加密方式：將word1每個c在keys中找到位置i，使keys[i]==c，並將c換成values[i]。  

decrypt解密方式：將word2每次讀入長度2的子字串s，找到所有i使values[i]==s，並將s換成keys[i]。  
有多個i時可以選擇其中任一個，例：  
> keys=['a','b'] , values=['xx','xx']  
> decrypt('xxxx')有可能是'aa'、'ab'、'ba'或是'bb'  

# 解法
雜湊表en，建立加密時的單向映射。雜湊表de，保存解密時逆推的所有可能字元。  
root為字典樹的根節點，把dictionary所有字串加入，並在各個尾節點標記end。  

加密時就跟描述一樣，不贅述。  
解密時維護一個佇列做BFS，從根節點開始，每次以長度2的字串s到de找還原可能，試著前往下一個節點。若順利走完整個字串，且當前節點有標記end，則可能性+1。執行時間6791ms。

```python
class Node:
    def __init__(self):
        self.child=defaultdict(Node)
        self.isWord=False

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.en=dict()
        self.de=defaultdict(list)
        self.root=Node()
        
        for k,v in zip(keys,values):
            self.en[k]=v
            self.de[v].append(k)
                               
        for w in dictionary:
            curr=self.root
            for c in w:
                curr=curr.child[c]
            curr.isWord=True

    def encrypt(self, word1: str) -> str:
        en=[]
        for c in word1:
            en.append(self.en[c])
        return ''.join(en)

    def decrypt(self, word2: str) -> int:
        N=len(word2)
        q=deque()
        q.append([self.root,0])
        cnt=0
        while q:
            curr,i=q.popleft()
            if i>=N:
                if curr.isWord:
                    cnt+=1
                continue
            for nextChar in self.de[word2[i:i+2]]:
                if nextChar in curr.child:
                    q.append([curr.child[nextChar],i+2])
        return cnt

```

腦筋急轉彎，聰明人的解法：直接對dictionary加密，看會變成什麼樣子，直接計數，解密的時候看看有幾種來源就可以了。  
行數少，執行快，只要446ms。

```python
class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.possible=Counter()
        self.en=dict()

        for k,v in zip(keys,values):
            self.en[k]=v
            
        for w in dictionary:
            self.possible[self.encrypt(w)]+=1

    def encrypt(self, word1: str) -> str:
        en=[]
        for c in word1:
            en.append(self.en[c])
        return ''.join(en)

    def decrypt(self, word2: str) -> int:
        return self.possible[word2]
```