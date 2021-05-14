import json

import requests

from .utils import get_groups, get_webhook


def create_message(members, group_num):
    template = f"""\n\
    Daily report for *Group {group_num}*!\n\
    Please write what you are going to study today, what course you will take, etc.\n\
    \n\
    *グループ{group_num}* 向けのDaily Reportです！\n\
    今日どんな事を勉強するのか、どんなコースを取るのか書いてくださいね。\n\
    ---------\n\
    """
    mention = " ".join([f"<{m}>" for m in members])
    return mention + template


def send_message(message):
    url = get_webhook()
    payload = {"text": message}
    headers = {"content-type": "application/json"}
    if url is "":
        print(f"Dry run: {json.dumps(payload)}")
        return
    response = requests.post(
        url,
        data=json.dumps(payload),
        headers=headers,
    )
    print(response.text)


def main():
    groups = get_groups()
    for i, g in enumerate(groups):
        message = create_message(g, i)
        send_message(message)


if __name__ == "__main__":
    main()