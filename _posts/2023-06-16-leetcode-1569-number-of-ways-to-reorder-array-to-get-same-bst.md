--- 
layout      : single
title       : LeetCode 1569. Number of Ways to Reorder Array to Get Same BST
tags        : LeetCode Hard Array Tree BinarySearchTree DP Math
---
每日題。又是數學題，每次碰到這種都不好過。  
我自己只想到是樹狀DP，組合數的部分還是靠朋友支援才搞懂的。  

# 題目
輸入陣列nums，是一個由整數1\~n的排列。  
我們會依照nums中的順序將所有元素插入初始為空的二元搜尋樹(BST)。  
求將nums**重新排序**後，有幾種方案得到的BST和原本nums的結果相同。  

例如nums = [2,1,3]，和[2,3,1]得到的BST相同，但和[3,2,1]不同。  

答案可能很大，先模10^9+7後回傳。  

# 解法
題目問的是**除本身以外**的其他方案數，而以下是先求**全部方案數**，最後在扣掉本身1。  

對於根節點為x的BST來說，所有小於x的數都是左子節點，大於x的都是右子節點。  
設左子樹節點有l個，右子樹節點有r個。  

為確保BST的結構相同，左右子樹必須遵照特定的插入順序，這時候就簡化成一個子問題。  
例如：  
> nums = [4,2,1,3]  
> 根節點是4，左子樹是[2,1,3]，右子樹為空  
> 但是對於4來說，左子樹是[2,1,3]或是[2,3,1]都是一樣的  
> 左子樹有2種方案，右子樹只有1種方案(空)  
> 根據乘法原理，得到2\*1=2  

扣掉原本nums的一種方案，得到答案2-1=1。  
答案是對的，方法是錯的。  
照這個方法來算，num = [2,1,3]算出是1\*1=1，跟剛才講到的互斥，應該是2才對！  

來仔細看看：  
> nums = [2,1,3]  
> 根節點是2，左子樹是[1]，右子樹是[3]  
> 兩邊各只有1種方案，但是！  
> 可以先建構左子樹，或是先建構右子樹，或是兩者**交織**建立  
> 總共有l+r個子節點，要在這些位置中決定左子樹l個點在哪些位置  
> 也就是組合數的C(l+r,l)  
> 答案是左子樹方案\*右子樹方案\*C(l+r,l)  
> 也就是1\*1\*2=2  

公式推出來就可以實作了。  
定義dp(a)：以陣列a建構出的BST方案數。  
轉移方程式：dp(a)=dp(left)\*dp(right)\*C(l+r,l)，其中left和right分別是a中小於和大於a[0]的數    
base cases：當一顆樹的節點不超過2，則一定只有一種方案  

每次拆分左右子樹需要O(N)時間，最差情況會拆出N個子樹，也就是變成linked list。  
時間複雜度O(N^2)。  
空間複雜度O(N^2)。  

```python
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD=10**9+7
   
        def dp(a):
            if len(a)<=2:
                return 1
            left=[]
            right=[]
            for x in a[1:]:
                if x<a[0]:
                    left.append(x)
                else:
                    right.append(x)
            
            l=len(left)
            r=len(right)
            return dp(left)*dp(right)*comb(l+r,l)%MOD
                
        ans=dp(nums)-1
        return ans%MOD
```
