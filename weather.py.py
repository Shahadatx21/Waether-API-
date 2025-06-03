from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model
model = joblib.load('weather_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    
    prediction = model.predict([[temp, humidity]])
    
    return render_template('index.html', prediction_text=f'🌤 Predicted Weather: {prediction[0]}')

if __name__ == '__main__':
    app.run(debug=True)
