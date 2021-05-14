import random

import pandas as pd

from .utils import chunk, save_groups, get_groupnum

areas = ["iOS", "Android", "Frontend", "Backend", "ML"]
langs = ["En", "Either", "Ja"]


def create_area_and_lang_groups():
    df = pd.read_csv("build_standup_bot/assets/testdata.csv")
    groups = {
        lang: {
            area: sorted(
                df[(df["Area"] == area) & (df["Language"] == lang)].ID.to_list(),
                key=lambda x: random.random(),
            )
            for area in areas
        }
        for lang in langs
    }
    return groups


def create_groups(groups):
    reverse = 1
    member_list = []
    for area in areas:
        for lang in langs[::reverse]:
            member_list += groups[lang][area]
        reverse *= -1
    return chunk(member_list, get_groupnum())


def main():
    tmp_groups = create_area_and_lang_groups()
    groups = create_groups(tmp_groups)
    save_groups(groups)


if __name__ == "__main__":
    main()