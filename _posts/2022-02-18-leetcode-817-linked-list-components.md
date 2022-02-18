---
layout      : single
title       : LeetCode 817. Linked List Components
tags 		: LeetCode Medium HashTable LinkedList
---
隨便抽題來寫，結果碰到這超級爛的題目描述，難怪可以600讚1600爛。

# 題目
輸入head表示linked list的起點、整數陣列nums。  
若節點中的值同時存在於nums中，稱為元件，連續出現多個nums值則算同一個元件。求總共有多少元件。  
> head = [0,1,2,3], nums = [0,1,3]  
> [0,1]和[3]各為一個元件  
> head = [0,1,2,3,4], nums = [0,3,1,4]   
> [0,1]和[3,4]各為一個元件

# 解法
我還是看討論區解釋才懂題目在講什麼的，結果很單純。  
簡單來講就是把不在nums中的節點當作空氣，看最後會變成幾個區段。  
例：
> head = [0,1,2,3], nums = [0,1,3]  
> 可以看成[0,1]和[3]兩段

先把nums裝入set變數d，維護布林值comp，表示是否已經計入。若節點值在d中且comp=false，則把comp設true，計數+1；直到某個節點值不在d中，再將comp恢復為false。

```python
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        d = set(nums)
        ans = 0
        curr = head
        comp = False
        while curr:
            if curr.val in d:
                if not comp:
                    comp = True
                    ans += 1
            else:
                comp = False
            curr = curr.next

        return ans
```
