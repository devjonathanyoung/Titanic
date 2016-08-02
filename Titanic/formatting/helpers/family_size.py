def extract(data):
    # Sibsp = Number of Siblings/Spouses Aboard
    # parch = Number of Parents/Children Aboard
    data["FamilySize"] = data["SibSp"] + data["Parch"]