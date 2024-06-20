import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

app = Flask(__name__)
 
data = pd.read_csv("C:/Users/pc/Downloads/archive (13)/DailyDelhiClimateTest.csv")
data = data.dropna()
 
data['temp_humidity'] = data['meantemp'] * data['humidity']
data['temp_wind_speed'] = data['meantemp'] * data['wind_speed']
data['humidity_wind_speed'] = data['humidity'] * data['wind_speed']

X = data[['meantemp', 'humidity', 'wind_speed', 'temp_humidity', 'temp_wind_speed', 'humidity_wind_speed']]
y = data['meanpressure']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
 
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
 
mae_rf = mean_absolute_error(y_test, y_pred_rf)
mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        meantemp = float(request.form['meantemp'])
        humidity = float(request.form['humidity'])
        wind_speed = float(request.form['wind_speed'])
         
        input_data = scaler.transform([[meantemp, humidity, wind_speed, 
                                        meantemp * humidity, meantemp * wind_speed, humidity * wind_speed]])
        
         
        prediction = rf_model.predict(input_data)[0]
        
        return render_template('prediction_result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
