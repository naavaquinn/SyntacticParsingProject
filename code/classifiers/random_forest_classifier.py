
# Instantiate model with 100 decision trees
random_forest = RandomForestClassifier()
random_forest.fit(train_X, train_Y)
y_pred_rf = random_forest.predict(test_X)
     

evaluation_metrics("Random Forest", test_Y, y_pred_rf)
