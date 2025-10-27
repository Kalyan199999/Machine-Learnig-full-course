from flask import Flask, render_template, request
import joblib
import os
print("Current working directory:", os.getcwd())


app = Flask(__name__ ,template_folder='./templates')

# Load model and vectorizer
model = joblib.load('./models/model.pkl')

vectorizer = joblib.load('./models/vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input text
    text = request.form['news_text']
    
    # Transform text with the vectorizer
    transformed_text = vectorizer.transform([text])
    
    # Predict category
    prediction = model.predict(transformed_text)[0]
    
    return render_template('result.html', prediction=prediction, input_text=text)

if __name__ == "__main__":
    app.run(debug=True)
