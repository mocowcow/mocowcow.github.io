import leetcode_api
from post_maker import PostMaker

# contest link
# https://leetcode.com/contest/weekly-contest-406/


def main():
    print("輸入競賽網址：")
    link = input()
    contest_name = link.split("/")[4]
    print(f"{contest_name = }")

    c_info = leetcode_api.get_contest_json(contest_name)
    c_questions = c_info["questions"]

    foreword = contest_name.replace("-", " ") + "。  "
    maker = PostMaker()
    for c_q in c_questions:
        title_slug = c_q["title_slug"]
        maker.make_leetcode_post(title_slug, foreword)


if __name__ == "__main__":
    main()
