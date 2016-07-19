import pandas
import formatting.format_data as fd
from sklearn.ensemble import RandomForestClassifier


titanic_training_data = pandas.read_csv("./data/train.csv")
titanic_test = pandas.read_csv("./data/test.csv")

fd.format_titanic_data(titanic_training_data, titanic_training_data)
fd.format_titanic_data(titanic_test, titanic_training_data)

# learner = Learner(titanic_training_data)
# prediction = learner.predict(titanic_test)
predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
alg = RandomForestClassifier(random_state=1, n_estimators=10, min_samples_split=2, min_samples_leaf=1)

# prediction.to_csv("kaggle.csv", index=False)
