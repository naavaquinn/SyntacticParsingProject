from sklearn.tree import DecisionTreeClassifier

# Decision Tree classifer object
d_tree = DecisionTreeClassifier()
d_tree.fit(train_X, train_Y)
y_pred_d_tree = d_tree.predict(test_X)
     

evaluation_metrics("Decison Tree", test_Y, y_pred_d_tree)
