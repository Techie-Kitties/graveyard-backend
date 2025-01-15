from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime, date

from App.controllers import (
    create_payment, 
    get_all_payments,
    get_payment,
    get_payment_by_customer_id,
    get_payment_by_user_id,
    get_payment_by_date_created,
    delete_payment
)

payment_views = Blueprint('payment_views', __name__, template_folder='../templates')

@payment_views.route('/api/payments', methods=['POST'])
@jwt_required()
def create_payment_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    data = request.json
    if not 'customer_id' in data or not 'user_id' in data or not 'amount' in data or not 'date_created' in data:
        return jsonify({"message":"Missing parameters"}), 400

    if not 'id' in data:
        payment = create_payment(data['customer_id'], data['user_id'], data['amount'], datetime.fromisoformat(data['date_created']))
    else:
        payment = get_payment(data['id'])
        if payment.exists:
            return jsonify({"message":"Id already in use"}), 400
        payment = create_payment(data['customer_id'], data['user_id'], data['amount'], datetime.fromisoformat(data['date_created']), data['id'])

    return jsonify({"message":"payment Created"}), 201

@payment_views.route('/api/payments', methods=['GET'])
@jwt_required()
def get_payments_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    id = request.args.get('id')
    customer_id = request.args.get('customer_id')
    user_id = request.args.get('user_id')
    date_created = request.args.get('date_created')

    if id:
        payment = get_payment(id)
        if payment.exists:
            payment_dict = payment.to_dict()
            payment_dict['id'] = payment.id
            return payment_dict, 200
        return jsonify({"message":"payment Not Found"}), 404

    if customer_id:
        payments = get_payment_by_customer_id(customer_id)
        if payments:
            payments_array = []
            for payment in payments:
                payment_dict = payment.to_dict()
                payment_dict['id'] = payment.id
                payments_array.append(payment_dict)
            return jsonify(payments_array), 200
        return jsonify({"message":"payments Not Found"}), 404
    
    if user_id:
        payments = get_payment_by_user_id(user_id)
        if payments:
            payments_array = []
            for payment in payments:
                payment_dict = payment.to_dict()
                payment_dict['id'] = payment.id
                payments_array.append(payment_dict)
            return jsonify(payments_array), 200
        return jsonify({"message":"payments Not Found"}), 404
    
    if date_created:
        payments = get_payment_by_date_created(datetime.fromisoformat(date_created))
        if payments:
            payments_array = []
            for payment in payments:
                payment_dict = payment.to_dict()
                payment_dict['id'] = payment.id
                payments_array.append(payment_dict)
            return jsonify(payments_array), 200
        return jsonify({"message":"payments Not Found"}), 404

    payments = get_all_payments()
    payments_array = []
    for payment in payments:
        payment_dict = payment.to_dict()
        payment_dict['id'] = payment.id
        payments_array.append(payment_dict)
    return jsonify(payments_array), 200

@payment_views.route('/api/payments', methods=['DELETE'])
@jwt_required()
def delete_payment_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    id = request.args.get('id')
    if not id:
        return jsonify({"message":"Missing id parameter"}), 400
    payment = get_payment(id)
    if payment.exists:
        delete_payment(id)
        return jsonify({"message":"payment Deleted"}), 200
    return jsonify({"message":"payment Not Found"}), 404