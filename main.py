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
# Increase n_estimators for the number of trees
# Increase min_samples_split and min_samples_leaf to reduce overfitting and improve on unknown data
alg = RandomForestClassifier(random_state=1, n_estimators=150, min_samples_split=4, min_samples_leaf=2)

# prediction.to_csv("kaggle.csv", index=False)
