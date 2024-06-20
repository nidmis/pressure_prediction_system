# pressure_prediction_system
A web application built using Python, Flask, and HTML/CSS, designed to predict mean atmospheric pressure based on input parameters such as mean temperature, humidity, and wind speed. 

1)Technologies Used:

--Python: Used for data processing, model training (using scikit-learn), and web framework (Flask).

--Flask: A micro web framework in Python used for handling HTTP requests, rendering HTML templates, and integrating backend logic.

--HTML/CSS: Frontend markup and styling for the web application interface.

--scikit-learn: Python library used for machine learning tasks, including model selection, preprocessing, and evaluation.

2)Functionality:

--Input Form: Users can input mean temperature, humidity, and wind speed values into a form.

--Prediction: Upon submission, the application uses a trained Random Forest Regression model to predict the mean atmospheric pressure.

--Result Display: After prediction, users are shown the predicted mean pressure along with an option to return to the input form for further predictions.

--Background Animation: The application includes dynamic cloud animations moving across the screen from left to right and right to left to enhance visual appeal.

3)Features:

--Data Processing: Initial data is loaded from a CSV file, processed to handle missing values, and used to train a machine learning model.

--Model Training: A Random Forest Regression model is trained using processed data to predict mean pressure based on weather parameters.

--Interactive Interface: HTML forms allow seamless user interaction for inputting data and viewing predictions.

--Visual Appeal: Cloud animations in the background create a visually engaging experience without obstructing the main content.
