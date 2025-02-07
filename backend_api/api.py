from flask import Flask, request, jsonify  
from flask_cors import CORS

app = Flask(__name__)  
CORS(app)
  
def calculate_bmi(weight, height):  
    """Calculate BMI given weight in kilograms and height in meters."""  
    return weight / (height ** 2)  
  
@app.route('/get_bmi', methods=['POST'])  
def calculate_bmi_endpoint():  
    data = request.get_json()  
    weight = data.get('weight')  
    height = data.get('height')  
  
    if weight is None or height is None:  
        return jsonify({'error': 'Please provide both weight and height'}), 400  
  
    try:  
        weight = float(weight)  
        height = float(height)  
    except ValueError:  
        return jsonify({'error': 'Weight and height must be numbers'}), 400  
  
    if height <= 0:  
        return jsonify({'error': 'Height must be greater than zero'}), 400  
  
    bmi = calculate_bmi(weight, height)  
    return jsonify({'bmi': bmi})  
  
app.run(host='0.0.0.0' ,port=8080)
