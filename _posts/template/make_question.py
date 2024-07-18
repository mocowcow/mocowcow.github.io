from post_maker import PostMaker

# question link
# https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/


def main():
    print("輸入題目網址：")
    maker = PostMaker()
    while True:
        link = input()
        title_slug = link.split("/")[4]
        maker.make_leetcode_post(title_slug)


if __name__ == "__main__":
    main()
