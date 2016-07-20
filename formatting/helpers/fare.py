def extract(data):
    data["Fare"] = data["Fare"].fillna(data["Fare"].median())
