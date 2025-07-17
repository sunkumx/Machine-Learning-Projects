from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Accuracy: {acc:.2f}")
    return acc

def save_model(model, scaler, model_path='model.joblib', scaler_path='scaler.joblib'):
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)
