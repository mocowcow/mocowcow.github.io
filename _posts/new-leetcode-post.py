from datetime import datetime
from string import Template
import os


tpl = '''--- 
layout      : single
title       : LeetCode $TOPIC
tags        : LeetCode
---
$FOREWORD

# 題目

# 解法

```python
code here

```
'''
template = Template(tpl)

# 找出已經寫過的
leetcode_posts = set()
path = '.'
files = os.listdir(path)
for f in files:
    try:
        ss = f.split('-')
        if ss[3] != 'leetcode':
            continue
        n = ss[4]
        leetcode_posts.add(n)
    except:
        pass

# 自訂前言
print('自訂前言：')
foreword=input()

# 嘗試新建
print('目前已寫過', len(leetcode_posts), '題')
print('輸入題號+題目名：\n')
while True:
    # topic = '1. Two Sum'
    topic = input().strip()
    number = topic[:topic.index('.')]
    if number in leetcode_posts:
        print('已經寫過了\n')
        continue
    title = '-'.join(topic.split(' ')[1:]).lower()
    time = datetime.now().strftime('%Y-%m-%d')
    filename = f'{time}-leetcode-{number}-{title}.md'
    text = template.substitute(FOREWORD=foreword,TOPIC=topic)
    with open(filename, 'w', encoding='utf8') as f:
        f.write(text)
    print('新建成功\n')
    leetcode_posts.add(number)
