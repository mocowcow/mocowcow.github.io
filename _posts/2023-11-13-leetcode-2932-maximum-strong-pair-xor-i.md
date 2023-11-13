---
layout      : single
title       : LeetCode 2932. Maximum Strong Pair XOR I
tags        : LeetCode Easy Array Simulation BitManipulation Trie TwoPointers SlidingWindow HashTable Bitmask
---
周賽371。同時是Q1也是Q4。  
其實我感覺這題有點微妙，怎麼會有將近700人通過。  
畢竟中國站在11/4號的每日題就是這次的原題，答案稍微改一下就可以了。  

更扯的是js和C#能用O(N^2)過Q4，真的是很鳥。  

## 題目

輸入整數陣列nums。一個整數數對x和y若滿足以下條件，則稱為**強壯的**：  

- |x - y| <= min(x, y)  

你必須從nums中選擇兩個整數組成**強壯的數對**，且他們的XOR值是所有**強壯數對**中的最大值。  
求所有強壯數對中的XOR最大值。  

注意：你可以選擇同一個整數兩次來組成數對。  

## 解法

相似題[421. maximum xor of two numbers in an array]({% post_url 2022-01-27-leetcode-421-maximum-xor-of-two-numbers-in-an-array %})。  

一樣先來個暴力解。  
時間複雜度O(N^2)。  
空間複雜度O(1)。  

```python
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans=0
        for x in nums:
            for y in nums:
                if abs(x-y)<=min(x,y):
                    ans=max(ans,x^y)
                    
        return ans
```

對於整數x來說，要怎麼找到能使XOR結果最大化的整數y？  
假設x=4，二進位表示0b1000。  
因為XOR具有抵銷的特性，最理想其況下應該是找到二進位0b0111的數，才能使得所有位元都是1，得到0b1111。  

為了讓0b1000變成0b1111，需要找到0b0111。  
我們先在nums中找有沒有0b0xxx開頭的數。有找到，就繼續找0b01xx；沒找到就往0b11xx找。重複值到找滿所有位元。  
如果整個陣列都只有一種狀況，那最差情況下也就只找到自己，XOR結果為0。  

這種查找方式就像是樹狀結構，每個節點有找到/沒找到兩個分支，正是**字典樹**。  
先確認數字的最大位元之後，以數的二進位表示**建樹**，即可實現此查找方式。  

那|x - y| <= min(x, y)這個條件怎麼辦？  
先約定大前提y <= x，這樣min(x, y)實質上就只能是y，而|x - y|就只是x-y。  
代入原式子，得到x-y <= y，移項得到x <= 2y。  

把nums依遞增排序後枚舉x，可以保證先前處理過的整數y一定不超過x。  
另外維護一個指針j，指向最小的合法的y位置。如果y不滿足2y >= x，則把y從字典樹中**移除**，保證x在樹中找到的數y一定都滿足條件。  

時間複雜度O(N log N + N log MX)，其中MX為max(nums)，在此為20。  
空間複雜度O(N log MX)。  

```python
class Trie:
    def __init__(self):
        self.child=defaultdict(Trie)
        self.cnt=0
        
def build(root,x,MX):
    curr=root
    for i in reversed(range(MX)):
        b=(x>>i)&1
        curr=curr.child[b]
        curr.cnt+=1

def getXOR(root,x,MX):
    res=0
    curr=root
    for i in reversed(range(MX)):
        b=(x>>i)&1
        rev=b^1
        if rev in curr.child:
            res|=(1<<i)
            curr=curr.child[rev]
        else:
            curr=curr.child[b]
    return res

def kill(root,x,MX):
    curr=root
    for i in reversed(range(MX)):
        b=(x>>i)&1
        prev=curr
        curr=curr.child[b]
        curr.cnt-=1
        if curr.cnt==0:
            del prev.child[b]
            return 
        
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        MX=max(x.bit_length() for x in nums)
        nums.sort()
        root=Trie()
        ans=0
        j=0
        for x in nums:
            # keep 2y >= x
            while not nums[j]*2>=x:
                kill(root,nums[j],MX)
                j+=1
            build(root,x,MX)
            ans=max(ans,getXOR(root,x,MX))
                
        return ans
```
