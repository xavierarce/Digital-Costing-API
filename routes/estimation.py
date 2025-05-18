from flask import Flask,Blueprint, request, jsonify
import logging

app = Flask(__name__)

import models.estimation as estimation_model

estimation_bp = Blueprint('estimation_bp', __name__)

@estimation_bp.route('/save_estimation', methods=['POST'])
def save_estimation():
    print("Landed")
    app.logger.info("L|anded")
    # or
    logging.info("Landed")
    data = request.get_json()
    try:
        inserted_id = estimation_model.insert_estimation(data)
        return jsonify({'status': 'success', 'id': inserted_id})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500



@estimation_bp.route('/history', methods=['GET'])
def get_history():
    try:
        estimations = estimation_model.get_estimations()  # your method to fetch all
        return jsonify({'status': 'success', 'data': estimations})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
