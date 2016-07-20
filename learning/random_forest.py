from sklearn.ensemble import RandomForestClassifier
import pandas


class LearnerRandomForest:
    def __init__(self, training_data):

        # Increase n_estimators for the number of trees
        # Increase min_samples_split and min_samples_leaf to reduce overfitting and improve on unknown data
        # self.predictors = ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "FamilySize",
        #                   "Title", "FamilyId"]
        self.predictors = ["Pclass", "Sex", "Fare", "Title"]
        self.alg = RandomForestClassifier(random_state=1, n_estimators=150, min_samples_split=8, min_samples_leaf=4)
        self.alg.fit(training_data[self.predictors], training_data["Survived"])

    def predict(self, to_predict_data):
        predictions = self.alg.predict(to_predict_data[self.predictors])
        return predictions
