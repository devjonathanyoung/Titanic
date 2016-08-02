from sklearn.linear_model import LogisticRegression
import pandas


class LearnerLogisticRegression:
    def __init__(self, training_data):
        self.predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked"]
        self.alg = LogisticRegression(random_state=1)
        self.alg.fit(training_data[self.predictors], training_data["Survived"])

    def predict(self, to_predict_data):
        predictions = self.alg.predict(to_predict_data[self.predictors])
        return predictions
