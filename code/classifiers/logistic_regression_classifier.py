
logistic_regression = LogisticRegression()
logistic_regression.fit(train_X, train_Y)
y_pred_lr = logistic_regression.predict(test_X)
     

evaluation_metrics("Logistic Regression", test_Y, y_pred_lr)
