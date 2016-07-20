import pandas
import formatting.format_data as fd
from learning.gradient_boosting import LearnerGradientBoosting


titanic_training_data = pandas.read_csv("./data/train.csv")
titanic_test = pandas.read_csv("./data/test.csv")

fd.format_titanic_data(titanic_training_data, titanic_training_data)
fd.format_titanic_data(titanic_test, titanic_training_data)
learner = LearnerGradientBoosting(titanic_training_data)

predictions = learner.predict(titanic_test)
formatted_prediction = pandas.DataFrame({
    "PassengerId": titanic_test["PassengerId"],
    "Survived": predictions
})
formatted_prediction.to_csv("kaggle.csv", index=False)
