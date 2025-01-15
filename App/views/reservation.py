from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime, date

from App.controllers import (
    create_reservation, 
    get_all_reservations,
    get_reservation,
    get_reservation_by_customer_id,
    get_reservation_by_grave_id,
    update_reservation,
    delete_reservation
)

reservation_views = Blueprint('reservation_views', __name__, template_folder='../templates')

@reservation_views.route('/api/reservations', methods=['POST'])
@jwt_required()
def create_reservation_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    data = request.json
    if not 'customer_id' in data or not 'reservation_date' in data or not 'grave_id' in data:
        return jsonify({"message":"Missing parameters"}), 400

    if not 'id' in data:
        reservation = create_reservation(data['customer_id'], datetime.fromisoformat(data['reservation_date']), data['grave_id'])
    else:
        reservation = get_reservation(id)(data['id'])
        if reservation.exists:
            return jsonify({"message":"Id already in use"}), 400
        reservation = create_reservation(data['customer_id'], datetime.fromisoformat(data['reservation_date']), data['grave_id'], data['id'])

    return jsonify({"message":"Reservation Created"}), 201

@reservation_views.route('/api/reservations', methods=['GET'])
@jwt_required()
def get_reservations_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403
        
    id = request.args.get('id')
    customer_id = request.args.get('customer_id')
    grave_id = request.args.get('grave_id')

    if id:
        reservation = get_reservation(id)
        if reservation.exists:
            reservation_dict = reservation.to_dict()
            reservation_dict['id'] = reservation.id
            return reservation_dict, 200
        return jsonify({"message":"Reservation Not Found"}), 404

    if customer_id:
        reservations = get_reservation_by_customer_id(customer_id)
        if reservations:
            reservations_array = []
            for reservation in reservations:
                reservation_dict = reservation.to_dict()
                reservation_dict['id'] = reservation.id
                reservations_array.append(reservation_dict)
            return jsonify(reservations_array), 200
        return jsonify({"message":"Reservation Not Found"}), 404

    if grave_id:
        reservations = get_reservation_by_grave_id(grave_id)
        if reservations:
            reservations_array = []
            for reservation in reservations:
                reservation_dict = reservation.to_dict()
                reservation_dict['id'] = reservation.id
                reservations_array.append(reservation_dict)
            return jsonify(reservations_array), 200
        return jsonify({"message":"Reservation Not Found"}), 404

    reservations = get_all_reservations()
    reservations_array = []
    for reservation in reservations:
        reservation_dict = reservation.to_dict()
        reservation_dict['id'] = reservation.id
        reservations_array.append(reservation_dict)
    return jsonify(reservations_array), 200

@reservation_views.route('/api/reservations', methods=['PUT'])
@jwt_required()
def update_reservation_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    data = request.json
    if not 'id' in data or not 'reservation_date' in data:
        return jsonify({"message":"Missing id or date parameter"}), 400
    reservation = get_reservation(data['id'])
    if not reservation.exists:
        return jsonify({"message":"Reservation not found"}), 404

    update_reservation(data['id'], datetime.fromisoformat(data['reservation_date']))
    return jsonify({"message":"Reservation updated"}), 200

@reservation_views.route('/api/reservations', methods=['DELETE'])
@jwt_required()
def delete_reservation_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    id = request.args.get('id')
    if not id:
        return jsonify({"message":"Missing id parameter"}), 400
    reservation = get_reservation(id)
    if reservation.exists:
        delete_reservation(id)
        return jsonify({"message":"Reservation Deleted"}), 200
    return jsonify({"message":"Reservation Not Found"}), 404