
# SyntacticParsingProject
# Machine Learning Classifier Comparison

## Overview

The goal of this project is to implement a syntactic annotation reliability scorer capable of assigning reliability scores to automatically generated syntactic parses. Despite significant advances in automated parsing systems, ensuring the reliability of syntactic annotations remains an unsolved task. Assessing the reliability of a syntactic annotation offers benefits not only for syntactic parsing tasks but also for all downstream NLP tasks utilizing the generated syntactic annotations.

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
```

2. Navigate the project directory

```bash
cd SyntacticParsingProject
```

3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage
- Ensure you have the necessary dataset files

### Parsers
The parsers directory includes utilities for parsing and analyzing syntactic structures:


**Compare Parser**: Compare syntactic annotations between different parsers.
**CoNLL-U Parser**: Convert between CoNLL-U format files and text files.
**Stanza Parser**: Process text data and parse syntactic structures using the Stanza library.
**Trankit Parser**: Process and parse syntactic structures using the Trankit library.
**Vectorize**: Utilities for vectorizing data for machine learning tasks.
### Utilities

The utils directory contains additional utilities for data processing and analysis:

**Compare Models**: Compare performance metrics of different classification models.

### Data
The data directory contains sample data files in CoNLL-U format for testing and experimentation.

### Classifiers

- **Support Vector Machine (SVM):**
    - The SVM classifier is implemented using scikit-learn's \`SVC\` class with a linear kernel. Training and testing data are loaded from the pickle files, preprocessed, and fed into the classifier.

- **Decision Tree:**
    - A Decision Tree classifier is trained and tested using scikit-learn's \`DecisionTreeClassifier\`. The default settings are used for this classifier.

- **Random Forest:**
    - The Random Forest classifier is implemented using scikit-learn's \`RandomForestClassifier\`. It consists of an ensemble of decision trees and is trained on the dataset to perform classification.

- **Logistic Regression:**
    - Logistic Regression is applied using scikit-learn's \`LogisticRegression\` class. It's a linear model suitable for binary classification tasks.

- **K-Nearest Neighbors (KNN):**
    - The KNN classifier is implemented using scikit-learn's \`KNeighborsClassifier\`. It classifies samples based on the majority class among its k-nearest neighbors.
- **## Artificial Neural Network:**
    - An artificial neural network (ANN) model is built using Keras. It consists of multiple layers with dropout regularization and sigmoid activation functions. The model is trained using the training data and evaluated on the test data.
- ## Model Comparisons

- Performance metrics such as accuracy, precision, recall, and F1-score are computed for each classifier. Confusion matrices and ROC curves are also generated to visualize the performance.


## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the GNU General Public License v3.0 License. See the LICENSE file for details.
