def fill_empty_ages(data, train_median):
    data["Age"] = data["Age"].fillna(train_median)


def replace_sex_with_numbers(data):
    data.loc[data["Sex"] == "male", "Sex"] = 0
    data.loc[data["Sex"] == "female", "Sex"] = 1


def fill_empty_embarked(data):
    data["Embarked"] = data["Embarked"].fillna("S")


def replace_embarked_with_numbers(data):
    data.loc[data["Embarked"] == "S", "Embarked"] = 0
    data.loc[data["Embarked"] == "C", "Embarked"] = 1
    data.loc[data["Embarked"] == "Q", "Embarked"] = 2


def fill_empty_fare(data):
    data["Fare"] = data["Fare"].fillna(data["Fare"].median())


def compute_family_size(data):
    # Sibsp = Number of Siblings/Spouses Aboard
    # parch = Number of Parents/Children Aboard
    data["FamilySize"] = data["SibSp"] + data["Parch"]


def compute_namelength(data):
    data["NameLength"] = data["Name"].apply(lambda x: len(x))


def format_titanic_data(data, train_data):
    fill_empty_ages(data, train_data["Age"].median())

    replace_sex_with_numbers(data)

    fill_empty_embarked(data)
    replace_embarked_with_numbers(data)

    fill_empty_fare(data)

    compute_family_size(data)
    compute_namelength(data)

    return data
