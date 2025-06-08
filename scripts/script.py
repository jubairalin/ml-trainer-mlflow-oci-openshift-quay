
import argparse
import pandas as pd
import joblib
import mlflow
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=str, default='train')
parser.add_argument('--mlflow-uri', type=str, required=True)
args = parser.parse_args()

mlflow.set_tracking_uri(args.mlflow_uri)
mlflow.set_experiment("OpenShift-MLflow-Demo")

df = pd.read_csv("dataset.csv")
X = df[['ColumnA', 'ColumnB', 'ColumnC']].values
y = df['Label'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

with mlflow.start_run():
    model = DecisionTreeClassifier().fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    mlflow.log_metric("accuracy", acc)
    joblib.dump(model, "model.pkl")
    mlflow.log_artifact("model.pkl")
