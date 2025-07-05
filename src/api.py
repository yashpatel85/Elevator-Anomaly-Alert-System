from flask import Flask, request, jsonify
from .inference import infer

app = Flask(__name__)

required_fields = {
    'vibration_mean', 'vibration_std', 'vibration_max', 'vibration_min',
    'humidity_mean', 'humidity_std', 'humidity_max', 'humidity_min',
    'revolution_mean', 'revolution_std', 'revolution_max', 'revolution_min',
} 


@app.route('/predict', methods = ['POST'])
def predict():
    data = request.get_json()

    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({'error': f"Missing Fields: {missing}"}), 400
    try:

        features = [float(data[k]) for k in sorted(data)]
    except (ValueError, TypeError):
        return jsonify({'error': 'All inputs must be numbers'}), 400
    result = infer(features, data)
    return jsonify(result)




if __name__ == '__main__':
    app.run(debug = True)

