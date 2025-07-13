import joblib

def predict_diabetes(input):
    model = joblib.load('saved\DecisionTreePrediction.pkl')
    prediction = model.predict(([input]))
    return prediction