from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt

from App.controllers import (
    create_customer, 
    get_all_customers,
    get_customer,
    get_customer_by_name,
    update_customer,
    delete_customer
)

customer_views = Blueprint('customer_views', __name__, template_folder='../templates')

@customer_views.route('/api/customers', methods=['POST'])
@jwt_required()
def create_customer_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    data = request.json
    if not 'name' in data or not 'phone_number' in data or not 'email_address' in data:
        return jsonify({"message":"Missing parameters"}), 400

    if not 'id' in data:
        customer = create_customer(data['name'], data['phone_number'], data['email_address'])
    else:
        customer = get_customer(data['id'])
        if customer.exists:
            return jsonify({"message":"Id already in use"}), 400
        customer = create_customer(data['name'], data['phone_number'], data['email_address'], data['id'])

    return jsonify({"message":"customer Created"}), 201

@customer_views.route('/api/customers', methods=['GET'])
@jwt_required()
def get_customers_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    id = request.args.get('id')
    name = request.args.get('name')

    if id:
        customer = get_customer(id)
        if customer.exists:
            customer_dict = customer.to_dict()
            customer_dict['id'] = customer.id
            return customer_dict, 200
        return jsonify({"message":"Customer Not Found"}), 404

    if name:
        customers = get_customer_by_name(name)
        if customers:
            customers_array = []
            for customer in customers:
                customer_dict = customer.to_dict()
                customer_dict['id'] = customer.id
                customers_array.append(customer_dict)
            return jsonify(customers_array), 200
        return jsonify({"message":"Customer Not Found"}), 404

    customers = get_all_customers()
    customers_array = []
    for customer in customers:
        customer_dict = customer.to_dict()
        customer_dict['id'] = customer.id
        customers_array.append(customer_dict)
    return jsonify(customers_array), 200

@customer_views.route('/api/customers', methods=['PUT'])
@jwt_required()
def update_customer_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    data = request.json
    if not 'id' in data:
        return jsonify({"message":"Missing id parameter"}), 400
    customer = get_customer(data['id'])
    if not customer.exists:
        return jsonify({"message":"customer not found"}), 404

    if 'phone_number' in data:
        phone_number = data['phone_number']
    else:
        phone_number = None
    
    if 'email_address' in data:
        email_address = data['email_address']
    else:
        email_address = None

    if phone_number == None and email_address == None:
        return jsonify({"message":"Missing phone_number and/or email_address parameter"}), 400

    update_customer(data['id'], phone_number, email_address)
    return jsonify({"message":"customer updated"}), 200

@customer_views.route('/api/customers', methods=['DELETE'])
@jwt_required()
def delete_customer_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    id = request.args.get('id')
    if not id:
        return jsonify({"message":"Missing id parameter"}), 400
    customer = get_customer(id)
    if customer.exists:
        delete_customer(id)
        return jsonify({"message":"Customer Deleted"}), 200
    return jsonify({"message":"Customer Not Found"}), 404