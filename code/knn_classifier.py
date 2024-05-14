from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(train_X, train_Y)
y_pred_knn = knn.predict(test_X)
     

evaluation_metrics("KNN", test_Y, y_pred_knn)
