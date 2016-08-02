import re


def get_title(name):
    title_search = re.search(' ([A-Za-z]+)\.', name)
    if title_search:
        return title_search.group(1)
    return ""


def get_name_length(data):
    data["NameLength"] = data["Name"].apply(lambda x: len(x))


def extract(data):
    get_name_length(data)
    titles = data["Name"].apply(get_title)
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Dr": 5, "Rev": 6, "Major": 7, "Col": 7, "Mlle": 8,
                     "Mme": 8, "Don": 9, "Lady": 10, "Countess": 10, "Jonkheer": 10, "Sir": 9, "Capt": 7, "Ms": 2,
                     "Dona": 9}
    for k, v in title_mapping.items():
        titles[titles == k] = v
    data["Title"] = titles
