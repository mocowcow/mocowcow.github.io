---
layout      : single
title       : LeetCode 421. Maximum XOR of Two Numbers in an Array
tags 		: LeetCode Medium HashTable Trie BitManipulation
---
中午吃飽就在想解法，想到睡著，總算有個差強人意的答案。  
這位論壇老哥評論深得我心：
> man i hate bit manipulation 

# 題目
輸入整數陣列，求任兩個數做XOR運算可得到的最大值。

# 解法
將每個數字依照位元建立字典樹。  
再對每個數字試著求相反位元，例：9 = 00..1001，試著找1..0110是否存在。  
執行速度略為感人啊。  

```python
class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()
        # build trie
        for n in nums:
            curr = root
            for i in range(31, -1, -1):
                bit = (n >> i) & 1
                curr = curr.children[bit]
                
        # get max XOR
        ans = 0
        for n in nums:
            curr = root
            xor = 0
            for i in range(31, -1, -1):
                bit = (n >> i) & 1
                reverse = 1 ^ bit
                if reverse in curr.children:
                    xor |= (1 << i)
                    curr = curr.children[reverse]
                else:
                    curr = curr.children[bit]
            ans = max(ans, xor)

        return ans
```

大神的解法，反正我看了是不怎麼能理解。

```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = mask = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            s = set()
            for n in nums:
                s.add(n & mask)
            temp = ans | (1 << i)
            for n in s:
                if temp ^ n in s:
                    ans = temp
                    break

        return ans
```