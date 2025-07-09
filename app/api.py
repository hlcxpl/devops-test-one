from flask import Flask, request, jsonify
from app.reservations import check_availability

app= Flask(__name__)
reservations = []

@app.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    is_available = check_availability(reservations, data)
    
    if is_available:
        reservations.append(data)
        return jsonify({"message": "Reservation successful"}), 201
    else:
        return jsonify({"message": "Room not available"}), 400