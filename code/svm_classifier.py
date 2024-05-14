train_Y = gentle_train_Y
test_Y = gentle_test_Y
train_X = []
for i in range(len(gentle_train_df)):
  row = gentle_train_df.loc[i, :].values.flatten().tolist()
  train_X.append(row)

test_X = []

for i in range(len(gentle_test_df)):
  row = gentle_test_df.loc[i, :].values.flatten().tolist()
  test_X.append(row)
     

from sklearn.svm import SVC
SupportVectorClassModel = SVC(kernel = 'linear', probability=True)
SupportVectorClassModel.fit(train_X, train_Y)
y_pred_test = SupportVectorClassModel.predict(test_X)
     

SupportVectorClassModel = SVC(kernel = 'linear', probability=True)
SupportVectorClassModel.fit(train_X, train_Y)
y_pred_test = SupportVectorClassModel.predict(test_X)
     

methodDict = {}
from sklearn import metrics
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns

def evaluation_metrics(model, y_test, y_pred_class):
  accuracy =  metrics.accuracy_score(y_test, y_pred_class)
  print("Accuracy:", accuracy)
  methodDict[model] = accuracy * 100

  print("-" * 70)

  #Classification report
  print("Classification report:")
  report = classification_report(y_test, y_pred_class)
  print(report)

  print("-" * 70)

  #Confusion matrix
  confusion = metrics.confusion_matrix(y_test, y_pred_class)

  # visualize Confusion Matrix
  plt.figure(figsize=(4, 2))
  sns.heatmap(confusion,annot=True,fmt="d")
  plt.title('Confusion Matrix')
  plt.xlabel('Predicted')
  plt.ylabel('Actual')
  plt.show()

  print("-" * 70)

  # ROC curve
  roc_auc = metrics.roc_auc_score(y_test, y_pred_class)
  fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_class)

  plt.figure(figsize=(5, 5))
  plt.plot(fpr, tpr, color='#DF6589FF', label='ROC curve (area = %0.2f)' % roc_auc)
  plt.plot([0, 1], [0, 1], color='#3C1053FF', linestyle='--')
  plt.xlim([0.0, 1.0])
  plt.ylim([0.0, 1.0])
  plt.rcParams['font.size'] = 12
  plt.title('ROC curve for treatment classifier')
  plt.xlabel('False Positive Rate (1 - Specificity)')
  plt.ylabel('True Positive Rate (Sensitivity)')
  plt.legend(loc="lower right")
  plt.show()

     

evaluation_metrics("SVM", test_Y, y_pred_test)
