--- 
layout      : single
title       : LeetCode 89. Gray Code
tags        : LeetCode Medium BitManipulation Math
---
今天每日題的原題，當初碰到也覺得很奇妙，比較需要特別記住這個東西。  

# 題目
n位元格雷碼序列是2^n個整數的序列，其中：  
- 0到2^n-1的整數各出現一次  
- 第一個整數是0  
- 每兩個相鄰整數的二進制只有一個位元不一樣  
- **第一個**整數和**最後一個**整數的二進制只有一個位元不一樣  

輸入一個整數n，回傳任意有效的格雷碼。

# 解法
格雷碼的數量都是以2的次方在成長。  
先看看範例的的1位元是[0,1]，2位元是[00,01,11,10]其中有沒有什麼規律。  

i位元的格雷碼記做f(i)，由兩部分所組成：  
- 在f(i-1)的所有結果左方加上一個0
- 將f(i-1)的反轉，之後在左方加上一個1  

例如f(2)時是[00,01,11,10]，可以構造出組成f(3)：  
- 左半邊是f(2)所有結果左方加上0，得到[000,001,011,010]  
- 右半邊是f(2)先反轉變成[10,11,01,00]，在對每個結果左方加上1，得到[110,111,101,100]  
- 左右兩邊拼起來就是f(3)  

因為左半邊的最後一個數和右半邊第一個數都是由同一個數字所生成，因此可以保證只有一個位元不同。  

時空間複雜度O(2^n)。  

```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        def f(i):
            if i==1:
                return [0,1]
            prev=f(i-1)
            add=1<<(i-1)
            rev=[x|add for x in reversed(prev)]
            return prev+rev
        
        return f(n)
```

改成迴圈版本，直接在原本的數列上做修改。  

```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans=[0,1]
        
        for i in range(n-1):
            add=1<<(i+1)
            ans+=[x|add for x in reversed(ans)]
            
        return ans
```