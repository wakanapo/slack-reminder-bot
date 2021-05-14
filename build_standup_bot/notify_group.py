import json

import requests

from .utils import get_groups, get_webhook


def create_message(groups):
    message = ["This is new groups!"]
    for i, g in enumerate(groups):
        message.append(f"[Group {i}]")
        message.append(" ".join([f"<{m}>" for m in g]))
    return "\n".join(message)


def send_message(message):
    url = get_webhook()
    payload = {"text": message}
    headers = {"content-type": "application/json"}
    if url is None:
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
    message = create_message(groups)
    send_message(message)


if __name__ == "__main__":
    main()