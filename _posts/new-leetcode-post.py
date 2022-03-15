from datetime import datetime
import os

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

# 嘗試新建
print('目前已寫過', len(leetcode_posts), '題')
print('輸入題號+題目名：\n')
while True:
    # TOPIC = '1. Two Sum'
    TOPIC = input().strip()
    number = TOPIC[:TOPIC.index('.')]
    if number in leetcode_posts:
        print('已經寫過了\n')
        continue
    title = '-'.join(TOPIC.split(' ')[1:]).lower()
    time = datetime.now().strftime('%Y-%m-%d')
    filename = f'{time}-leetcode-{number}-{title}.md'
    template = f"""---
layout      : single
title       : LeetCode {TOPIC}
tags 		: LeetCode
---
# 題目

# 解法

```python
code here

```

"""

    print('新建成功\n')
    leetcode_posts.add(number)
    with open(filename, 'w', encoding='utf8') as f:
        f.write(template)
