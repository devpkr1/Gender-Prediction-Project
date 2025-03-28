# Gender Prediction

## Description
This project implements a gender prediction model using various machine learning algorithms, including Logistic Regression, Multinomial Naive Bayes, and XGBoost. The model predicts gender based on names. The data is preprocessed by encoding the target variable and splitting it into training and validation sets.

## Installation Instructions
1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install pandas scikit-learn xgboost joblib matplotlib seaborn
   ```

## Usage
1. Open the Jupyter notebook `gender prediction.ipynb`.
2. Run the cells sequentially to load the data, preprocess it, build the models, and evaluate their performance.

## Model Evaluation
The following models are implemented:
- Logistic Regression
- Multinomial Naive Bayes
- XGBoost

Performance metrics such as accuracy, precision, recall, F1-score, and AUC are calculated for each model. The evaluation process includes generating confusion matrices and ROC-AUC curves for visual representation.

### Accuracy Metrics
![accuracy metrics for different models](accuracy-metrics.png)

### Confusion Matrices
![Confusion matrices for different models](confusion-matrics.png)

### ROC - AUC Curve
![ROC - AUC curve for Logistic Regression](roc-auc-curve.png)

## Deployment
The trained model is saved as `logistic regression.pkl` for future use.

## Live App
**App Link:-** [Click Here](https://pkr1234-gender-predictor-by-name.hf.space)

## License
This project is licensed under the [MIT License](LICENSE).
