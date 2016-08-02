def replace_embarked_with_numbers(data):
    data.loc[data["Embarked"] == "S", "Embarked"] = 0
    data.loc[data["Embarked"] == "C", "Embarked"] = 1
    data.loc[data["Embarked"] == "Q", "Embarked"] = 2


def extract(data):
    data["Embarked"] = data["Embarked"].fillna("S")
    replace_embarked_with_numbers(data)
