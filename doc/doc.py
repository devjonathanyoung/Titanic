# predict algorithm score using random split (here we do it 3 times on titanic data)
# from sklearn.cross_validation import cross_val_score
# scores = cross_val_score(alg,titanic[predictors], titanic["Survived"], cv=3)

# titanic_data.describe()
# print(titanic_data["Sex"].unique())
# print(titanic["Embarked"].unique())

""""
# Perform feature selection
selector = SelectKBest(f_classif, k=5)
selector.fit(titanic[predictors], titanic["Survived"])

# Get the raw p-values for each feature, and transform from p-values into scores
scores = -np.log10(selector.pvalues_)

# Plot the scores.
plt.bar(range(len(predictors)), scores)
plt.xticks(range(len(predictors)), predictors, rotation='vertical')
plt.show()
"""