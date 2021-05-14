import random

import pandas as pd

from .utils import chunk, save_groups, get_groupnum


def create_groups():
    df = pd.read_csv("build_standup_bot/assets/testdata.csv")
    trainees = df["ID"].tolist()
    random.shuffle(trainees)
    return chunk(trainees, get_groupnum())


def main():
    groups = create_groups()
    save_groups(groups)


if __name__ == "__main__":
    main()