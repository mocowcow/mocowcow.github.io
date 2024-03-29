--- 
layout      : single
title       : LeetCode 2683. Neighboring Bitwise XOR
tags        : LeetCode Medium Array BitManipulation Simulation Math
---
周賽345。差點被這題搞死，拖到最後才解出來。  

# 題目
一個大小為n的陣列derived，這是由大小同為n的**二進位陣列**original透過XOR構造而來。  

對於derived中的每個索引i：  
- 如果i=n-1，則derived[i]=original[i] XOR oringinal[0]  
- 否則derived[i]=original[i] XOR oringinal[i+1]  

輸入陣列derived，並判斷是否存在**合法的二進位陣列**original能夠構造出derived。  
若存在則回傳true，否則回傳false。  

# 解法
以下簡稱derived為d，original為a。  
d[i]是由a[i] ^ a[(i+1)%N]所構成，要判斷d是存在對應的a。  

因為XOR相消的特性：  
- d[i] = a[i] ^ a[i+1]  
- 等於 d[i] ^ a[i+1] = a[i] ^ a[i+1] ^ a[i+1]  
- 相消得到 d[i] ^ a[i+1] = a[i]  

只要任意一個a[i]的值確定，就可以透過公式推導出a[i-1]，最後推出整個a陣列。  

研究一下，d[i]所對應的a[i]可能為何？  
若d[i] = 1，則a[i]和a[i+1]有兩種可能：  
- [1, 0]或是[0, 1]  
若d[i] = 0，則a[i]和a[i+1]有兩種可能：  
- [1, 1]或是[0, 0]  

發現不管d[i]為何，a[i]都有可能是0或是1。  

反正只有兩種可能，那麼兩種都代進去，只要其中一種合法，答案就是true。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        d=derived
        N=len(d)
        
        def ok(x):
            a=[0]*N # a[i] = d[i] ^ a[i+1]
            a[-1]=x # 假設a的最後一個元素是x
            for i in reversed(range(N-1)): # 然後從倒數第二個開始往回推
                a[i]=d[i]^a[i+1]
            # 除了最後一個位置a[N-1]以外都是推出來的，一定合法
            # 最後只要檢查d[N-1]是否合法
            return d[-1]==a[-1]^a[0] 
        
        for x in [0,1]:
            if ok(x):
                return True
            
        return False
```

看了其他神人的解答，幾乎都是依照公式來推出規律。  

根據題目定義：d[i] = a[i] ^ d[i+1]  
假設a長度為3，則：  
> b[0] = a[0] ^ a[1]  
> b[1] = a[1] ^ a[2]  
> b[2] = a[2] ^ a[3]  

可見a之中的每個元素都在b出現了兩次。  
利用這個特性，若將b中所有元素做XOR，相當於a中的**每個元素都XOR兩次**，結果必定等於0。  

更嚴謹的證明，則要繼續從剛才的a[i] = d[i] ^ a[i+1]繼續推導。  
同樣假設a長度為3：  
> a[0] = b[0] ^ a[1]  
> a[1] = b[1] ^ a[2]  
> a[2] = b[2] ^ a[0]  
> 將a[0]中的a[1]展開  
> a[0] = b[0] ^ b[1] ^ a[2]  
> 再將a[2]展開  
> a[0] = b[0] ^ b[1] ^ b[2] ^ a[0]  
> 兩邊同時XOR一次a[0]  
> 0 = b[0] ^ b[1] ^ b[2]

得證，b中所有元素做XOR等於0。  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        '''
        a = [a1, a2, a3]
        b = [a1^a2, a2^a3, a3^a1]
        XOR b = a1^a2 ^ a2^a3 ^ a3^a1 = 0
        '''
        XOR=0
        for x in derived:
            XOR^=x
            
        return XOR==0
```