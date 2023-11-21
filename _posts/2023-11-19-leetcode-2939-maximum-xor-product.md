---
layout      : single
title       : LeetCode 2939. Maximum Xor Product
tags        : LeetCode Medium Math BitManipulation Greedy
---
周賽372。

## 題目

輸入三個整數a, b和n。求滿足0 <= x < 2^n之下，(a XOR x) * (b XOR x)的最大值。  

答案可能很大，先模10^9+7後回傳。  

## 解法

x的上限是(2^n)-1，二進位最多n位。  
a和b都要和x做XOR，我們要決定x的每個位是1還是0。
  
為了使乘積盡可能大，則a和b的二進位表示中，需要盡可能多的1。  
分類討論a,b第i位的情況：  

- a,b都是1，則x必須為0，否則會降低乘積  
- a或b其中一者是1，**可選**讓1在a,b之間交換  
- a,b都是0，則x必須為1，可使a,b都變成1  

總而言之，在a,b的第i位都是0時，可以把他們一起變成1。  
但只有其中一者為1時，怎麼決定要不要交換？看看例題三：  
> a=1, b=6, n=3  
> a=0b001, b=0b110  
> 答案=1\*6=6  

這時每位都有一個1，沒辦法再變多。  
但是正確答案應該是：  
> x=0b101  
> a^x=0b100, b^x=0b011  
> 答案=4\*3=10  

發現在i=0和i=2位交換之後，乘積更大了。這是一個很重要的提示。  
試想a+b=c，在c不變的情況下，怎麼分配a,b才能使乘積最大化？兩者**盡可能平分**。  
但我們可能無法使a和b完全相等，只能盡量減少其差距，並增大乘積。  

回到剛才**可選交換**的情況，如果第i位的a是1，b是0，則交換後a會減少2^i，而b會增加2^i；反之亦然。  
從高位開始處理，只有在**可交換**，且持有1的一方**大於**另一方時，才要進行交換。  
貪心地考慮，交換後最差情況也只是a和b總值互換而已，絕對差一定不會增加，所以在滿足上述條件時總是交換。  

注意：a和b的二進位有可能超過n位，沒辦法改變。例如a=8, b=0, n=0時，答案為0。  

時間複雜度O(n)。  
空間複雜度O(1)。  

```python
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD=10**9+7
        for i in reversed(range(n)):
            mask=(1<<i)
            am=a&mask
            bm=b&mask
            
            if am>0 and bm>0:
                pass
            elif am==0 and bm==0:
                a|=mask
                b|=mask
            elif (am and a>b) or (bm and b>a):
                a^=mask
                b^=mask
            
        return (a*b)%MOD
```
