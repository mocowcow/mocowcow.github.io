import os
from string import Template
from datetime import datetime

import leetcode_api

POST_TEMPLATE_STRING = """---
layout      : single
title       : $POST_TITLE
tags        : $TAGS
---
$CONTENT
"""
POST_TEMPLATE = Template(POST_TEMPLATE_STRING)
LC_POST_CONTENT_TEMPLATE_STRING = """$FOREWORD

## 題目
$LCLINK

## 解法
"""
LC_POST_CONTENT_TEMPLATE = Template(LC_POST_CONTENT_TEMPLATE_STRING)


class PostMaker:
    def __init__(self):
        # 找出已經寫過的
        self.leetcode_posts = set()
        files = os.listdir(".")
        for f in files:
            try:
                ss = f.split('-')
                if ss[3] != 'leetcode':
                    continue
                n = ss[4]
                self.leetcode_posts.add(n)
            except:  # 非 lc 題解不處理
                pass

    def make_post(self, post_title, tags="", content=""):
        curr_date = datetime.now().strftime('%Y-%m-%d')
        trimmed_title = post_title.replace(" ", "-").replace(".", "").lower()
        file_name = f'{curr_date}-{trimmed_title}.md'
        text = POST_TEMPLATE.substitute(
            POST_TITLE=post_title,
            TAGS=tags,
            CONTENT=content
        )
        with open(file_name, 'w', encoding='utf8') as f:
            f.write(text)

    def make_leetcode_post(self, title_slug, foreword="", lclink=""):
        q_info = leetcode_api.get_question(title_slug)
        front_id = q_info["questionFrontendId"]
        title = q_info["title"]
        front_id = q_info["questionFrontendId"]
        difficulty = q_info["difficulty"]

        if front_id in self.leetcode_posts:
            print("已經寫過了")
            return

        post_title = f"LeetCode {front_id}. {title}"
        tags = f"LeetCode {difficulty}"
        content = LC_POST_CONTENT_TEMPLATE.substitute(
            FOREWORD=foreword, LCLINK=lclink)
        self.make_post(post_title, tags, content)
        self.leetcode_posts.add(front_id)
        print("建立成功：", post_title)
