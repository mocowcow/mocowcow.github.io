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

上面這種要換不換或許有點難理解，這邊改另一種方式來思考。  
不對a,b本身做修改，而是去構造a,b經過XOR之後的結果p,q，使得p\*q最大。  

記得，我們只能對後面n位做處理，所以p,q超過n位的地方都和a,b是相同的。  
同樣地，為了使乘積盡可能大，要讓p,q的絕對差最小化。  
倒序處理n個位，若a,b的第i位都是1或0，則p,q都可以是1；否則將1丟給較小的一方，把絕對差變小。  

時間複雜度O(n)。  
空間複雜度O(1)。  

```python
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD=10**9+7
        p=(a>>n)<<n # clean last n bits for a
        q=(b>>n)<<n # clean last n bits for b
        for i in reversed(range(n)):
            mask=(1<<i)
            am=a&mask
            bm=b&mask
            if am==bm: # am==bm==0 or am==bm==1
                p|=mask
                q|=mask
            elif p>q:
                q|=mask
            else:
                p|=mask

        return (p*q)%MOD
```

試想a=1111, b=0000的情況下，要怎麼分給p,q？  
當(2^i)-1等於所有0<=j<i的2^j總和，差不多就是一半。其中一者拿最高位的1，剩下都給另一邊。  
分配後是p=1000, q=0111。  
就算a的1不多，例如a=101, b=000，也是同樣的分法，畢竟沒有辦法分得更平均。  

上述情況是p,q只能選一者放1，稱為single。拿a和b做XOR後，保持1的位元可以擇一設為1。  
若在第i位上，a,b都是1或0，則p,q都可以變成1，這種情況稱作double。拿n位全是1的遮罩和single做XOR，保持1的位元可以**兩者**都設為1。  

別忘了，我們只能對後n位做調整，超過的部分必須保持原樣。  
所以p,q超出n位的部分要先保留，然後兩者各加上double，最後才來分配single。  

如果沒有超出n位的值，則p和q都相等，就按照剛才所說過的p拿最大位元，其餘給q。  
否則兩者的絕對差至少2^n，就算把所有single都加上也不足夠，所以全部給較小者。  

時間複雜度O(1)。  
空間複雜度O(1)。  

```python
class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD=10**9+7
        
        p=(a>>n)<<n # clean last n bits
        q=(b>>n)<<n
        a^=p # keep only last n bits
        b^=q
        
        single=a^b # only a or b can be 1
        last_n=(1<<n)-1
        double=last_n^single # both a and b are 1
        
        # apply double 1
        p|=double 
        q|=double
        
        # assign single 1 if any
        if single>0:
            if p==q: # assign largest bit to p, others to q
                m=single.bit_length()
                largest=1<<(m-1)
                other=single^largest
                p^=largest
                q|=other
            else: # assign all to smaller one
                if p>q: # keep p<q
                    p,q=q,p
                p|=single
                
        return (p*q)%MOD
```
