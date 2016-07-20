def extract(data, train_median):
    data["Age"] = data["Age"].fillna(train_median)
