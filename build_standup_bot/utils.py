import json
import os

DEFAULT_GROUP_NUM = 10


def get_groupnum():
    return os.getenv("GROUP_NUM", DEFAULT_GROUP_NUM)


def chunk(li, n):
    k, m = divmod(len(li), n)
    return [li[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(n)]


def get_groups():
    with open("build_standup_bot/assets/groups.json", "r") as f:
        groups = json.load(f)
    return groups


def save_groups(groups):
    with open("build_standup_bot/assets/groups.json", "w") as f:
        json.dump(groups, f)


def get_webhook():
    return os.getenv("WEBHOOK_URL", None)