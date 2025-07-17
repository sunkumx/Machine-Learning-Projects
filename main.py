from data_loader import load_data
from preprocessing import preprocess_data
from model import train_model, evaluate_model, save_model

def main():
    df = load_data()
    X_train, X_test, y_train, y_test, scaler = preprocess_data(df)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model, scaler)

if __name__ == "__main__":
    main()
