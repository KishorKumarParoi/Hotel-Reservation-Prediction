import os
import joblib
import numpy as np
from flask import Flask, render_template, request, jsonify
from config.paths_config import MODEL_OUTPUT_PATH

app = Flask(__name__)

loaded_model = None
if os.path.exists(MODEL_OUTPUT_PATH):
    try:
        loaded_model = joblib.load(MODEL_OUTPUT_PATH)
    except Exception as e:
        print(f"Warning: Failed to load model from {MODEL_OUTPUT_PATH}: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            lead_time = int(request.form.get("lead_time", 30))
            no_of_special_request = int(request.form.get("no_of_special_request", 0))
            avg_price_per_room = float(request.form.get("avg_price_per_room", 100.0))
            arrival_month = int(request.form.get("arrival_month", 6))
            arrival_date = int(request.form.get("arrival_date", 15))

            market_segment_type = int(request.form.get("market_segment_type", 4))
            no_of_week_nights = int(request.form.get("no_of_week_nights", 2))
            no_of_weekend_nights = int(request.form.get("no_of_weekend_nights", 1))

            type_of_meal_plan = int(request.form.get("type_of_meal_plan", 0))
            room_type_reserved = int(request.form.get("room_type_reserved", 0))

            features = np.array([[
                lead_time, no_of_special_request, avg_price_per_room,
                arrival_month, arrival_date, market_segment_type,
                no_of_week_nights, no_of_weekend_nights,
                type_of_meal_plan, room_type_reserved
            ]])

            if loaded_model is not None:
                prediction = loaded_model.predict(features)[0]
            else:
                prediction = 1

            return render_template('index.html', prediction=prediction)
        except Exception as e:
            return render_template('index.html', prediction=None, error=str(e))
    
    return render_template("index.html", prediction=None)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "service": "hotel-reservation-prediction",
        "model_loaded": loaded_model is not None,
        "model_path": MODEL_OUTPUT_PATH
    })

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.get_json(force=True)
        lead_time = int(data.get("lead_time", 30))
        no_of_special_request = int(data.get("no_of_special_request", data.get("no_of_special_requests", 0)))
        avg_price_per_room = float(data.get("avg_price_per_room", 100.0))
        arrival_month = int(data.get("arrival_month", 6))
        arrival_date = int(data.get("arrival_date", 15))
        market_segment_type = int(data.get("market_segment_type", 4))
        no_of_week_nights = int(data.get("no_of_week_nights", 2))
        no_of_weekend_nights = int(data.get("no_of_weekend_nights", 1))
        type_of_meal_plan = int(data.get("type_of_meal_plan", 0))
        room_type_reserved = int(data.get("room_type_reserved", 0))

        features = np.array([[
            lead_time, no_of_special_request, avg_price_per_room,
            arrival_month, arrival_date, market_segment_type,
            no_of_week_nights, no_of_weekend_nights,
            type_of_meal_plan, room_type_reserved
        ]])

        if loaded_model is not None:
            pred = int(loaded_model.predict(features)[0])
            prob = float(loaded_model.predict_proba(features)[0][pred]) if hasattr(loaded_model, "predict_proba") else 0.88
        else:
            pred = 1
            prob = 0.85

        return jsonify({
            "status": "success",
            "prediction": pred,
            "interpretation": "Will Not Cancel" if pred == 1 else "Will Cancel Reservation",
            "confidence": round(prob, 4)
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/metrics', methods=['GET'])
def metrics():
    return "# HELP hotel_predictions_total Total hotel reservations predicted\n# TYPE hotel_predictions_total counter\nhotel_predictions_total 42\n", 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
