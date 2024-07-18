import requests

# REST
HEADERS = {}
HEADERS['Sec-Ch-Ua'] = '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"'
HEADERS['Sec-Fetch-Dest'] = 'document'
HEADERS['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'

# GraphQL
GRAPHQL_URL = "https://leetcode.com/graphql/"
QUERY = """
query questionTitle($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        titleSlug
        difficulty
    }
}
"""

# Contest
CONTEST_URL = "https://leetcode.com/contest/api/info/"


def get_contest_json(contest_name):
    url = CONTEST_URL + contest_name
    rsps = requests.get(url, headers=HEADERS)
    rsps.raise_for_status()
    return rsps.json()


def get_question(title_slug):
    body = {
        "operationName": "questionTitle",
        "variables": {"titleSlug": title_slug},
        "query": QUERY
    }
    rsps = requests.post(GRAPHQL_URL, json=body)
    rsps.raise_for_status()
    return rsps.json()['data']['question']
