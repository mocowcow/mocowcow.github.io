---
layout      : single
title       : LeetCode 895. Maximum Frequency Stack
tags 		: LeetCode Hard Stack HashTable Design Heap
---
每日題。stack系列連霸一周啦！搞不好今晚雙周賽壓軸就是stack。

# 題目
設計資料結構Maximum Frequency Stack，包含以下功能：  
1. 無參數建構子
2. void push(int val)，將元素押入stack
3. int pop()，彈出出現頻率最高的元素，若有多個頻率相同的元素，則彈出最後靠近stack頂端的

# 解法
看著題目描述有點可怕，但只要想成對每個出現頻率獨立維護一個stack，那就很簡單了。  
試著押入[5,7,5,7,3]：  
> freq1=[5] ,freq2=[]  
> freq1=[5,7] ,freq2=[]    
> freq1=[5,7] ,freq2=[5]   
> freq1=[5,7] ,freq2=[5,7]   
> freq1=[5,7,3] ,freq2=[5,7]   

全部彈出順序應為[7,5,3,7,5]。  

為了實驗這個邏輯，我們還需要一個雜湊表ctr用來計算出現次數，還有一個變數maxFreq表示現在最高頻率是幾次，好決定從哪個stack中彈出元素。  
每次push，先將該val值計數+1，並加入相應頻率的stack中，並更新maxFreq。  
每次pop，先以maxFreq選擇stack彈出元素val，並將val計數-1。若該stack為空，則將maxFreq-1。最後回傳val。

```python
class FreqStack:

    def __init__(self):
        self.d=defaultdict(list)
        self.ctr=Counter()
        self.maxFreq=0

    def push(self, val: int) -> None:
        self.ctr[val]+=1
        self.d[self.ctr[val]].append(val)
        self.maxFreq=max(self.maxFreq,self.ctr[val])

    def pop(self) -> int:
        val=self.d[self.maxFreq].pop()
        self.ctr[val]-=1
        if not self.d[self.maxFreq]:
            self.maxFreq-=1
        return val
```

這邊提供一個邪門的方法。  
當我學完heap的功能時，馬上就想到可以用在這個地方，似乎比起上面解法更容易想到。  

維護最小堆疊h，還需要一個雜湊表計數，再一個serial流水號變數，用來比對元素新舊。  
每次push，先將該val值計數+1，流水號+1，並以(出現次數, 新舊順序, 值)的格式押入heap中。heap會先以出現頻率高者往前排、若頻率相同則較新的在前。    
每次pop，直接取值，並將計數-1，回傳即可。


```python
class FreqStack:

    def __init__(self):
        self.h=[]
        self.ctr=Counter()
        self.serial=0

    def push(self, val: int) -> None:
        self.ctr[val]+=1
        self.serial+=1
        heappush(self.h,(-self.ctr[val],-self.serial,val))

    def pop(self) -> int:
        _,_,val=heappop(self.h)
        self.ctr[val]-=1
        return val 
```

