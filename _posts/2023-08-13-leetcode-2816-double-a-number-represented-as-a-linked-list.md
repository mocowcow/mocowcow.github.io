---
layout      : single
title       : LeetCode 2816. Double a Number Represented as a Linked List
tags        : LeetCode Medium Array LinkedList
---
周賽358。很單純的linked list題。  

## 題目

輸入一個linked list的首節點head，這個list代表一個非負整數，且不具有前導零。  

將每個list代表的值翻倍後，回傳修改過的head。  

## 解法

每一個節點代表一個位的值。  
最簡單暴力就是將全部節點值拆出來，全部乘二，然後由後往前處理進位，然後轉回list。  

例題很良心的提醒長度會改變：  
> [9,9,9]  
> 翻倍後[1,9,9,8]  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes=[]
        curr=head
        while curr:
            nodes.append(curr.val*2)
            curr=curr.next
            
        carry=0
        for i in reversed(range(len(nodes))):
            nodes[i]+=carry
            carry=nodes[i]//10
            nodes[i]%=10
            
        if carry>0:
            nodes=[carry]+nodes
        
        dummy=ListNode()
        curr=dummy
        for x in nodes:
            o=ListNode(x)
            curr.next=o
            curr=o
        
        return dummy.next
```

既然是linked list，那八成可以用遞迴解決。  

對於每個值為val的節點o，他的新值會是兩倍的val加上下個節點的進位，然後再把進位丟給上一個節點。  
定義f(o)：將節點o為首的list翻倍，然後回傳產生的進位值。  

從head開始翻倍，如果head會進位，記得建立新的節點。  

時間複雜度O(N)。  
空間複雜度O(N)。  

```python
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def f(o):
            if not o:
                return 0
            o.val=o.val*2+f(o.next)
            carry=o.val//10
            o.val%=10
            return carry
        
        carry=f(head)
        
        if carry:
            head=ListNode(carry,head)    
            
        return head
```

不管是遞迴還是暴力法都要額外空間，其實還有更省的方法。  

首先把list反轉，這樣處理進位就變成加在下一個節點上面，可以單純迴圈遍歷。  
但是我們沒有紀錄上一個節點prev，沒辦法到最後一個節點後面。要等第二次反轉，才把進位加到head前方。  

例如：  
> [9,8]  
> 反轉第一次=[8,9]  
> 翻倍=[6,9]，最後進位剩下1  
> 反轉第二次=[9,6]  
> 在首節點補上進位=[1,9,6]  

時間複雜度O(N)。  
空間複雜度O(1)。  

```python
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head):
            prev=None
            curr=head
            while curr:
                t=curr.next
                curr.next=prev
                prev=curr
                curr=t
            return prev
        
        head=reverse(head)
        carry=0
        curr=head
        while curr:
            curr.val=curr.val*2+carry
            carry=curr.val//10
            curr.val%=10
            curr=curr.next
        
        head=reverse(head)
        if carry:
            head=ListNode(carry,head)
            
        return head
```
