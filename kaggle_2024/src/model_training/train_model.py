import click
import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score
from sklearn.metrics import precision_recall_curve
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
from typing import List, Tuple


TARGET = 'IsBadBuy'
PROB_THRESHOLD = 0.5   

@click.command()
@click.option("--data-file-path", default="kaggle_2024/data/final/engineered_features.csv")
@click.option("--output-folder", default="kaggle_2024/src/model_training/")
def train_model(data_file_path: str, output_folder: str):    
    df = pd.read_csv(data_file_path)
    features = list(df.columns.values)
    features.remove(TARGET)
    X_train, X_valid, y_train, y_valid = _get_training_and_validation_sets(df, features)
    rf, y_train_preds, y_valid_preds = _get_model_and_predictions(X_train, y_train, X_valid)

    _summarize_findings(y_train, y_train_preds, PROB_THRESHOLD)
    _summarize_findings(y_valid, y_valid_preds, PROB_THRESHOLD)

    _save_precision_recall_curve(y_train, y_train_preds, output_folder)
    _save_permutation_importance(rf, X_valid, y_valid, features, output_folder)

def _save_permutation_importance(model: object, X_valid: np.ndarray, y_valid: np.ndarray, features: List[str], output_folder: str) -> None:
    result = permutation_importance(model, X_valid, y_valid, n_repeats=5, random_state=42)
    importance_df = pd.DataFrame(data={
    'feature': features,
    'importances_mean': result['importances_mean'],
    'importances_std': result['importances_std']
    })
    importance_df = importance_df.sort_values('importances_mean',ascending=False)
    filename = os.path.join(output_folder, 'permutation_importance.csv')
    importance_df.to_csv(filename, index=False)

def _save_precision_recall_curve(y_train: np.ndarray, y_train_preds: np.ndarray, output_folder: str) -> None:
    precision, recall, _ = precision_recall_curve(y_train, y_train_preds)
    plt.plot(recall, precision)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    filename = os.path.join(output_folder, 'precision_recall.png')
    plt.savefig(filename)

def _get_model_and_predictions(X_train: np.ndarray, y_train: np.ndarray, X_valid: np.ndarray) -> Tuple[object, np.ndarray, np.ndarray]:
    rf = RandomForestClassifier(max_depth = 5, n_estimators=100, random_state = 42)
    rf.fit(X_train, y_train)
    y_train_preds = rf.predict_proba(X_train)[:,1]
    y_valid_preds = rf.predict_proba(X_valid)[:,1]
    return rf, y_train_preds, y_valid_preds

def _get_training_and_validation_sets(df: pd.DataFrame, features: List[str]) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    # Shuffle first in case the dates are in order
    df = df.sample(n = len(df), random_state = 42)
    validation = df.sample(frac = 0.3, random_state = 42)
    train = df.drop(validation.index)
    X_train = train[features].values
    X_valid = validation[features].values
    y_train = train[TARGET].values
    y_valid = validation[TARGET].values
    return X_train, X_valid, y_train, y_valid

def _calculate_specificity(y_actual, y_pred, PROB_THRESHOLD):
    return sum((y_pred < PROB_THRESHOLD) & (y_actual == 0)) /sum(y_actual == 0)

def _summarize_findings(y_actual, y_pred, PROB_THRESHOLD): 
    auc = roc_auc_score(y_actual, y_pred)
    accuracy = accuracy_score(y_actual, (y_pred > PROB_THRESHOLD))
    recall = recall_score(y_actual, (y_pred > PROB_THRESHOLD))
    precision = precision_score(y_actual, (y_pred > PROB_THRESHOLD))
    specificity = _calculate_specificity(y_actual, y_pred, PROB_THRESHOLD)
    f1_score = _calculate_f1_score(precision, recall)
    print(f'AUC: {auc}')
    print(f'Accuracy: {accuracy}')
    print(f'Recall: {recall}')
    print(f'Precision: {precision}')
    print(f'Specificity: {specificity}')
    print(f'f1 score: {f1_score}')


def _calculate_f1_score(precision: float, recall: float) -> float:
    return 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0


if __name__ == "__main__":
    train_model()