# SyntacticParsingProject
# Machine Learning Classifier Comparison

## Overview

This project aims to compare the performance of various machine learning classifiers using a dataset containing text data. The goal is to classify text samples into different categories based on their content. 

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Classifiers](#classifiers)
  - [Support Vector Machine (SVM)](#support-vector-machine-svm)
  - [Decision Tree](#decision-tree)
  - [Random Forest](#random-forest)
  - [Logistic Regression](#logistic-regression)
  - [K-Nearest Neighbors (KNN)](#k-nearest-neighbors-knn)
- [Model Comparisons](#model-comparisons)
- [Artificial Neural Network](#artificial-neural-network)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Python 3.x
- pandas
- scikit-learn
- matplotlib
- seaborn
- keras

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Mery-e/SyntacticParsingProject.git
2. Navigate the project directory

```bash
cd machine-learning-classifier-comparison
3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt

# Machine Learning Classifier Comparison

## Usage

1. **Navigate to the project directory:**

    ```bash
    cd machine-learning-classifier-comparison
    ```

2. **Install the required dependencies using pip:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Usage:**

    - Ensure you have the necessary dataset files:
        - `train_data.pkl`: Pickle file containing the training data.
        - `test_data.pkl`: Pickle file containing the test data.

    - Run the Python script `classifier_comparison.py`:

    ```bash
    python classifier_comparison.py
    ```

    - View the results and visualizations generated by the script.

## Classifiers

- **Support Vector Machine (SVM):**
    - The SVM classifier is implemented using scikit-learn's `SVC` class with a linear kernel. Training and testing data are loaded from the pickle files, preprocessed, and fed into the classifier.

- **Decision Tree:**
    - A Decision Tree classifier is trained and tested using scikit-learn's `DecisionTreeClassifier`. The default settings are used for this classifier.

- **Random Forest:**
    - The Random Forest classifier is implemented using scikit-learn's `RandomForestClassifier`. It consists of an ensemble of decision trees and is trained on the dataset to perform classification.

- **Logistic Regression:**
    - Logistic Regression is applied using scikit-learn's `LogisticRegression` class. It's a linear model suitable for binary classification tasks.

- **K-Nearest Neighbors (KNN):**
    - The KNN classifier is implemented using scikit-learn's `KNeighborsClassifier`. It classifies samples based on the majority class among its k-nearest neighbors.

## Model Comparisons

- Performance metrics such as accuracy, precision, recall, and F1-score are computed for each classifier. Confusion matrices and ROC curves are also generated to visualize the performance.

## Artificial Neural Network

- An artificial neural network (ANN) model is built using Keras. It consists of multiple layers with dropout regularization and sigmoid activation functions. The model is trained using the training data and evaluated on the test data.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

